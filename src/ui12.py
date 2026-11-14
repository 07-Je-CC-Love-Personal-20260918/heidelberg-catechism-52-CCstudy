# -*- coding: utf-8 -*-
"""v14：10 个免密钥底图＋切换器 · 1563 海德堡情景图 · 「一个主日下午」讲解图 · 标记按类聚焦"""

TILES_JS = r"""
var TILES=[
 {n:'Esri 街道',u:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',o:{attribution:'© Esri'}},
 {n:'Esri 地形',u:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',o:{attribution:'© Esri'}},
 {n:'Esri 国家地理风格',u:'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',o:{attribution:'© Esri, National Geographic',maxZoom:16}},
 {n:'Esri 卫星',u:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',o:{attribution:'© Esri, Maxar'}},
 {n:'高德 街道（中国大陆快）',u:'https://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',o:{subdomains:'1234',attribution:'© 高德地图'}},
 {n:'高德 卫星',u:'https://webst0{s}.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',o:{subdomains:'1234',attribution:'© 高德地图'}},
 {n:'OpenStreetMap',u:'https://tile.openstreetmap.org/{z}/{x}/{y}.png',o:{attribution:'© OpenStreetMap'}},
 {n:'OSM 人道主义',u:'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',o:{subdomains:'abc',attribution:'© OpenStreetMap, HOT'}},
 {n:'OpenTopoMap 地形',u:'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',o:{subdomains:'abc',attribution:'© OpenTopoMap',maxZoom:17}},
 {n:'CyclOSM',u:'https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png',o:{subdomains:'abc',attribution:'© CyclOSM, OpenStreetMap'}}];
function base(map,note){var k=0,layer=null,ok=0,bad=0,timer,manual=false,ls;try{ls=localStorage}catch(e){}
 var saved=null;try{saved=ls&&ls.getItem('hc-tiles');}catch(e){}
 var idx=TILES.map(function(t){return t.n;}).indexOf(saved);
 function use(i,byUser){if(layer)map.removeLayer(layer);k=i;ok=0;bad=0;manual=!!byUser;var t=TILES[i];
  layer=L.tileLayer(t.u,Object.assign({maxZoom:18,crossOrigin:true},t.o)).addTo(map);sel.value=i;
  note.textContent='底图：'+t.n+' · 载入中…';
  layer.on('tileload',function(){ok++;if(ok===4)note.textContent='底图：'+t.n;});
  layer.on('tileerror',function(){bad++;if(bad>=4&&ok<2)next();});
  clearTimeout(timer);timer=setTimeout(function(){if(ok<2)next();},5000);}
 function next(){var n=(k+1)%TILES.length;if(n===(idx>=0?idx:0)){note.textContent='在线底图暂不可用，请参看示意图或稍后切换底图';return;}note.textContent=TILES[k].n+' 无响应，自动切换…';use(n);}
 var C=L.Control.extend({options:{position:'topright'},onAdd:function(){var dv=L.DomUtil.create('div','tilepick');
   dv.innerHTML='<label>🗺️ 底图</label>';sel=L.DomUtil.create('select','',dv);
   TILES.forEach(function(t,i){var o=document.createElement('option');o.value=i;o.textContent=t.n;sel.appendChild(o);});
   L.DomEvent.disableClickPropagation(dv);L.DomEvent.disableScrollPropagation(dv);
   sel.addEventListener('change',function(){use(+sel.value,true);try{ls&&ls.setItem('hc-tiles',TILES[+sel.value].n);}catch(e){}
     document.querySelectorAll('.tilepick select').forEach(function(s){if(s!==sel&&s._use)s._use(+sel.value);});});
   sel._use=function(i){use(i,true);};return dv;}});
 var sel;map.addControl(new C());use(idx>=0?idx:0);}
"""

