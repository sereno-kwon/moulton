# -*- coding: utf-8 -*-
"""/the-hall 페이지 본문 (UK 'The Hall Estate' 페이지 번역). build.py가 읽어 the-hall/index.html 생성.
   투어·숙박 안내는 알렉스 몰튼 자선 신탁 사이트(moultontrust.org)로 연결."""
from build import t

SLUG = 'the-hall'
TITLE_KO = '홀 에스테이트 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'홀 에스테이트 | Moulton Bicycles Korea', en:'The Hall Estate | Moulton Bicycles Korea', ja:'ホール・エステート | Moulton Bicycles Korea', zh:'The Hall 庄园 | Moulton Bicycles Korea'}"
DESCRIPTION = '모든 것이 시작된 곳. 브래드퍼드 온 에이번의 알렉스 몰튼 가문 저택 홀 에스테이트, 지금도 몰튼 프레임이 만들어지는 마구간과 1963년의 바이시클 웍스.'
OG_TITLE = 'The Hall Estate | Moulton Bicycles Korea'
OG_DESC = 'Where it all began. The ancestral home of Dr Alex Moulton and the home of Moulton Bicycles.'

TRUST = 'https://moultontrust.org'

CSS = """
/* ===== The Hall page ===== */
.eyebrow{font-size:14px;letter-spacing:.18em;margin-bottom:16px}
.phero{position:relative;height:min(78vh,760px);min-height:460px;overflow:hidden;background:#161616}
.phero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.phero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.7) 0%,rgba(0,0,0,.35) 45%,rgba(0,0,0,.05) 75%),linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.5) 100%)}
.phero__txt{position:absolute;left:0;right:0;bottom:clamp(40px,8vh,80px);z-index:2;color:#fff}
.phero__txt .eyebrow{color:#fff;opacity:.85;font-size:15px;margin-bottom:22px}
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
.lede .stat b{display:block;font-family:var(--en);font-size:clamp(24px,2.6vw,36px);font-weight:600;letter-spacing:-.02em;line-height:1}
.lede .stat span{display:block;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-top:8px;font-family:var(--en)}

.wide{position:relative;aspect-ratio:21/9;overflow:hidden;background:var(--bg-soft)}
.wide img{width:100%;height:100%;object-fit:cover}

/* craft */
.craft{padding:clamp(64px,8vw,110px) 0}
.craft__grid{display:grid;grid-template-columns:1fr 1.2fr;gap:clamp(32px,6vw,96px);align-items:start;margin-bottom:clamp(40px,6vw,72px)}
.craft h2{margin-bottom:16px}
.craft p+p{margin-top:12px}
.places{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(14px,2vw,28px)}
.pl__img{aspect-ratio:1/1;overflow:hidden;background:var(--bg-soft)}
.pl__img img{width:100%;height:100%;object-fit:cover;transition:transform 1s cubic-bezier(.2,.7,.2,1)}
.pl:hover .pl__img img{transform:scale(1.05)}
.pl__num{font-family:var(--en);font-size:12px;letter-spacing:.22em;color:var(--red);font-weight:600;margin:16px 0 6px}
.pl h3{font-size:20px;margin-bottom:6px}
.pl p{font-size:14.5px}

/* visit */
.visit{background:var(--ink);color:#fff;padding:clamp(64px,8vw,110px) 0}
.visit .eyebrow{color:#fff;opacity:.85}
.visit__head{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:end;margin-bottom:clamp(32px,5vw,56px);padding-bottom:22px;border-bottom:1px solid rgba(255,255,255,.18)}
.visit__head p{color:rgba(255,255,255,.72);font-size:15px}
.vg{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(255,255,255,.12)}
.v{background:var(--ink);display:flex;flex-direction:column}
.v__img{aspect-ratio:4/3;overflow:hidden;background:#222}
.v__img img{width:100%;height:100%;object-fit:cover;transition:transform 1s cubic-bezier(.2,.7,.2,1)}
.v:hover .v__img img{transform:scale(1.04)}
.v__txt{padding:28px 26px 32px;display:flex;flex-direction:column;flex:1}
.v__txt h3{font-size:19px;margin-bottom:10px}
.v__txt p{color:rgba(255,255,255,.72);font-size:14.5px;flex:1}
.v__txt .link{align-self:flex-start;margin-top:22px}

/* next */
.next{padding:clamp(56px,7vw,96px) 0}
.next__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.next a{display:block;background:var(--bg);padding:32px 28px 36px;transition:background .25s}
.next a:hover{background:var(--bg-soft)}
.next .k{font-family:var(--en);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--red);font-weight:600;margin-bottom:16px}
.next h3{font-size:20px;margin-bottom:10px}
.next p{font-size:14.5px;margin-bottom:20px}

@media (max-width:1024px){.next__grid{grid-template-columns:1fr}}
@media (max-width:820px){
  .lede__grid,.craft__grid,.visit__head{grid-template-columns:1fr;gap:20px}
  .visit__head{align-items:start}
  .places,.vg{grid-template-columns:1fr}
  .wide{aspect-ratio:16/10}
}
@media (max-width:560px){.lede .stat{grid-template-columns:1fr 1fr}.phero{height:70vh}}
"""

