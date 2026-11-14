# -*- coding: utf-8 -*-
"""v15：三级可折叠目录（一级带序号）· 全站统一 · 自动展开当前位置 · 触屏去毛玻璃"""
import re, html as _h
from cci_text import HC, BC, COD, CREEDS

E = lambda s: _h.escape(str(s), quote=False)
A = lambda s: _h.escape(str(s), quote=True)

L1COL = {"index.html": "var(--prologue)", "history.html": "var(--teal)", "p1-misery.html": "var(--misery)",
         "p2-christ.html": "var(--deliver)", "p3-spirit.html": "var(--deliver)", "p4-law.html": "var(--gratitude)",
         "p5-prayer.html": "var(--gratitude)", "topics.html": "#2E7D32", "texts.html": "#5B4A2E"}


def _strip(s):
    return _h.unescape(re.sub(r'<[^>]+>', '', s)).strip()


def _sections(chunks):
    out = []
    for c in chunks:
        m = re.match(r'<section class="sec[^"]*" id="([\w-]+)">', c)
        if m:
            h = re.search(r'<h2>(?:<span class="h2e">([^<]*)</span>)?(.*?)</h2>', c, flags=re.S)
            if h:
                out.append((m.group(1), (h.group(1) or '').strip(), _strip(h.group(2))))
    return out


def structure(pages, PAGES, LDS, EMO):
    """返回 [(file, emoji, title, [L2...])]；L2=(id, emoji, title, extra, [L3...])；L3=(id, label, title)"""
    by_n = {d["n"]: d for d in LDS}
    S = []
    for f, e, sh, lg, rg in PAGES:
        L2 = []
        if rg:
            for n in range(rg[0], rg[1] + 1):
                d = by_n[n]
                qs = [q for q, _, _ in d["qas"]]
                qr = "%d-%d问" % (qs[0], qs[-1]) if len(qs) > 1 else "%d问" % qs[0]
                L3 = [("q%d" % q, "问%d" % q, HC[q]["q"]) for q in qs]
                L2.append(("ld%d" % n, EMO[n - 1], "%d · %s" % (n, d["title"]), qr, L3))
        elif f == "topics.html":
            secs = _sections(pages[f])
            tp = [s for s in secs if s[0].startswith("tp-")]
            ap = [s for s in secs if s[0].startswith("ap-")]
            other = [s for s in secs if not s[0].startswith(("tp-", "ap-"))]
            if tp:
                L2.append((tp[0][0], "🧩", "跨主日专题", "%d 篇" % len(tp), [(i, "", t) for i, em, t in tp]))
            for i, em, t in other:
                L2.append((i, em or "♾️", t, "", []))
            if ap:
                L2.append((ap[0][0], "📎", "附录", "%d 项" % len(ap), [(i, em, t) for i, em, t in ap]))
        else:
            for i, em, t in _sections(pages[f]):
                L2.append((i, em, t, "", []))
        SHORT = {"index.html": "总论", "history.html": "历史 · 地图 · 文化", "p1-misery.html": "总纲与困苦 · 1–4",
                 "p2-christ.html": "中保与圣子 · 5–19", "p3-spirit.html": "圣灵·教会·圣礼 · 20–31",
                 "p4-law.html": "感恩 · 十诫 · 32–44", "p5-prayer.html": "感恩 · 祷告 · 45–52", "topics.html": "专题 · 结语 · 附录"}
        S.append((f, e, SHORT.get(f, lg), L2))
    # 原文阅读室
    t2 = [("creeds", "📜", "三大普世信经", "", [("t-rd-apostles", "", CREEDS[0]["name"]), ("t-rd-nicene", "", CREEDS[1]["name"]), ("t-rd-athan", "", CREEDS[2]["name"])]),
          ("hc", "🕊️", "海德堡要理问答", "52 主日", [("hc%d" % d["n"], "主日%d" % d["n"], d["title"]) for d in LDS]),
          ("bc", "🏛️", "比利时信条", "37 条", [("bc%d" % a["no"], "第%d条" % a["no"], re.sub(r'^第.+?条\s*', '', a["title"])) for a in BC]),
          ("cod", "⚖️", "多特信经", "4 项教义", [("cod%d" % (j + 1), "", s["title"]) for j, s in enumerate(COD)])]
    S.append(("texts.html", "📜", "原文阅读室", t2))
    return S