SCENE_SVG = r"""<svg viewBox="0 0 900 430" class="svg7 scene14" role="img" aria-label="1563 年海德堡城情景示意图">
<defs><linearGradient id="sky14" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#BFD9F2"/><stop offset="1" stop-color="#F6EBD3"/></linearGradient>
<linearGradient id="hill14" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7FA36B"/><stop offset="1" stop-color="#4E7A47"/></linearGradient>
<linearGradient id="riv14" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5FA8D3"/><stop offset="1" stop-color="#2E77B8"/></linearGradient></defs>
<rect width="900" height="430" fill="url(#sky14)"/>
<g class="cloud14 c1"><ellipse cx="120" cy="60" rx="46" ry="16"/><ellipse cx="150" cy="52" rx="30" ry="14"/></g>
<g class="cloud14 c2"><ellipse cx="620" cy="44" rx="56" ry="17"/><ellipse cx="660" cy="36" rx="32" ry="14"/></g>
<path d="M0 250 C120 150 260 120 380 170 C460 205 520 140 640 120 C760 100 840 170 900 160 L900 300 L0 300Z" fill="url(#hill14)"/>
<path d="M0 250 C140 230 300 260 420 245 C560 228 700 250 900 236 L900 300 L0 300Z" fill="#6F955F" opacity=".7"/>
<!-- 城堡 -->
<g class="bld14"><rect x="560" y="132" width="110" height="52" rx="3" fill="#C9705A"/><rect x="548" y="112" width="22" height="72" fill="#B85E49"/><rect x="662" y="118" width="20" height="66" fill="#B85E49"/>
<path d="M548 112 l11 -16 l11 16Z M662 118 l10 -15 l10 15Z" fill="#7A3A2C"/><rect x="580" y="148" width="10" height="14" fill="#5B2A20"/><rect x="606" y="148" width="10" height="14" fill="#5B2A20"/><rect x="632" y="148" width="10" height="14" fill="#5B2A20"/></g>
<!-- 城区 -->
<rect x="0" y="292" width="900" height="34" fill="#E7D7B8"/>
<g class="bld14"><rect x="120" y="248" width="70" height="46" fill="#F1E3C6" stroke="#A88B5C"/><path d="M116 248 L155 222 L194 248Z" fill="#9C4A3A"/><rect x="146" y="268" width="16" height="26" fill="#6B4A2E"/></g>
<g class="bld14"><rect x="300" y="236" width="96" height="58" fill="#EADBC0" stroke="#A88B5C"/><path d="M296 236 L348 206 L400 236Z" fill="#8E3F31"/><rect x="336" y="160" width="24" height="76" fill="#D9C7A4" stroke="#A88B5C"/><path d="M332 160 L348 128 L364 160Z" fill="#7A3A2C"/><circle cx="348" cy="180" r="7" fill="#fff" stroke="#7A3A2C"/></g>
<g class="bld14"><rect x="450" y="258" width="60" height="36" fill="#F3E6CC" stroke="#A88B5C"/><path d="M446 258 L480 238 L514 258Z" fill="#9C4A3A"/></g>
<g class="bld14"><rect x="220" y="262" width="54" height="32" fill="#F3E6CC" stroke="#A88B5C"/><path d="M216 262 L247 244 L278 262Z" fill="#A55444"/></g>
<!-- 内卡河与老桥 -->
<path d="M0 330 C200 318 420 338 640 324 C760 316 840 330 900 324 L900 380 L0 380Z" fill="url(#riv14)"/>
<path class="ripple14" d="M40 350 h60 M180 360 h50 M330 348 h70 M520 362 h50 M700 352 h60 M820 366 h40" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".7"/>
<g><path d="M690 330 q30 -24 60 0 q30 -24 60 0 q30 -24 60 0" fill="none" stroke="#B9A07A" stroke-width="10"/><rect x="684" y="318" width="192" height="8" fill="#B9A07A"/></g>
<rect x="0" y="380" width="900" height="50" fill="#D7C39C"/>
<!-- 编号 -->
<g class="pin14"><circle cx="615" cy="100" r="15"/><text x="615" y="105">1</text></g>
<g class="pin14"><circle cx="348" cy="112" r="15"/><text x="348" y="117">2</text></g>
<g class="pin14"><circle cx="155" cy="206" r="15"/><text x="155" y="211">3</text></g>
<g class="pin14"><circle cx="480" cy="222" r="15"/><text x="480" y="227">4</text></g>
<g class="pin14"><circle cx="780" cy="296" r="15"/><text x="780" y="301">5</text></g>
<g class="pin14"><circle cx="90" cy="352" r="15"/><text x="90" y="357">6</text></g>
<text class="lab14" x="890" y="420" text-anchor="end">示意情景，非比例实景</text>
</svg>"""

