(function () {
  // Theme toggle
  var toggle = document.getElementById('themeToggle');
  var form = document.getElementById('themeForm');
  var input = document.getElementById('themeInput');
  if (toggle && form && input) {
    toggle.addEventListener('click', function () {
      var html = document.documentElement;
      var current = html.getAttribute('data-theme') || 'dark';
      var next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      input.value = next;
      form.submit();
    });
  }

  // Terminal typing
  var body = document.getElementById('termBody');
  if (!body) return;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var lines = [
    { prompt: true, text: 'whoami' },
    { out: true, text: '{' },
    { out: true, text: '  "name": <span class="str">"Esmaeil Taghizadeh"</span>,' },
    { out: true, text: '  "role": <span class="str">"Software Developer"</span>,' },
    { out: true, text: '  "stack": [<span class="str">"Python"</span>, <span class="str">"Django"</span>, <span class="str">"Flask"</span>, <span class="str">"SQL"</span>],' },
    { out: true, text: '  "location": <span class="str">"Qeshm, Iran"</span>,' },
    { out: true, text: '  "status": <span class="str">"available_for_hire"</span>' },
    { out: true, text: '}' }
  ];
  if (reduceMotion) {
    var html = '';
    lines.forEach(function (l) {
      if (l.prompt) html += '<div class="term-line"><span class="prompt">$</span> <span class="cmd">' + l.text + '</span></div>';
      else html += '<div class="term-line">' + l.text + '</div>';
    });
    body.innerHTML = html + '<span class="cursor"></span>';
    return;
  }
  var i = 0;
  function typeLine() {
    if (i >= lines.length) {
      body.innerHTML += '<span class="cursor"></span>';
      return;
    }
    var l = lines[i];
    var div = document.createElement('div');
    div.className = 'term-line';
    body.appendChild(div);
    if (l.prompt) {
      var raw = l.text;
      var j = 0;
      div.innerHTML = '<span class="prompt">$</span> ';
      var interval = setInterval(function () {
        div.innerHTML = '<span class="prompt">$</span> <span class="cmd">' + raw.slice(0, j + 1) + '</span>';
        j++;
        if (j >= raw.length) {
          clearInterval(interval);
          i++;
          setTimeout(typeLine, 220);
        }
      }, 45);
    } else {
      div.innerHTML = l.text;
      div.style.opacity = 0;
      requestAnimationFrame(function () {
        div.style.transition = 'opacity .25s';
        div.style.opacity = 1;
      });
      i++;
      setTimeout(typeLine, 130);
    }
  }
  typeLine();
})();

// Wizard
(function () {
  var form = document.getElementById('projectForm');
  if (!form) return;
  var order = ['1', '2', '3', '4', 'review', 'success'];
  var current = 0;
  var panels = {};
  form.querySelectorAll('.step-panel').forEach(function (p) { panels[p.dataset.step] = p; });
  var dots = document.querySelectorAll('.step-dot');
  var labels = document.querySelectorAll('.steps-labels span');
  var prevBtn = document.getElementById('prevBtn');
  var nextBtn = document.getElementById('nextBtn');
  var reviewList = document.getElementById('reviewList');
  var fieldMeta = {
    fullname: 'نام', email: 'ایمیل', phone: 'تلفن', company: 'شرکت',
    ptype: 'نوع پروژه', details: 'توضیح پروژه', budget: 'بودجه', timeline: 'بازه زمانی',
    contactPref: 'روش تماس ترجیحی', extra: 'توضیح اضافه'
  };
  form.querySelectorAll('.radio-card').forEach(function (card) {
    card.addEventListener('click', function () {
      form.querySelectorAll('.radio-card').forEach(function (c) { c.classList.remove('checked'); });
      card.classList.add('checked');
      card.querySelector('input').checked = true;
    });
  });
  function showStep(idx) {
    order.forEach(function (key) { panels[key].classList.remove('active'); });
    panels[order[idx]].classList.add('active');
    var stepNum = order[idx];
    var isNumbered = !isNaN(stepNum);
    dots.forEach(function (d) {
      var n = parseInt(d.dataset.dot, 10);
      d.classList.toggle('active', isNumbered && n === parseInt(stepNum, 10));
      d.classList.toggle('done', isNumbered ? n < parseInt(stepNum, 10) : true);
    });
    labels.forEach(function (l) {
      l.classList.toggle('active', isNumbered && l.dataset.label === stepNum);
    });
    prevBtn.style.visibility = idx === 0 ? 'hidden' : 'visible';
    if (order[idx] === 'review') {
      buildReview();
      nextBtn.textContent = 'ارسال درخواست';
    } else if (order[idx] === 'success') {
      nextBtn.textContent = 'تأیید';
      nextBtn.type = 'submit';
    } else if (idx === 3) {
      nextBtn.textContent = 'مرور نهایی';
      nextBtn.type = 'button';
    } else {
      nextBtn.textContent = 'بعدی';
      nextBtn.type = 'button';
    }
  }
  function validateStep(idx) {
    var step = order[idx];
    if (step === 'review' || step === 'success') return true;
    var panel = panels[step];
    var required = panel.querySelectorAll('[required]');
    for (var i = 0; i < required.length; i++) {
      if (!required[i].value.trim()) {
        required[i].focus();
        return false;
      }
    }
    if (step === '2') {
      var checked = panel.querySelector('input[name="ptype"]:checked');
      if (!checked) return false;
    }
    return true;
  }
  function buildReview() {
    var data = new FormData(form);
    reviewList.innerHTML = '';
    Object.keys(fieldMeta).forEach(function (key) {
      var val = (data.get(key) || '').toString().trim();
      if (!val) return;
      var li = document.createElement('li');
      li.innerHTML = '<span>' + fieldMeta[key] + '</span><span>' + val.replace(/</g, '&lt;') + '</span>';
      reviewList.appendChild(li);
    });
  }
  nextBtn.addEventListener('click', function (e) {
    if (order[current] === 'success') return;
    if (order[current] === 'review') {
      current++;
      showStep(current);
      return;
    }
    if (!validateStep(current)) return;
    current = Math.min(current + 1, order.length - 1);
    showStep(current);
  });
  prevBtn.addEventListener('click', function () {
    current = Math.max(current - 1, 0);
    showStep(current);
  });
  showStep(0);
})();