def toc_html(S, cur):
    out = ['<div class="toc toc3" id="toc3">']
    for k, (f, e, title, L2) in enumerate(S):
        here = f == cur
        pre = '' if here else f
        col = L1COL.get(f, "var(--royal)")
        first = ('%s#%s' % (pre, L2[0][0])) if L2 else f
        out.append('<div class="t1%s" style="--tc:%s" data-f="%s"><div class="th1"><button class="tg" type="button" aria-label="展开/折叠"></button>'
                   '<a class="l1" href="%s"><span class="n1">%d</span><span class="emo">%s</span><span class="t">%s</span><span class="qr">%d</span></a></div><div class="tb1">'
                   % (" open" if here else "", col, f, A(first if not here else '#' + (L2[0][0] if L2 else 'top')), k + 1, e, E(title), len(L2)))
        for (i, em, t, extra, L3) in L2:
            n = re.match(r'ld(\d+)$', i)
            dn = ' data-n="%s"' % n.group(1) if n else ''
            has = bool(L3)
            out.append('<div class="t2%s"><div class="th2">%s<a class="l2" href="%s#%s"%s title="%s"><span class="emo">%s</span><span class="t">%s</span>%s</a></div>'
                       % (" has" if has else "", '<button class="tg" type="button" aria-label="展开/折叠"></button>' if has else '<i class="tgx"></i>',
                          pre, i, dn, A(t), em, E(t), '<span class="qr">(%s)</span>' % E(extra) if extra else ''))
            if has:
                out.append('<div class="tb2">' + ''.join('<a class="l3" href="%s#%s" title="%s">%s<span class="t">%s</span></a>'
                                                         % (pre, j, A(lab + " " + tt if lab else tt), '<span class="no3">%s</span>' % E(lab) if lab else '', E(tt)) for j, lab, tt in L3) + '</div>')
            out.append('</div>')
        out.append('</div></div>')
    out.append('</div>')
    return ''.join(out)


def apply(page, S, cur):
    """替换页面里 <nav class="side"> 的目录内容"""
    a = page.index('<nav class="side">') + len('<nav class="side">')
    b = page.index('</nav>', a)
    return page[:a] + toc_html(S, cur) + page[b:]


CSS13 = r"""
/* ===== v15 三级目录 ===== */
.toc3{padding:6px 8px 40px;font-family:var(--sans)}
.toc3 a{--tc:inherit!important}
.toc3 a{display:flex!important;align-items:center;gap:6px;min-width:0;white-space:nowrap;text-decoration:none;color:var(--ink-2);border-radius:8px;border-left:3px solid transparent;
 transition:background .18s,color .18s,border-color .18s}
.toc3 a .t{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis}
.toc3 a .emo,.toc3 a .qr,.toc3 a .n1,.toc3 a .no3{flex:none}
.toc3 .th1,.toc3 .th2{display:flex;align-items:center;gap:2px}
.toc3 .tg{flex:none;width:22px;height:22px;border:0;background:none;cursor:pointer;border-radius:6px;display:grid;place-items:center;color:var(--tc);padding:0}
.toc3 .tg::before{content:"";width:7px;height:7px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(-45deg);transition:transform .22s}
.toc3 .open>.th1 .tg::before,.toc3 .open>.th2 .tg::before{transform:rotate(45deg)}
.toc3 .tg:hover{background:color-mix(in srgb,var(--tc) 14%,transparent)}
.toc3 .tgx{flex:none;width:22px}
/* 一级 */
.toc3 .t1{margin:4px 0;border-radius:12px}
.toc3 .t1.open{background:color-mix(in srgb,var(--tc) 6%,transparent)}
.toc3 .l1{flex:1;padding:7px 8px;font-size:15px;font-weight:800;color:var(--tc)}
.toc3 .n1{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:var(--tc);color:#fff;font-size:12px;font-weight:800}
.toc3 .l1 .qr{font-size:11px;font-weight:600;color:var(--muted);background:var(--paper-3);border-radius:99px;padding:1px 7px}
.toc3 .tb1,.toc3 .tb2{display:none}
.toc3 .open>.tb1,.toc3 .open>.tb2{display:block;animation:fadein .2s ease}
/* 二级 */
.toc3 .t2{margin-left:14px;border-left:1.5px solid color-mix(in srgb,var(--tc) 22%,transparent)}
.toc3 .l2{flex:1;padding:5px 8px;font-size:14px}
.toc3 .l2 .qr{font-size:11px;color:var(--muted)}
/* 三级 */
.toc3 .tb2{margin-left:24px}
.toc3 .l3{padding:3px 8px;font-size:12.5px;color:var(--muted)}
.toc3 .no3{font-weight:700;color:var(--tc);font-size:11.5px;min-width:3.2em}
.toc3 a:hover{background:color-mix(in srgb,var(--tc) 10%,transparent);color:var(--tc);border-left-color:color-mix(in srgb,var(--tc) 45%,transparent)}
.toc3 a.active{background:linear-gradient(90deg,color-mix(in srgb,var(--tc) 22%,transparent),color-mix(in srgb,var(--tc) 3%,transparent))!important;
 color:var(--tc)!important;border-left-color:var(--tc)!important;font-weight:700}
.toc3 a.done .t::after{content:" ✓";color:var(--gratitude)}
.toc3 .t2.cur>.th2 .l2{color:var(--tc);font-weight:700}
.toc3 .ttools{display:flex;gap:6px;margin:2px 4px 8px}
.toc3 .ttools button{flex:1;font:600 12px var(--sans);padding:5px 8px;border-radius:8px;border:1px solid var(--rule);background:var(--paper);color:var(--ink-2);cursor:pointer}
.toc3 .ttools button:hover{color:var(--royal);border-color:var(--royal)}
/* 触屏：去毛玻璃、减阴影，滚动更轻 */
@media (pointer:coarse){.topbar,.glass,.side{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}
 .topbar{background:color-mix(in srgb,var(--paper) 96%,transparent)!important}.tile,.qa,.kb,.mw{box-shadow:none!important}}
"""