SCENE_ITEMS = [
 ("🏰", "选侯宫堡", "腓特烈三世（「虔诚者」）的驻地。他亲自主持要理编订，1566 年在奥格斯堡帝国议会上为它辩护。"),
 ("⛪", "圣灵教堂", "城中主堂。1560 年圣餐之争就发生在这类祭坛前；改革后祭坛换成圣餐桌，下午在此讲要理。"),
 ("🎓", "海德堡大学（1386）", "德意志最古老的大学之一。乌尔西努任神学教授、俄利维亚努任宫廷传道，神学团队出自这里。"),
 ("🖨️", "印刷作坊", "1563 年由约翰·迈耶（Johann Mayer）印行；同年连出三版，并编入选侯的《教会规程》。"),
 ("🌉", "内卡河老桥", "通往莱茵的水道：书籍、学生与流亡者沿河往返，把要理带向低地与更远之处。"),
 ("🛶", "流亡者与学生", "来自低地、法国的改革宗难民在普法尔茨落脚；他们日后把海德堡要理带回荷兰。"),
]

AFTERNOON = [
 ("🌅", "上午 · 讲道", "按经文讲解圣经，宣告福音。"),
 ("🕑", "下午 · 要理讲道", "牧师按当周「主日」讲解问答；52 个主日，一年讲完一轮。"),
 ("🗣️", "孩子当众答问", "年轻人背诵并回答本周问答，会众一同复习。"),
 ("🏠", "家中复习", "家长在家带领背诵，一周后再讲下一个主日。"),
 ("🍞", "圣餐前查问", "领圣餐前由长老探访、查问信仰，要理是共同的标准。"),
]


def scene_sections():
    items = ''.join('<li style="--i:%d"><b class="nomk"><span class="sn14">%d</span>%s %s</b><p>%s</p></li>' % (i, i + 1, e, t, x)
                    for i, (e, t, x) in enumerate(SCENE_ITEMS))
    steps = '<i class="af-ar">→</i>'.join('<div class="af14" style="--i:%d"><em>%s</em><b class="nomk">%s</b><p>%s</p></div>' % (i, e, t, x)
                                         for i, (e, t, x) in enumerate(AFTERNOON))
    return ('<section class="sec histsec" id="hist-scene"><div class="eyebrow">SCAENA · 1563</div><h2>情景图：1563 年的海德堡</h2>'
            '<p class="lead">一座河谷里的大学城：山上是选侯，城中是教会与大学，脚下是通往莱茵的河。按编号对照右侧说明。</p>'
            '<div class="sc14"><div class="zbox">%s<button class="zbtn" type="button">⤢ 放大</button></div><ol class="sclist">%s</ol></div></section>'
            '<section class="sec histsec" id="hist-sunday"><div class="eyebrow">USUS · DOMINICA</div><h2>讲解图：要理问答怎样「用」——一个主日下午</h2>'
            '<p class="lead">「52 个主日」不是章节编号，而是讲道日程：1563 年的《教会规程》要求每个主日下午讲一段，让全会众一年学完一遍。</p>'
            '<div class="aflow">%s</div>'
            '<p class="fnote7">💡 所以每个主日的长度大致相当于一次讲道。照这个节奏学：每周一个主日，先背问答，再读解读，周末用闪卡复习。</p></section>') % (SCENE_SVG, items, steps)


