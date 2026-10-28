# -*- coding: utf-8 -*-
"""index.html의 헤더·푸터·스타일을 재사용해 suspension/index.html을 생성.
   본문 내용은 아래 CONTENT 영역만 수정하면 됨.  실행: python3 build_suspension.py"""
import re, pathlib

root = pathlib.Path(__file__).parent
src = (root / 'index.html').read_text(encoding='utf-8')

def between(s, a, b):
    i = s.index(a); j = s.index(b, i)
    return s[i:j]

head_links = between(src, '<link rel="preconnect"', '<style>')
style = between(src, '<style>', '</style>') + '</style>'
ticker = between(src, '<!-- ===== TICKER ===== -->', '<!-- ===== HEADER ===== -->')
header = between(src, '<!-- ===== HEADER ===== -->', '<main id="top">')
footer = between(src, '<!-- ===== FOOTER ===== -->', '<script>')
js_head = between(src, "const IMG_BASE = 'https://", "/* ===== bikes grid ===== */")
js_head = re.sub(r"/\* =+\n   MODELS.*?=+ \*/\n", "", js_head, flags=re.S)
js_reveal = between(src, "/* ===== reveal on scroll ===== */", "applyLang();")

# 서브페이지에서는 메인 앵커를 /#... 로
for blk in ('header',):
    pass
header = header.replace('href="#bikes"', 'href="/#bikes"').replace('href="#moulton"', 'href="/#moulton"') \
               .replace('href="#history"', 'href="/#history"').replace('href="#buy"', 'href="/#buy"') \
               .replace('href="#top"', 'href="/"')
# 푸터 서스펜션 링크는 현재 페이지
footer = footer.replace('href="https://www.moultonbicycles.co.uk/pages/moulton-suspension" target="_blank" rel="noopener"', 'href="/suspension/"')

# applyLang에서 메인 전용 renderGrid/renderPress 제거, 타이틀 교체
js_head = js_head.replace("  renderGrid(); renderPress(pressIdx, true);\n", "")
js_head = re.sub(r"document\.title = \{[^\n]*\}\[LANG\];",
  "document.title = {ko:'몰튼 서스펜션 | Moulton Bicycles Korea', en:'Moulton Suspension | Moulton Bicycles Korea', ja:'モールトンのサスペンション | Moulton Bicycles Korea', zh:'莫尔顿避震系统 | Moulton Bicycles Korea'}[LANG];", js_head)
# MODELS/PRESS 배열은 서브페이지에 불필요
js_head = re.sub(r"const MODELS = \[.*?\n\];\n", "", js_head, flags=re.S)
js_head = re.sub(r"const PRESS = \[.*?\n\];\n", "", js_head, flags=re.S)