JS13 = r"""
(function(){var d=document,T=d.getElementById('toc3');if(!T)return;var side=d.querySelector('.side');
var tools=d.createElement('div');tools.className='ttools';tools.innerHTML='<button type="button" data-x="1">全部展开</button><button type="button" data-x="0">全部折叠</button><button type="button" data-x="c">只看当前</button>';
T.insertBefore(tools,T.firstChild);
function setOpen(el,v){el.classList.toggle('open',v);}
T.addEventListener('click',function(e){var b=e.target.closest('.tg');if(b){e.preventDefault();var p=b.parentElement.parentElement;setOpen(p,!p.classList.contains('open'));return;}
 var x=e.target.closest('.ttools button');if(x){var k=x.dataset.x;
  if(k==='1')T.querySelectorAll('.t1,.t2.has').forEach(function(z){setOpen(z,true);});
  else if(k==='0')T.querySelectorAll('.t1,.t2').forEach(function(z){setOpen(z,false);});
  else{T.querySelectorAll('.t1,.t2').forEach(function(z){setOpen(z,false);});var a=T.querySelector('a.active');if(a)reveal(a);else{var h=T.querySelector('.t1[data-f="'+(location.pathname.split('/').pop()||'index.html')+'"]');if(h)setOpen(h,true);}}}});
function reveal(a){var t2=a.closest('.t2'),t1=a.closest('.t1');if(t1)setOpen(t1,true);if(t2&&t2.classList.contains('has')){setOpen(t2,true);}
 T.querySelectorAll('.t2.cur').forEach(function(z){z.classList.remove('cur');});if(t2)t2.classList.add('cur');
 var r=a.getBoundingClientRect(),s=side.getBoundingClientRect();if(r.top<s.top+60||r.bottom>s.bottom-40)side.scrollTop+=r.top-s.top-s.height/2;}
window.__tocAct=function(a){if(!a||!T.contains(a))return;var prev=T.querySelector('.t2.cur.has');var nt2=a.closest('.t2');if(prev&&prev!==nt2)setOpen(prev,false);reveal(a);};
/* 当前问号（三级）高亮 */
var qs=[].slice.call(d.querySelectorAll('.ld .qa[id]'));if(qs.length&&'IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){
  T.querySelectorAll('a.l3.active').forEach(function(z){z.classList.remove('active');});var l=T.querySelector('a.l3[href="#'+en.target.id+'"]');if(l)l.classList.add('active');}});},{rootMargin:'-30% 0px -60% 0px'});qs.forEach(function(q){io.observe(q);});}
/* 已背熟标记 */
function done(){var s={};try{s=JSON.parse(localStorage.getItem('hc-done')||'{}');}catch(e){}T.querySelectorAll('a.l2[data-n]').forEach(function(a){a.classList.toggle('done',!!s[a.dataset.n]);});}
done();d.addEventListener('change',function(e){if(e.target.matches('.chk input'))setTimeout(done,50);});
if(location.hash){var a=T.querySelector('a[href="'+location.hash+'"]');if(a)setTimeout(function(){a.classList.add('active');reveal(a);},300);}
})();
"""