CSS12 = r"""
/* ===== v14 底图切换器 ===== */
.tilepick{background:color-mix(in srgb,var(--paper-2) 94%,transparent);border:1px solid var(--rule);border-radius:12px;padding:5px 8px;box-shadow:0 6px 18px -8px rgba(0,0,0,.35);
 display:flex;align-items:center;gap:6px;font:600 12.5px var(--sans);color:var(--ink-2)}
.tilepick select{font:500 12.5px var(--sans);border:1px solid var(--rule);border-radius:8px;padding:3px 4px;background:var(--paper);color:var(--ink);max-width:170px}
@media (max-width:560px){.tilepick label{display:none}.tilepick select{max-width:128px}}
/* 情景图 */
.sc14{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:14px;align-items:start}
@media (max-width:900px){.sc14{grid-template-columns:1fr}}
.scene14{border-radius:16px;box-shadow:var(--sh2)}
.cloud14 ellipse{fill:#fff;opacity:.9}
.cloud14{animation:drift14 26s linear infinite}.cloud14.c2{animation-duration:34s;animation-delay:-10s}
@keyframes drift14{from{transform:translateX(-160px)}to{transform:translateX(980px)}}
.ripple14{stroke-dasharray:30 40;animation:flowmv 2.4s linear infinite}
.pin14 circle{fill:#D2283E;stroke:#fff;stroke-width:3}.pin14 text{font:800 15px var(--sans);fill:#fff;text-anchor:middle}
.pin14{animation:pop .5s both}.lab14{font:12px var(--sans);fill:#6b5d45}
.sclist{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.sclist li{border-radius:12px;padding:10px 12px;background:var(--paper-2);border:1px solid var(--rule);animation:rise .5s both;animation-delay:calc(var(--i)*.07s)}
.sclist b{display:flex;align-items:center;gap:6px;font-size:15.5px}
.sn14{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:#D2283E;color:#fff;font:800 12px var(--sans)}
.sclist p{margin:4px 0 0;font-size:.93em;line-height:1.7;color:var(--ink-2)}
/* 讲解流程 */
.aflow{display:flex;flex-wrap:wrap;align-items:stretch;gap:8px}
.af14{flex:1 1 150px;border-radius:14px;padding:12px 14px;background:linear-gradient(150deg,color-mix(in srgb,var(--gratitude) 16%,var(--paper-2)),var(--paper-2));
 border:1px solid color-mix(in srgb,var(--gratitude) 35%,var(--rule));animation:rise .5s both;animation-delay:calc(var(--i)*.1s)}
.af14 em{font-style:normal;font-size:26px}.af14 b{display:block;margin-top:2px;color:var(--brass);font-size:15px}.af14 p{margin:4px 0 0;font-size:.92em;line-height:1.65}
.af-ar{align-self:center;font-style:normal;font-weight:800;color:var(--brass)}
@media (max-width:640px){.af-ar{display:none}.af14{flex-basis:100%}}
/* ===== v14 标记按类聚焦 ===== */
.mklegend .mkl{cursor:pointer;border-radius:8px;padding:2px 4px;transition:background .2s,opacity .2s}
.mklegend .mkl:hover{background:color-mix(in srgb,var(--royal) 8%,transparent)}
.mklegend .mkl.on{background:color-mix(in srgb,var(--royal) 14%,transparent);box-shadow:inset 0 0 0 1.5px var(--royal)}
.mkhint{font:12px var(--sans);color:var(--muted)}
body[data-mkf] mark.mk{opacity:.38;filter:grayscale(.7)}
body[data-mkf="mk-god"] mark.mk-god,body[data-mkf="mk-sin"] mark.mk-sin,body[data-mkf="mk-chr"] mark.mk-chr,body[data-mkf="mk-spi"] mark.mk-spi,
body[data-mkf="mk-cov"] mark.mk-cov,body[data-mkf="mk-key"] mark.mk-key,body[data-mkf="mk-gra"] mark.mk-gra{opacity:1;filter:none;outline:2px solid currentColor;outline-offset:1px}
"""

JS12 = r"""
(function(){var d=document,lg=d.getElementById('mkLegend');if(!lg)return;
lg.querySelectorAll('.mkl').forEach(function(c){var m=c.querySelector('mark');if(m){var k=[].filter.call(m.classList,function(x){return x!=='mk'&&x.indexOf('mk-')===0;})[0];if(k){c.dataset.c=k;c.title='只看「'+m.textContent+'」这一类（再点取消）';}}});
var h=d.createElement('span');h.className='mkhint';h.textContent='点类别 → 只看这一类';var btn=d.getElementById('mkBtn');lg.insertBefore(h,btn);
lg.addEventListener('click',function(e){var c=e.target.closest('.mkl[data-c]');if(!c)return;var k=c.dataset.c,on=d.body.dataset.mkf===k;
 lg.querySelectorAll('.mkl.on').forEach(function(x){x.classList.remove('on');});
 if(on){delete d.body.dataset.mkf;}else{d.body.dataset.mkf=k;c.classList.add('on');}});
})();
"""
CSS12 += r"""
/* 经文出处：长串经文在栏内换行，不越栏 */
details.refs ol li{overflow-wrap:anywhere;word-break:break-word;break-inside:avoid;min-width:0}
details.refs ol{column-gap:22px}
"""