sub_css = """
<style>
/* ===== Suspension page ===== */
.phero{position:relative;height:min(78vh,760px);min-height:460px;overflow:hidden;background:#161616}
.phero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.phero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.7) 0%,rgba(0,0,0,.35) 45%,rgba(0,0,0,.05) 75%),linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.5) 100%)}
.phero__txt{position:absolute;left:0;right:0;bottom:clamp(40px,8vh,80px);z-index:2;color:#fff}
.phero__txt .eyebrow{color:#fff;opacity:.85}
.phero__txt h1{font-size:clamp(36px,6vw,84px);line-height:1;letter-spacing:-.03em;text-shadow:0 2px 24px rgba(0,0,0,.35)}
html[lang="ko"] .phero__txt h1{font-family:var(--ko);font-weight:500;word-break:keep-all}
html[lang="ja"] .phero__txt h1,html[lang="zh"] .phero__txt h1{letter-spacing:0;line-height:1.1}
.phero__txt p{color:rgba(255,255,255,.85);margin-top:20px;max-width:52ch}
.lede{padding:clamp(64px,8vw,110px) 0}
.lede__grid{display:grid;grid-template-columns:1fr 1.2fr;gap:clamp(32px,6vw,96px);align-items:start}
.lede h2{font-family:var(--en);font-weight:300;font-size:clamp(28px,3.6vw,48px);letter-spacing:-.02em}
html[lang="ko"] .lede h2,html[lang="ja"] .lede h2,html[lang="zh"] .lede h2{font-weight:300}
.lede p+p{margin-top:16px}
.lede .stat{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px;padding-top:28px;border-top:1px solid var(--line)}
.lede .stat b{display:block;font-family:var(--en);font-size:clamp(26px,3vw,40px);font-weight:600;letter-spacing:-.02em;line-height:1}
.lede .stat span{display:block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-top:8px;font-family:var(--en)}
.wide{position:relative;aspect-ratio:21/9;overflow:hidden;background:var(--bg-soft)}
.wide img{width:100%;height:100%;object-fit:cover}
.overview{background:var(--bg-soft);padding:clamp(64px,8vw,110px) 0}
.overview__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.ov{background:var(--bg-soft);padding:34px 28px 38px}
.ov .num{font-family:var(--en);font-size:11px;letter-spacing:.22em;color:var(--red);margin-bottom:20px}
.ov h3{font-size:20px;margin-bottom:12px}
.ov p{font-size:15px}
.sys{padding:clamp(40px,6vw,80px) 0 0}
.sys__head{margin-bottom:clamp(28px,4vw,48px)}
.sys__head .eyebrow{margin-bottom:10px}
.unit{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:clamp(32px,6vw,96px);padding:clamp(40px,6vw,80px) 0;border-top:1px solid var(--line)}
.unit__img{position:relative;aspect-ratio:4/3;overflow:hidden;background:var(--bg-soft)}
.unit__img img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.unit:hover .unit__img img{transform:scale(1.04)}
.unit:nth-child(even) .unit__img{order:2}
.unit__txt .tag{font-family:var(--en);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-3);margin-bottom:12px}
.unit__txt h3{font-family:var(--en);font-size:clamp(26px,3vw,40px);margin-bottom:18px;letter-spacing:-.02em}
.unit__txt p+p{margin-top:12px}
.spec{list-style:none;margin-top:24px;border-top:1px solid var(--line)}
.spec li{display:grid;grid-template-columns:150px 1fr;gap:16px;padding:11px 0;border-bottom:1px solid var(--line);font-size:14px}
.spec li b{font-family:var(--en);font-weight:600;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);padding-top:3px}
.cta{background:var(--ink);color:#fff;padding:clamp(64px,8vw,110px) 0;text-align:center}
.cta h2{margin-bottom:16px}
.cta p{color:rgba(255,255,255,.75);margin:0 auto 32px}
.cta .btn{margin:0 6px}
@media (max-width:1024px){.overview__grid{grid-template-columns:1fr}}
@media (max-width:820px){
  .lede__grid{grid-template-columns:1fr;gap:28px}
  .unit{grid-template-columns:1fr;gap:22px}
  .unit:nth-child(even) .unit__img{order:0}
  .wide{aspect-ratio:16/10}
  .spec li{grid-template-columns:110px 1fr}
}
@media (max-width:560px){.lede .stat{grid-template-columns:1fr 1fr}.phero{height:70vh}}
</style>"""

# ===================== CONTENT =====================
def t(ko, en, ja, zh):
    esc = lambda s: s.replace('"', '&quot;')
    return f'data-ko="{esc(ko)}" data-en="{esc(en)}" data-ja="{esc(ja)}" data-zh="{esc(zh)}"'