def main():
    return f"""
<main id="top">

<section class="phero">
  <img data-src="the-hall-estate-bradford-on-avon-aerial.jpg" alt="The Hall Estate, Bradford-on-Avon, from the air" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow" {t('모든 것이 시작된 곳','Where it all began','すべてが始まった場所','一切开始的地方')}>모든 것이 시작된 곳</div>
    <h1 {t('홀 에스테이트','The Hall Estate','ホール・エステート','The Hall 庄园')}>홀 에스테이트</h1>
    <p {t('역사 깊은 도시 브래드퍼드 온 에이번에 자리한 알렉스 몰튼 박사의 가문 저택이자, 한 엔지니어링 유산이 태어난 곳.',
         'In the historic town of Bradford-on-Avon stands the ancestral home of Dr Alex Moulton, and the birthplace of a remarkable engineering legacy.',
         '歴史ある町ブラッドフォード・オン・エイヴォンに佇む、アレックス・モールトン博士の先祖代々の邸宅であり、一つのエンジニアリングの遺産が生まれた場所。',
         '坐落于历史名镇 Bradford-on-Avon 的亚历克斯·莫尔顿博士祖宅，也是一段非凡工程遗产的诞生地。')}>역사 깊은 도시 브래드퍼드 온 에이번에 자리한 알렉스 몰튼 박사의 가문 저택이자, 한 엔지니어링 유산이 태어난 곳.</p>
  </div>
</section>

<section class="lede">
  <div class="wrap lede__grid rv">
    <div>
      <div class="eyebrow">The Hall, Bradford-on-Avon</div>
      <h2 {t('집이자 연구소이자 공장','A home, a laboratory and a factory','家であり、研究所であり、工場','既是家，也是实验室与工厂')}>집이자 연구소이자 공장</h2>
    </div>
    <div>
      <p {t('홀은 오래전부터 혁신과 산업에 닿아 있었습니다. 몰튼 가문의 고무 제조와 엔지니어링을 통해, 첫 몰튼 자전거가 구상되기 훨씬 전부터 이 저택은 창의와 사업의 중심이었습니다. 알렉스에게 홀은 가족의 집 이상이었습니다. 아이디어가 시험되고, 다듬어지고, 실현되는 곳이었습니다.',
           'The Hall has long been tied to innovation and industry. Through the Moulton family\'s work in rubber manufacturing and engineering, the estate was a centre of creativity and enterprise well before the first Moulton bicycle was conceived. For Alex it was more than a family home: it was where ideas were tested, refined and realised.',
           'ホールは古くから革新と産業に結びついてきました。モールトン家のゴム製造とエンジニアリングを通じて、最初のモールトン自転車が構想されるずっと前から、この邸宅は創造と事業の中心でした。アレックスにとってホールは家族の家以上のものでした。アイデアが試され、磨かれ、実現される場所だったのです。',
           'The Hall 长久以来与创新和工业紧密相连。通过莫尔顿家族在橡胶制造与工程领域的事业，早在首款莫尔顿自行车构想之前，这座庄园就已是创造与事业的中心。对亚历克斯而言，它不只是家，更是想法被试验、打磨并实现的地方。')}>홀은 오래전부터 혁신과 산업에 닿아 있었습니다. 몰튼 가문의 고무 제조와 엔지니어링을 통해, 첫 몰튼 자전거가 구상되기 훨씬 전부터 이 저택은 창의와 사업의 중심이었습니다. 알렉스에게 홀은 가족의 집 이상이었습니다. 아이디어가 시험되고, 다듬어지고, 실현되는 곳이었습니다.</p>
      <p {t('60년 넘게 홀에서 살아온 알렉스는 이 저택과 역사, 그리고 혁신의 정신을 다음 세대를 위해 지키고자 홀을 알렉스 몰튼 자선 신탁에 맡겼습니다.',
           'After living at The Hall for more than sixty years, Alex placed it in the care of the Alex Moulton Charitable Trust, to protect the estate, its history and its spirit of innovation for future generations.',
           '60年以上ホールに住んだアレックスは、この邸宅とその歴史、革新の精神を次世代のために守るべく、ホールをアレックス・モールトン慈善信託に託しました。',
           '在 The Hall 生活六十余年后，亚历克斯将其托付给亚历克斯·莫尔顿慈善信托，以为后代守护这座庄园、它的历史与创新精神。')}>60년 넘게 홀에서 살아온 알렉스는 이 저택과 역사, 그리고 혁신의 정신을 다음 세대를 위해 지키고자 홀을 알렉스 몰튼 자선 신탁에 맡겼습니다.</p>
      <div class="stat">
        <div><b>1963</b><span {t('바이시클 웍스','Bicycle Works','バイシクル・ワークス','自行车工厂')}>바이시클 웍스</span></div>
        <div><b>Grade I</b><span {t('등록 문화재 저택','Listed Mansion','指定建造物','一级保护建筑')}>등록 문화재 저택</span></div>
        <div><b>30+</b><span {t('출고 국가','Countries Shipped','出荷国','出口国家')}>출고 국가</span></div>
      </div>
    </div>
  </div>
</section>

<div class="wide rv"><img data-src="the-hall-estate-bradford-on-avon-buildings.jpg" alt="The Hall Estate buildings" loading="lazy"></div>

<section class="craft">
  <div class="wrap">
    <div class="craft__grid rv">
      <div>
        <div class="eyebrow" {t('설계, 혁신, 장인정신','Design, Innovation & Craft','設計、革新、職人技','设计、创新与工艺')}>설계, 혁신, 장인정신</div>
        <h2 {t('몰튼 바이시클의 집','The home of Moulton Bicycles','モールトン・バイシクルの家','莫尔顿自行车之家')}>몰튼 바이시클의 집</h2>
      </div>
      <div>
        <p {t('몰튼 자전거는 처음부터 홀 가까이에서 설계되고 만들어졌습니다. 알렉스는 위대한 엔지니어링이란 개인적이고, 손으로 직접 하며, 장인정신에 뿌리내린 것이어야 한다고 믿었고, 그것이 자랄 수 있는 환경을 만들었습니다. 저택의 오래된 마구간과 작업장에서 숙련된 장인들이 그의 첫 설계를 만들었고, 1963년에 세상에 나온 그 자전거는 작은 바퀴와 풀 서스펜션, 정밀한 프레임으로 현대 사이클링을 바꿨습니다.',
             'Moulton bicycles have been designed and built close to The Hall from the start. Alex believed great engineering should be personal, hands-on and rooted in craftsmanship, and he created an environment where that could thrive. Skilled makers in the estate\'s historic stables and workshops built his original designs, which launched in 1963 and changed modern cycling with small wheels, full suspension and precision frames.',
             'モールトン自転車は当初からホールの近くで設計され、作られてきました。アレックスは、偉大なエンジニアリングとは個人的で、手を動かし、職人技に根ざしたものであるべきだと信じ、それが育つ環境を作りました。邸宅の歴史ある厩舎と工房で熟練の職人たちが彼の最初の設計を形にし、1963年に世に出たその自転車は、小さな車輪、フルサスペンション、精密なフレームで現代のサイクリングを変えました。',
             '莫尔顿自行车从一开始就在 The Hall 附近设计制造。亚历克斯相信伟大的工程应当是个人的、亲手的、植根于工艺的，并为此营造了适合它生长的环境。庄园历史悠久的马厩与工坊中，熟练的工匠打造出他最初的设计，这些于 1963 年面世的自行车以小轮径、全避震与精密车架改变了现代骑行。')}>몰튼 자전거는 처음부터 홀 가까이에서 설계되고 만들어졌습니다. 알렉스는 위대한 엔지니어링이란 개인적이고, 손으로 직접 하며, 장인정신에 뿌리내린 것이어야 한다고 믿었고, 그것이 자랄 수 있는 환경을 만들었습니다. 저택의 오래된 마구간과 작업장에서 숙련된 장인들이 그의 첫 설계를 만들었고, 1963년에 세상에 나온 그 자전거는 작은 바퀴와 풀 서스펜션, 정밀한 프레임으로 현대 사이클링을 바꿨습니다.</p>
        <p {t('그 전통은 지금도 이어집니다. 프레임은 여전히 옛 마구간에서 만들어진 뒤, 1963년의 바이시클 웍스로 옮겨져 도장과 조립, 최종 준비를 거칩니다. 완성된 자전거는 브래드퍼드 온 에이번에서 30개가 넘는 나라로 보내집니다. 홀은 브랜드의 정신적 고향이자, 지금도 살아 있는 제조의 현장입니다.',
             'The tradition continues. Frames are still made in the former stables, then moved to the original Bicycle Works for painting, assembly and final preparation. From Bradford-on-Avon, bikes now ship to more than 30 countries. The Hall is both the brand\'s spiritual home and an active part of its manufacturing.',
             'その伝統は今も続いています。フレームは今も旧厩舎で作られ、1963年のバイシクル・ワークスに運ばれて塗装、組立、最終準備を経ます。完成した自転車はブラッドフォード・オン・エイヴォンから30カ国以上に送られます。ホールはブランドの精神的な故郷であり、今も生きた製造の現場です。',
             '这一传统延续至今。车架仍在旧马厩中制作，再送往 1963 年的 Bicycle Works 进行喷涂、组装与最终准备。整车从 Bradford-on-Avon 发往 30 多个国家。The Hall 既是品牌的精神家园，也是至今仍在运转的制造现场。')}>그 전통은 지금도 이어집니다. 프레임은 여전히 옛 마구간에서 만들어진 뒤, 1963년의 바이시클 웍스로 옮겨져 도장과 조립, 최종 준비를 거칩니다. 완성된 자전거는 브래드퍼드 온 에이번에서 30개가 넘는 나라로 보내집니다. 홀은 브랜드의 정신적 고향이자, 지금도 살아 있는 제조의 현장입니다.</p>
      </div>
    </div>
    <div class="places rv">
      <div class="pl">
        <div class="pl__img"><img data-src="the-hall-bradford-on-avon.jpg" alt="The Hall" loading="lazy"></div>
        <div class="pl__num">01</div>
        <h3 {t('더 홀','The Hall','ザ・ホール','The Hall')}>더 홀</h3>
        <p {t('알렉스 몰튼 가문의 저택. 1등급 등록 문화재인 제임스 1세 시대 양식의 맨션.','Alex Moulton\'s ancestral home, a Grade I-listed Jacobean mansion.','アレックス・モールトン家の邸宅。グレードI指定のジャコビアン様式の館。','亚历克斯·莫尔顿的祖宅，一级保护的詹姆斯一世时期风格宅邸。')}>알렉스 몰튼 가문의 저택. 1등급 등록 문화재인 제임스 1세 시대 양식의 맨션.</p>
      </div>
      <div class="pl">
        <div class="pl__img"><img data-src="the-hall-stables-square-2.jpg" alt="The Stables" loading="lazy"></div>
        <div class="pl__num">02</div>
        <h3 {t('마구간','The Stables','厩舎','马厩')}>마구간</h3>
        <p {t('지금도 몰튼 프레임이 만들어지는 곳.','Where Moulton bicycle frames are still fabricated today.','今もモールトンのフレームが作られる場所。','至今仍在制作莫尔顿车架的地方。')}>지금도 몰튼 프레임이 만들어지는 곳.</p>
      </div>
      <div class="pl">
        <div class="pl__img"><img data-src="moulton-bicycle-works.jpg" alt="The Bicycle Works" loading="lazy"></div>
        <div class="pl__num">03</div>
        <h3 {t('바이시클 웍스','The Bicycle Works','バイシクル・ワークス','Bicycle Works')}>바이시클 웍스</h3>
        <p {t('1963년의 첫 자전거 공장. 오늘날 몰튼의 도장과 조립이 이루어지는 곳.','The original 1963 bicycle factory, today home to Moulton\'s painting and assembly.','1963年の最初の自転車工場。今日、モールトンの塗装と組立が行われる場所。','1963 年的第一座自行车工厂，如今是莫尔顿喷涂与组装之地。')}>1963년의 첫 자전거 공장. 오늘날 몰튼의 도장과 조립이 이루어지는 곳.</p>
      </div>
    </div>
  </div>
</section>

<section class="visit">
  <div class="wrap">
    <div class="visit__head rv">
      <div>
        <div class="eyebrow" {t('방문, 숙박, 경험','Visit, Stay, Experience','訪問、滞在、体験','到访、住宿、体验')}>방문, 숙박, 경험</div>
        <h2 {t('홀을 방문하세요','Visit The Hall','ホールを訪ねて','到访 The Hall')}>홀을 방문하세요</h2>
      </div>
      <p {t('홀은 박물관이 아니라 살아 있는 일터입니다. 7에이커의 역사적인 정원에서 가이드 투어, 프라이빗 숙박, 웨딩을 통해 방문객과 지역 사회를 맞이합니다. 수백 년 된 방들을 둘러보고, 고요한 정원을 걷고, 한 위대한 영국 엔지니어의 생애를 빚어낸 공기를 느낄 수 있습니다.',
           'The Hall is a living, working place rather than a museum. It welcomes visitors, guests and the local community through guided tours, private stays and weddings on seven acres of historic grounds. See centuries-old rooms, walk the peaceful gardens and feel the atmosphere that shaped a great British engineering career.',
           'ホールは博物館ではなく、生きた仕事の場です。7エーカーの歴史ある敷地で、ガイドツアー、プライベート宿泊、ウェディングを通じて訪問者や地域社会を迎えています。数百年の歴史を持つ部屋を巡り、静かな庭園を歩き、偉大な英国エンジニアの生涯を育んだ空気を感じることができます。',
           'The Hall 不是博物馆，而是一个活着的工作场所。它通过导览、私人住宿与婚礼，在七英亩的历史园林中迎接访客、宾客与当地社区。您可以参观数百年历史的房间，漫步宁静的花园，感受塑造了一位伟大英国工程师生涯的氛围。')}>홀은 박물관이 아니라 살아 있는 일터입니다. 7에이커의 역사적인 정원에서 가이드 투어, 프라이빗 숙박, 웨딩을 통해 방문객과 지역 사회를 맞이합니다. 수백 년 된 방들을 둘러보고, 고요한 정원을 걷고, 한 위대한 영국 엔지니어의 생애를 빚어낸 공기를 느낄 수 있습니다.</p>
    </div>
    <div class="vg rv">
      <div class="v">
        <div class="v__img"><img data-src="old-photo-the-hall-estate-bradford-on-avon.jpg" alt="The Hall, historic photograph" loading="lazy"></div>
        <div class="v__txt">
          <h3 {t('가이드 투어','Guided Tours','ガイドツアー','导览参观')}>가이드 투어</h3>
          <p {t('1등급 등록 문화재인 제임스 1세 시대 양식의 맨션과 그 역사를 둘러보는 투어.','A tour through the Grade I-listed Jacobean mansion and its history.','グレードI指定のジャコビアン様式の館とその歴史を巡るツアー。','参观一级保护的詹姆斯一世时期宅邸及其历史。')}>1등급 등록 문화재인 제임스 1세 시대 양식의 맨션과 그 역사를 둘러보는 투어.</p>
          <a class="link" href="{TRUST}" target="_blank" rel="noopener" {t('투어 안내','Tour Information','ツアー案内','参观信息')}>투어 안내</a>
        </div>
      </div>
      <div class="v">
        <div class="v__img"><img data-src="the-hall-estate-bedroom.jpg" alt="A bedroom at The Hall" loading="lazy"></div>
        <div class="v__txt">
          <h3 {t('홀에서의 숙박','Stay at The Hall','ホールでの滞在','住宿 The Hall')}>홀에서의 숙박</h3>
          <p {t('제임스 1세 시대의 멋과 현대의 편안함을 함께 갖춘 복원된 객실에서 알렉스의 가문 저택에 머물 수 있습니다.','Stay in Alex\'s ancestral home, in restored accommodation that combines Jacobean character with modern comforts.','ジャコビアン様式の趣と現代の快適さを兼ね備えた復元客室で、アレックスの先祖代々の邸宅に滞在できます。','在兼具詹姆斯一世时期风韵与现代舒适的修复客房中，入住亚历克斯的祖宅。')}>제임스 1세 시대의 멋과 현대의 편안함을 함께 갖춘 복원된 객실에서 알렉스의 가문 저택에 머물 수 있습니다.</p>
          <a class="link" href="{TRUST}" target="_blank" rel="noopener" {t('숙박 안내','Stay Information','宿泊案内','住宿信息')}>숙박 안내</a>
        </div>
      </div>
      <div class="v">
        <div class="v__img"><img data-src="alex-moulton-hall-estate-steps.jpg" alt="Alex Moulton on the steps of The Hall" loading="lazy"></div>
        <div class="v__txt">
          <h3 {t('알렉스 몰튼 자선 신탁','Alex Moulton Charitable Trust','アレックス・モールトン慈善信託','亚历克斯·莫尔顿慈善信托')}>알렉스 몰튼 자선 신탁</h3>
          <p {t('홀과 그 유산을 지키기 위해 알렉스 몰튼이 1977년에 세운 신탁. 오늘날 홀 에스테이트를 관리합니다.','Founded by Alex Moulton in 1977 to safeguard The Hall and its heritage, the Trust cares for the estate today.','ホールとその遺産を守るためにアレックス・モールトンが1977年に設立した信託。今日、ホール・エステートを管理しています。','由亚历克斯·莫尔顿于 1977 年创立，旨在守护 The Hall 及其遗产，如今负责庄园的管理。')}>홀과 그 유산을 지키기 위해 알렉스 몰튼이 1977년에 세운 신탁. 오늘날 홀 에스테이트를 관리합니다.</p>
          <a class="link" href="{TRUST}" target="_blank" rel="noopener">moultontrust.org</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="next">
  <div class="wrap">
    <div class="next__grid rv">
      <a href="/alex-moulton/">
        <div class="k">The Engineer</div>
        <h3 {t('알렉스 몰튼 박사','Dr Alex Moulton','アレックス・モールトン博士','亚历克斯·莫尔顿博士')}>알렉스 몰튼 박사</h3>
        <p {t('미니의 서스펜션과 몰튼 자전거를 만든 영국 엔지니어의 생애와 철학.','The life and philosophy of the British engineer behind the Mini suspension and the Moulton bicycle.','ミニのサスペンションとモールトン自転車を生んだ英国エンジニアの生涯と哲学。','创造 Mini 避震与莫尔顿自行车的英国工程师的生平与哲学。')}>미니의 서스펜션과 몰튼 자전거를 만든 영국 엔지니어의 생애와 철학.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
      <a href="/design/">
        <div class="k">Heritage</div>
        <h3 {t('디자인의 진화','Design Evolution','デザインの進化','设计演进')}>디자인의 진화</h3>
        <p {t('1962년 F-프레임에서 스페이스프레임까지, 몰튼 설계가 걸어온 길.','From the 1962 F-frame to the spaceframe: the path of Moulton design.','1962年のFフレームからスペースフレームまで、モールトン設計が歩んだ道。','从 1962 年的 F 型车架到空间车架：莫尔顿设计的演进之路。')}>1962년 F-프레임에서 스페이스프레임까지, 몰튼 설계가 걸어온 길.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
      <a href="/colors/">
        <div class="k">Hall Green</div>
        <h3 {t('컬러 & 피니시','Colours & Finishes','カラー＆仕上げ','颜色与涂装')}>컬러 & 피니시</h3>
        <p {t('홀 에스테이트의 색, 홀 그린을 포함한 몰튼의 서른 가지 컬러.','Thirty Moulton colours, including Hall Green, the colour of The Hall Estate.','ホール・エステートの色、ホールグリーンを含むモールトンの30色。','包括 The Hall 庄园之色霍尔绿在内的莫尔顿三十种颜色。')}>홀 에스테이트의 색, 홀 그린을 포함한 몰튼의 서른 가지 컬러.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
    </div>
  </div>
</section>

</main>
"""
