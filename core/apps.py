from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        import core.translation  # noqa
        _patch_django_context_copy()


def _patch_django_context_copy():
    """
    Fix admin 500 on Python 3.13 / 3.14 with Django + Jazzmin.

    Original error:
      AttributeError: 'super' object has no attribute 'dicts'

    Incomplete patch caused:
      AttributeError: 'RequestContext' object has no attribute 'render_context'
    """
    import sys
    if sys.version_info < (3, 13):
        return

    try:
        from django.template.context import BaseContext, Context, RequestContext, RenderContext

        def _full_copy(self):
            cls = self.__class__
            duplicate = cls.__new__(cls)
            # Copy entire instance state
            duplicate.__dict__.update(self.__dict__)
            # dicts must be a new list (Django's expected semantics)
            if hasattr(self, 'dicts'):
                duplicate.dicts = self.dicts[:]
            # render_context must always exist for Context / RequestContext
            if not hasattr(duplicate, 'render_context') or duplicate.render_context is None:
                duplicate.render_context = RenderContext()
            elif hasattr(self, 'render_context') and hasattr(self.render_context, 'dicts'):
                # fresh RenderContext with same stack
                rc = RenderContext()
                rc.dicts = self.render_context.dicts[:]
                duplicate.render_context = rc
            return duplicate

        BaseContext.__copy__ = _full_copy
        Context.__copy__ = _full_copy
        RequestContext.__copy__ = _full_copy
    except Exception:
        pass