main = f"""
<main id="top">

<section class="phero">
  <img data-src="moulton-hydrolastic-rear-suspension-close-up.jpg" alt="Moulton Hydrolastic rear suspension" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow" {t('타협 없는 편안함','Comfort Without Compromise','妥協のない快適さ','毫不妥协的舒适')}>타협 없는 편안함</div>
    <h1 {t('몰튼 서스펜션','Moulton Suspension','モールトンのサスペンション','莫尔顿避震系统')}>몰튼 서스펜션</h1>
    <p {t('서스펜션은 모든 몰튼의 성능, 승차감, 효율의 중심에 있습니다. 그 뿌리는 알렉스 몰튼 박사의 자동차 서스펜션 연구에 닿아 있습니다.',
         'Suspension is central to the performance, comfort and efficiency of every Moulton, and its roots lie in Dr Alex Moulton’s automotive suspension work.',
         'サスペンションは、すべてのモールトンの性能、快適性、効率の中心にあります。その源流は、アレックス・モールトン博士の自動車サスペンション研究にあります。',
         '避震系统是每一台莫尔顿的性能、舒适与效率的核心，其根源在于亚历克斯·莫尔顿博士的汽车避震研究。')}>서스펜션은 모든 몰튼의 성능, 승차감, 효율의 중심에 있습니다. 그 뿌리는 알렉스 몰튼 박사의 자동차 서스펜션 연구에 닿아 있습니다.</p>
  </div>
</section>

<section class="lede">
  <div class="wrap lede__grid rv">
    <div>
      <div class="eyebrow">Engineering Efficiency Through Isolation</div>
      <h2 {t('분리가 만드는 효율','Efficiency through isolation','分離がもたらす効率','源于隔离的效率')}>분리가 만드는 효율</h2>
    </div>
    <div>
      <p {t('1950~60년대 알렉스 몰튼은 BMC를 위해 유체로 앞뒤를 연결한 하이드로라스틱 서스펜션을 개발했습니다. 오스틴·모리스 미니에 처음 적용된 이 시스템은 이후 400만 대가 넘는 자동차에 장착되었습니다.',
           'In the 1950s and 60s Alex Moulton developed the fluid-interconnected Hydrolastic suspension for BMC. First fitted to the Austin and Morris Mini, it went on to equip more than four million cars.',
           '1950〜60年代、アレックス・モールトンはBMCのために、前後を流体で連結したハイドロラスティック・サスペンションを開発しました。オースチン／モーリス・ミニに初めて採用され、その後400万台以上の車に搭載されました。',
           '20世纪50至60年代，亚历克斯·莫尔顿为 BMC 开发了前后液压互联的 Hydrolastic 避震系统。该系统首先应用于 Austin 与 Morris Mini，此后装配于超过四百万辆汽车。')}>1950~60년대 알렉스 몰튼은 BMC를 위해 유체로 앞뒤를 연결한 하이드로라스틱 서스펜션을 개발했습니다. 오스틴·모리스 미니에 처음 적용된 이 시스템은 이후 400만 대가 넘는 자동차에 장착되었습니다.</p>
      <p {t('자전거에서 그가 택한 해법은 더 부드러운 타이어나 휘어지는 프레임이 아니라, 가볍고 짧은 스트로크의 서스펜션이었습니다. 서스펜션이 달린 몰튼에서는 바퀴만 상하로 움직입니다. 노면의 충격 에너지는 라이더에게 전달되는 대신 서스펜션에 저장되고 제어됩니다.',
           'For the bicycle, his answer was lightweight, short-travel suspension rather than softer tyres or a flexible frame. On a suspended Moulton only the wheels move vertically; the energy of a bump is stored and controlled by the suspension instead of being passed to the rider.',
           '自転車において彼が選んだ答えは、柔らかいタイヤやしなるフレームではなく、軽量でショートストロークのサスペンションでした。サスペンション付きのモールトンでは、上下に動くのはホイールだけ。路面からの衝撃エネルギーはライダーに伝わる代わりに、サスペンションに蓄えられ、制御されます。',
           '对于自行车，他的答案不是更软的轮胎或可弯曲的车架，而是轻量、短行程的避震。在带避震的莫尔顿上，只有车轮上下运动；路面冲击的能量被避震系统储存并控制，而不是传递给骑行者。')}>자전거에서 그가 택한 해법은 더 부드러운 타이어나 휘어지는 프레임이 아니라, 가볍고 짧은 스트로크의 서스펜션이었습니다. 서스펜션이 달린 몰튼에서는 바퀴만 상하로 움직입니다. 노면의 충격 에너지는 라이더에게 전달되는 대신 서스펜션에 저장되고 제어됩니다.</p>
      <p {t('그 결과는 승차감, 접지력, 피로 감소, 그리고 실제 도로에서의 효율로 돌아옵니다.',
           'The result is comfort, traction, less fatigue and real-world efficiency on real roads.',
           'その結果は、快適性、トラクション、疲労の軽減、そして実際の路面での効率として返ってきます。',
           '其结果体现为舒适性、抓地力、更少的疲劳，以及真实路面上的效率。')}>그 결과는 승차감, 접지력, 피로 감소, 그리고 실제 도로에서의 효율로 돌아옵니다.</p>
      <div class="stat">
        <div><b>1962</b><span {t('첫 서스펜션 자전거','First suspended bicycle','初のサス付き自転車','首款避震自行车')}>첫 서스펜션 자전거</span></div>
        <div><b>4M+</b><span {t('하이드로라스틱 장착 자동차','Cars on Hydrolastic','ハイドロラスティック搭載車','搭载 Hydrolastic 的汽车')}>하이드로라스틱 장착 자동차</span></div>
        <div><b>0</b><span {t('프레임 플렉스','Frame flex','フレームのたわみ','车架形变')}>프레임 플렉스</span></div>
      </div>
    </div>
  </div>
</section>

<div class="wide rv"><img data-src="moulton-ns-safari-willow-green-side-view-landscape.jpg" alt="Moulton NS Safari" loading="lazy"></div>

<section class="overview">
  <div class="wrap">
    <div class="overview__grid rv">
      <div class="ov">
        <div class="num">01</div>
        <h3 {t('리어 서스펜션','Rear Suspension','リアサスペンション','后避震')}>리어 서스펜션</h3>
        <p {t('유체 댐핑 방식의 하이드로라스틱 유닛 또는 유지보수가 필요 없는 모노스피어 드라이 콘 시스템을 사용합니다. 뒷바퀴는 프레임과 독립적으로 움직입니다.',
             'Either the fluid-damped Hydrolastic unit or the maintenance-free Monosphere dry-cone system, letting the rear wheel move independently of the frame.',
             '流体減衰式のハイドロラスティック・ユニット、またはメンテナンスフリーのモノスフィア・ドライコーン・システムを採用。後輪はフレームから独立して動きます。',
             '采用液压阻尼的 Hydrolastic 单元，或免维护的 Monosphere 干式橡胶锥系统，使后轮独立于车架运动。')}>유체 댐핑 방식의 하이드로라스틱 유닛 또는 유지보수가 필요 없는 모노스피어 드라이 콘 시스템을 사용합니다. 뒷바퀴는 프레임과 독립적으로 움직입니다.</p>
      </div>
      <div class="ov">
        <div class="num">02</div>
        <h3 {t('프론트 서스펜션','Front Suspension','フロントサスペンション','前避震')}>프론트 서스펜션</h3>
        <p {t('마찰이 없는 플렉시터 시스템 또는 조절이 가능한 리딩 링크 설계를 사용합니다.',
             'Either the friction-free Flexitor system or the adjustable Leading Link design.',
             '摩擦のないフレキシター・システム、または調整可能なリーディングリンク設計を採用しています。',
             '采用无摩擦的 Flexitor 系统，或可调节的 Leading Link 设计。')}>마찰이 없는 플렉시터 시스템 또는 조절이 가능한 리딩 링크 설계를 사용합니다.</p>
      </div>
      <div class="ov">
        <div class="num">03</div>
        <h3 {t('피벗 베어링','Pivot Bearings','ピボットベアリング','枢轴轴承')}>피벗 베어링</h3>
        <p {t('리어 포크와 피벗 어셈블리는 서스펜션의 구조적 핵심입니다. 현행 대부분의 모델은 바텀 브래킷이 리어 트라이앵글에 직접 붙는 일체형 리어 포크를 사용해 페달링 힘과 서스펜션 움직임을 분리합니다. 브론즈 부시와 스테인리스 저널을 사용하며, 일부 모델은 실드 피벗을 갖춥니다.',
             'The rear fork and pivot assembly is the structural core of the suspension. Most current models use a unified rear fork with the bottom bracket attached directly to the rear triangle, isolating pedalling forces from suspension movement. Bronze bushes run on stainless-steel journals; some models have sealed pivots.',
             'リアフォークとピボットアッセンブリーは、サスペンションの構造的な核です。現行のほとんどのモデルは、ボトムブラケットがリアトライアングルに直接取り付けられた一体型リアフォークを採用し、ペダリングの力をサスペンションの動きから分離します。ブロンズブッシュとステンレスジャーナルを使用し、一部モデルはシールドピボットを備えます。',
             '后叉与枢轴总成是避震系统的结构核心。现行大多数车型采用一体式后叉，中轴直接安装在后三角上，将踩踏力与避震运动隔离。采用青铜衬套与不锈钢轴颈，部分车型配有密封枢轴。')}>리어 포크와 피벗 어셈블리는 서스펜션의 구조적 핵심입니다. 현행 대부분의 모델은 바텀 브래킷이 리어 트라이앵글에 직접 붙는 일체형 리어 포크를 사용해 페달링 힘과 서스펜션 움직임을 분리합니다. 브론즈 부시와 스테인리스 저널을 사용하며, 일부 모델은 실드 피벗을 갖춥니다.</p>
      </div>
    </div>
  </div>
</section>

<section class="sys">
  <div class="wrap">
    <div class="sys__head rv">
      <div class="eyebrow">The Systems</div>
      <h2 {t('네 가지 시스템','Four systems','4つのシステム','四种系统')}>네 가지 시스템</h2>
    </div>

    <article class="unit rv">
      <div class="unit__img"><img data-src="preview_images/5b467deba71c410992790f74be8f0674.thumbnail.0000000000.jpg" alt="Moulton Monosphere" loading="lazy"></div>
      <div class="unit__txt">
        <div class="tag" {t('리어 · 드라이 콘','Rear · Dry cone','リア · ドライコーン','后 · 干式橡胶锥')}>리어 · 드라이 콘</div>
        <h3>Monosphere</h3>
        <p {t('유압 유체가 없는 속이 빈 고무 콘 시스템입니다. 콘이 압축과 전단으로 동시에 작동해 스프링 레이트가 매끄럽게 상승하며, 댐핑은 고무 자체의 히스테리시스에서 나오기 때문에 별도의 댐퍼가 필요 없습니다. 1959년부터 2000년까지 BMC 미니에 쓰인 고무 콘과 같은 원리입니다.',
             'A dry, hollow rubber cone with no hydraulic fluid. The cone works in compression and shear for a smoothly rising spring rate, and damping comes from the hysteresis of the rubber itself, so no separate damper is needed. The concept mirrors the rubber cone used in the BMC Mini from 1959 to 2000.',
             '油圧流体を使わない中空ゴムコーンのシステムです。コーンが圧縮とせん断で同時に働くことで、スプリングレートは滑らかに立ち上がり、減衰はゴム自体のヒステリシスから生まれるため、別途ダンパーは不要です。1959年から2000年までBMCミニに使われたゴムコーンと同じ原理です。',
             '无液压油的中空橡胶锥系统。橡胶锥同时在压缩与剪切状态下工作，弹簧刚度平滑上升；阻尼来自橡胶自身的滞后特性，无需单独的阻尼器。其原理与1959至2000年间 BMC Mini 所用的橡胶锥相同。')}>유압 유체가 없는 속이 빈 고무 콘 시스템입니다. 콘이 압축과 전단으로 동시에 작동해 스프링 레이트가 매끄럽게 상승하며, 댐핑은 고무 자체의 히스테리시스에서 나오기 때문에 별도의 댐퍼가 필요 없습니다. 1959년부터 2000년까지 BMC 미니에 쓰인 고무 콘과 같은 원리입니다.</p>
        <ul class="spec">
          <li><b {t('댐핑','Damping','減衰','阻尼')}>댐핑</b><span {t('고무 히스테리시스','Rubber hysteresis','ゴムのヒステリシス','橡胶滞后')}>고무 히스테리시스</span></li>
          <li><b {t('유지보수','Maintenance','メンテナンス','维护')}>유지보수</b><span {t('불필요','Maintenance-free','不要','免维护')}>불필요</span></li>
          <li><b {t('조절','Adjustment','調整','调节')}>조절</b><span {t('대체 캠 플레이트로 스프링 레이트 약 10% 상향 (트래블 유지)','Alternative cam plate raises the spring rate by about 10% without reducing travel','別売カムプレートでスプリングレートを約10%向上（トラベルは維持）','更换凸轮板可将弹簧刚度提高约10%，行程不变')}>대체 캠 플레이트로 스프링 레이트 약 10% 상향 (트래블 유지)</span></li>
        </ul>
      </div>
    </article>

    <article class="unit rv">
      <div class="unit__img"><img data-src="preview_images/dc9f12bb19634bb48c89395d12d3999c.thumbnail.0000000000.jpg" alt="Moulton Hydrolastic" loading="lazy"></div>
      <div class="unit__txt">
        <div class="tag" {t('리어 · 유체 댐핑','Rear · Fluid damped','リア · 流体減衰','后 · 液压阻尼')}>리어 · 유체 댐핑</div>
        <h3>Hydrolastic</h3>
        <p {t('고무 콘 스프링과 내부 유체 댐핑을 결합한 유닛입니다. 유체가 정밀 밸브를 지나 보조 챔버로 이동하며 댐핑을 만들고, 내부 공기 챔버가 유체를 가압합니다. 완전히 밀폐된 구조라 윤활이 필요 없으며, 점진적인 스프링 레이트와 하중 아래에서의 안정성을 제공합니다.',
             'A rubber cone spring combined with internal fluid damping. Fluid passes through a precision valve into a secondary chamber to provide damping, and an internal air chamber pressurises the fluid. Fully self-contained and needing no lubrication, it gives a progressive spring rate and greater stability under load.',
             'ゴムコーンスプリングと内部流体減衰を組み合わせたユニットです。流体が精密バルブを通って副室へ移動することで減衰を生み、内部のエアチャンバーが流体を加圧します。完全密閉構造のため潤滑は不要で、プログレッシブなスプリングレートと荷重下での安定性をもたらします。',
             '将橡胶锥弹簧与内部液压阻尼相结合的单元。液体经精密阀门流入副腔产生阻尼，内部气室对液体加压。完全封闭，无需润滑，提供渐进式弹簧刚度与负载下更好的稳定性。')}>고무 콘 스프링과 내부 유체 댐핑을 결합한 유닛입니다. 유체가 정밀 밸브를 지나 보조 챔버로 이동하며 댐핑을 만들고, 내부 공기 챔버가 유체를 가압합니다. 완전히 밀폐된 구조라 윤활이 필요 없으며, 점진적인 스프링 레이트와 하중 아래에서의 안정성을 제공합니다.</p>
        <ul class="spec">
          <li><b {t('댐핑','Damping','減衰','阻尼')}>댐핑</b><span {t('정밀 밸브 유체 댐핑','Fluid, through a precision valve','精密バルブによる流体減衰','精密阀门液压阻尼')}>정밀 밸브 유체 댐핑</span></li>
          <li><b {t('스프링','Spring','スプリング','弹簧')}>스프링</b><span {t('고무 콘 + 가압 공기 챔버','Rubber cone + pressurised air chamber','ゴムコーン + 加圧エアチャンバー','橡胶锥 + 加压气室')}>고무 콘 + 가압 공기 챔버</span></li>
          <li><b {t('유지보수','Maintenance','メンテナンス','维护')}>유지보수</b><span {t('밀폐형, 윤활 불필요','Sealed, no lubrication','密閉型、潤滑不要','密封，无需润滑')}>밀폐형, 윤활 불필요</span></li>
        </ul>
      </div>
    </article>

    <article class="unit rv">
      <div class="unit__img"><img data-src="preview_images/19d30096d6114dae8c90d813f91c953c.thumbnail.0000000000.jpg" alt="Moulton Leading Link" loading="lazy"></div>
      <div class="unit__txt">
        <div class="tag" {t('프론트 · 조절식','Front · Adjustable','フロント · 調整式','前 · 可调节')}>프론트 · 조절식</div>
        <h3>Leading Link</h3>
        <p {t('포크 크라운 앞쪽에 떠 있는 포크 스터럽이 스테인리스 리딩 링크 위에서 회전합니다. 주된 지지는 스티어링 컬럼 안의 코일 스프링이 맡습니다. 스프링 레이트는 용도에 따라 달라서, 스피드나 경기용은 단단하게, 편안함을 위해서는 부드럽게 구성합니다. 라이더의 체중과 취향에 맞춰 라이드 하이트와 댐핑을 조절할 수 있습니다.',
             'A floating fork stirrup sits ahead of the fork crown and pivots on stainless-steel leading links, with a coil spring inside the steering column providing the main support. Spring rates vary by intent: firmer for speed or competition, softer for comfort. Ride height and damping are adjustable to rider weight and preference.',
             'フォーククラウンの前方に浮かぶフォークスターラップが、ステンレス製リーディングリンクの上で回転します。主な支持はステアリングコラム内のコイルスプリングが担います。スプリングレートは用途により、スピードや競技用は硬めに、快適性重視なら柔らかめに。ライダーの体重や好みに合わせてライドハイトと減衰を調整できます。',
             '浮动式前叉镫位于前叉肩前方，绕不锈钢前导连杆转动，主要支撑来自转向管内的螺旋弹簧。弹簧刚度因用途而异：竞速或比赛偏硬，舒适取向偏软。可根据骑行者体重与偏好调节离地高度与阻尼。')}>포크 크라운 앞쪽에 떠 있는 포크 스터럽이 스테인리스 리딩 링크 위에서 회전합니다. 주된 지지는 스티어링 컬럼 안의 코일 스프링이 맡습니다. 스프링 레이트는 용도에 따라 달라서, 스피드나 경기용은 단단하게, 편안함을 위해서는 부드럽게 구성합니다. 라이더의 체중과 취향에 맞춰 라이드 하이트와 댐핑을 조절할 수 있습니다.</p>
        <ul class="spec">
          <li><b {t('스프링','Spring','スプリング','弹簧')}>스프링</b><span {t('스티어링 컬럼 내 코일 스프링','Coil spring in the steering column','ステアリングコラム内コイルスプリング','转向管内螺旋弹簧')}>스티어링 컬럼 내 코일 스프링</span></li>
          <li><b {t('링크','Links','リンク','连杆')}>링크</b><span {t('스테인리스 스틸','Stainless steel','ステンレススチール','不锈钢')}>스테인리스 스틸</span></li>
          <li><b {t('조절','Adjustment','調整','调节')}>조절</b><span {t('라이드 하이트, 댐핑','Ride height, damping','ライドハイト、減衰','离地高度、阻尼')}>라이드 하이트, 댐핑</span></li>
        </ul>
      </div>
    </article>

    <article class="unit rv">
      <div class="unit__img"><img data-src="preview_images/a7096f4a4b48495d9e5efcd93741c192.thumbnail.0000000000.jpg" alt="Moulton Flexitor" loading="lazy"></div>
      <div class="unit__txt">
        <div class="tag" {t('프론트 · 무마찰','Front · Friction-free','フロント · 無摩擦','前 · 无摩擦')}>프론트 · 무마찰</div>
        <h3>Flexitor</h3>
        <p {t('비틀림 전단 상태의 고무 요소가 위치 결정, 스프링, 댐핑을 한 몸에서 해냅니다. 미끄러지는 면이 없어 정지 마찰이 사실상 없고, 닳거나 고착될 피벗도 없습니다. 범프 스톱과 리바운드 스톱을 조절할 수 있으며, 소프트 락아웃 기능은 오르막이나 스프린트에서 트래블을 줄이면서도 충격 흡수를 일부 남겨 둡니다. 윤활이나 복잡한 정비가 필요 없습니다.',
             'Rubber elements in torsional shear provide location, springing and damping in a single unit. With no sliding surfaces there is virtually no static friction, and no pivots to wear or seize. Bump-stop and rebound-stop settings are adjustable, and a soft-lockout reduces travel for climbing or sprinting while keeping some shock absorption. No lubrication or complex servicing is required.',
             'ねじりせん断状態のゴム要素が、位置決め、スプリング、減衰を一体で担います。摺動面がないため静摩擦はほぼゼロ、摩耗や固着するピボットもありません。バンプストップとリバウンドストップは調整可能で、ソフトロックアウト機能は登坂やスプリント時にトラベルを抑えつつ、ある程度の衝撃吸収を残します。潤滑や複雑な整備は不要です。',
             '处于扭转剪切状态的橡胶元件在一个单元内同时完成定位、弹性与阻尼。没有滑动面，几乎没有静摩擦，也没有会磨损或卡死的枢轴。压缩止点与回弹止点均可调节，软锁定功能可在爬坡或冲刺时减少行程，同时保留部分减震。无需润滑或复杂保养。')}>비틀림 전단 상태의 고무 요소가 위치 결정, 스프링, 댐핑을 한 몸에서 해냅니다. 미끄러지는 면이 없어 정지 마찰이 사실상 없고, 닳거나 고착될 피벗도 없습니다. 범프 스톱과 리바운드 스톱을 조절할 수 있으며, 소프트 락아웃 기능은 오르막이나 스프린트에서 트래블을 줄이면서도 충격 흡수를 일부 남겨 둡니다. 윤활이나 복잡한 정비가 필요 없습니다.</p>
        <ul class="spec">
          <li><b {t('원리','Principle','原理','原理')}>원리</b><span {t('고무 비틀림 전단','Rubber in torsional shear','ゴムのねじりせん断','橡胶扭转剪切')}>고무 비틀림 전단</span></li>
          <li><b {t('마찰','Friction','摩擦','摩擦')}>마찰</b><span {t('미끄럼면 없음, 정지 마찰 거의 0','No sliding surfaces, near-zero stiction','摺動面なし、静摩擦ほぼゼロ','无滑动面，静摩擦几乎为零')}>미끄럼면 없음, 정지 마찰 거의 0</span></li>
          <li><b {t('조절','Adjustment','調整','调节')}>조절</b><span {t('범프 스톱, 리바운드 스톱, 소프트 락아웃','Bump stop, rebound stop, soft-lockout','バンプストップ、リバウンドストップ、ソフトロックアウト','压缩止点、回弹止点、软锁定')}>범프 스톱, 리바운드 스톱, 소프트 락아웃</span></li>
        </ul>
      </div>
    </article>

  </div>
</section>

<section class="cta">
  <div class="wrap rv">
    <div class="eyebrow" {t('직접 경험하기','Experience it','体感する','亲身体验')}>직접 경험하기</div>
    <h2 {t('설명보다 한 번의 시승','One ride says more than any explanation','どんな説明より、一度の試乗を','一次试骑胜过千言万语')}>설명보다 한 번의 시승</h2>
    <p {t('서울 반포 루비워크샵 몰튼 쇼룸에서 서스펜션의 차이를 직접 느껴 보세요.','Feel the difference for yourself at the Moulton showroom, Rubi Workshop in Banpo, Seoul.','ソウル・盤浦のRubi Workshopモールトンショールームで、サスペンションの違いをご体感ください。','欢迎到首尔盘浦 Rubi Workshop 莫尔顿展厅，亲身感受避震的不同。')}>서울 반포 루비워크샵 몰튼 쇼룸에서 서스펜션의 차이를 직접 느껴 보세요.</p>
    <a class="btn light" href="https://rubiworkshop.com/models" target="_blank" rel="noopener" {t('상담 신청','Consulting','ご相談はこちら','预约咨询')}>상담 신청</a>
    <a class="btn light" href="/#bikes" {t('전 모델 보기','View all bikes','全モデルを見る','查看全部车型')}>전 모델 보기</a>
  </div>
</section>

</main>
"""
# ===================== /CONTENT =====================

page = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>몰튼 서스펜션 | Moulton Bicycles Korea</title>
<meta name="description" content="하이드로라스틱, 모노스피어, 리딩 링크, 플렉시터. 알렉스 몰튼 박사의 자동차 서스펜션 연구에서 비롯된 몰튼 서스펜션의 원리와 네 가지 시스템.">
<meta property="og:title" content="Moulton Suspension | Moulton Bicycles Korea">
<meta property="og:description" content="Comfort without compromise. The four Moulton suspension systems explained.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://moultonbicycles.co.kr/suspension/">
<link rel="canonical" href="https://moultonbicycles.co.kr/suspension/">
{head_links}{style}
{sub_css}
</head>
<body>

{ticker}{header}{main}
{footer}<script>
{js_head}
{js_reveal}applyLang();
</script>
</body>
</html>
"""
out = root / 'suspension' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding='utf-8')
print('written', out, len(page), 'bytes')
