/* Eonati: affiliate click tracking + sticky mobile bar + quiz. */
(function(){
  var page=(location.pathname.split('/').pop()||'index.html').replace('.html','');
  function designerOf(a){
    if(a.dataset&&a.dataset.d) return a.dataset.d;
    var h=a.href||'';
    if(h.indexOf('alestra')>-1) return 'alestra';
    if(h.indexOf('explorance')>-1) return 'juhi';
    if(h.indexOf('valeriiaty')>-1) return 'valeriia';
    return 'other';
  }
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href*="go.fiverr.com"]');
    if(!a) return;
    try{gtag('event','affiliate_click',{designer:designerOf(a),placement:(a.dataset&&a.dataset.p)||'inline',page:page,transport_type:'beacon'});}catch(err){}
  },true);

  // sticky bar: show after the first main button scrolls out of view
  var s=document.querySelector('.eo-sticky');
  var first=document.querySelector('[data-sticky-anchor]')||document.querySelector('.eo-btn[href*="go.fiverr"]');
  if(s&&first&&'IntersectionObserver' in window){
    var seen=false;
    new IntersectionObserver(function(es){
      es.forEach(function(en){
        if(!en.isIntersecting&&en.boundingClientRect.top<0) seen=true;
        s.classList.toggle('show',seen&&!en.isIntersecting);
      });
    }).observe(first);
  }

  // quiz
  var quiz=document.querySelector('.eo-quiz');
  if(quiz){
    var qs=[].slice.call(quiz.querySelectorAll('.eo-q')),score={juhi:0,alestra:0,valeriia:0},i=0;
    var bar=quiz.querySelector('.eo-bar i'),step=quiz.querySelector('.eo-step');
    function show(n){
      qs.forEach(function(q,k){q.classList.toggle('on',k===n);});
      bar.style.width=(n/qs.length*100)+'%';
      if(step) step.textContent='Question '+(n+1)+' of '+qs.length;
    }
    quiz.addEventListener('click',function(e){
      var b=e.target.closest('.eo-q button'); if(!b) return;
      (b.dataset.s||'').split(' ').forEach(function(t){var p=t.split(':');if(score[p[0]]!==undefined)score[p[0]]+=Number(p[1]||1);});
      i++;
      try{gtag('event','quiz_answer',{question:i,answer:b.dataset.v||''});}catch(err){}
      if(i<qs.length){show(i);return;}
      var win=Object.keys(score).sort(function(a,b){return score[b]-score[a];})[0];
      qs.forEach(function(q){q.classList.remove('on');});
      bar.style.width='100%'; if(step) step.textContent='Your match';
      var r=quiz.querySelector('.eo-result[data-r="'+win+'"]'); r.classList.add('on');
      try{gtag('event','quiz_result',{designer:win});}catch(err){}
      var st=document.querySelector('.eo-sticky');
      if(st){var src=r.querySelector('.eo-btn');var sa=st.querySelector('a');sa.href=src.href;sa.dataset.d=win;st.querySelector('div').innerHTML=r.dataset.sticky;}
      quiz.scrollIntoView({behavior:'smooth',block:'start'});
    });
    quiz.addEventListener('click',function(e){
      if(!e.target.closest('.eo-restart')) return;
      score={juhi:0,alestra:0,valeriia:0};i=0;
      quiz.querySelectorAll('.eo-result').forEach(function(r){r.classList.remove('on');});
      show(0);
    });
    show(0);
  }
})();
