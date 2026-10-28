# -*- coding: utf-8 -*-
"""/design 페이지 본문 (디자인 역사, UK 'Design Evolution' 페이지 번역). build.py가 읽어 design/index.html 생성."""
from build import t

SLUG = 'design'
TITLE_KO = '몰튼 디자인의 진화 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'몰튼 디자인의 진화 | Moulton Bicycles Korea', en:'Design Evolution | Moulton Bicycles Korea', ja:'モールトン デザインの進化 | Moulton Bicycles Korea', zh:'莫尔顿设计演进 | Moulton Bicycles Korea'}"
DESCRIPTION = '1962년 F-프레임에서 스페이스프레임까지. 알렉스 몰튼 박사가 설계한 몰튼 자전거의 디자인 진화를 연대순으로 소개합니다.'
OG_TITLE = 'Design Evolution | Moulton Bicycles Korea'
OG_DESC = 'The evolution of the Moulton bicycle from F-frame to spaceframe, 1962 to 2000.'

CSS = """
/* ===== Design evolution page ===== */
.phero{position:relative;height:min(78vh,760px);min-height:460px;overflow:hidden;background:#161616}
.phero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%;filter:saturate(.85)}
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
.lede p+p{margin-top:16px}
.frames{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:clamp(40px,5vw,64px)}
.frame{position:relative;aspect-ratio:4/3;overflow:hidden;background:var(--bg-soft)}
.frame img{width:100%;height:100%;object-fit:cover;filter:grayscale(.15)}
.frame span{position:absolute;left:18px;bottom:16px;font-family:var(--en);font-size:11px;font-weight:600;letter-spacing:.24em;text-transform:uppercase;background:rgba(255,255,255,.9);color:var(--ink);padding:7px 12px}

/* timeline */
.decade{border-top:1px solid var(--ink);padding:clamp(40px,6vw,80px) 0 clamp(24px,4vw,48px)}
.decade__head{display:grid;grid-template-columns:1fr 2fr;gap:clamp(24px,5vw,96px);align-items:end;margin-bottom:clamp(32px,5vw,64px)}
.decade__head .yr{font-family:var(--en);font-weight:600;font-size:clamp(56px,9vw,140px);line-height:.9;letter-spacing:-.04em;color:var(--ink)}
.decade__head .yr small{font-size:.45em;font-weight:300;letter-spacing:-.02em;color:var(--ink-3)}
.decade__head h2{font-family:var(--en);font-weight:300;font-size:clamp(24px,2.8vw,38px);letter-spacing:-.02em;padding-bottom:8px}
html[lang="ko"] .decade__head h2,html[lang="ja"] .decade__head h2,html[lang="zh"] .decade__head h2{font-weight:300}
.ev{display:grid;grid-template-columns:1fr 2fr;gap:clamp(24px,5vw,96px);padding:clamp(28px,4vw,56px) 0;border-top:1px solid var(--line)}
.ev:first-of-type{border-top:0}
.ev__meta{position:sticky;top:96px;align-self:start}
.ev__meta .y{font-family:var(--en);font-weight:600;font-size:clamp(22px,2.4vw,32px);letter-spacing:-.02em;color:var(--red);line-height:1}
.ev__meta h3{font-size:clamp(20px,2vw,26px);margin-top:12px;letter-spacing:-.01em}
.ev__body{display:grid;grid-template-columns:1fr 1fr;gap:clamp(20px,3vw,40px);align-items:start}
.ev__body p{font-size:15.5px}
.ev__body p+p{margin-top:12px}
.ev__img{aspect-ratio:4/3;overflow:hidden;background:var(--bg-soft)}
.ev__img img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.ev:hover .ev__img img{transform:scale(1.04)}
.ev__img.wide{grid-column:1/-1;aspect-ratio:16/8}
.ev__img figcaption{font-family:var(--en);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);padding:10px 2px 0}

.next{background:var(--bg-soft);padding:clamp(64px,8vw,110px) 0}
.next__grid{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.next a{display:block;border-top:1px solid var(--ink);padding-top:20px}
.next a .k{font-family:var(--en);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-3);margin-bottom:10px}
.next a h3{margin-bottom:8px}
.next a p{font-size:15px}
.next a .link{display:inline-block;margin-top:16px}

@media (max-width:1024px){.ev__body{grid-template-columns:1fr}}
@media (max-width:820px){
  .lede__grid{grid-template-columns:1fr;gap:28px}
  .decade__head{grid-template-columns:1fr;gap:8px}
  .ev{grid-template-columns:1fr;gap:18px}
  .ev__meta{position:static}
  .next__grid{grid-template-columns:1fr}
}
@media (max-width:560px){.frames{grid-template-columns:1fr}.phero{height:70vh}}
"""

def ev(year, title, body, img, cap, wide=False):
    """연표 항목. body는 (ko,en,ja,zh) 문단 튜플의 리스트"""
    ps = ''.join(f'<p {t(*p)}>{p[0]}</p>' for p in body)
    fig = f'<figure class="ev__img{" wide" if wide else ""}"><img data-src="{img}" alt="" loading="lazy"><figcaption>{cap}</figcaption></figure>'
    return f"""
    <article class="ev rv">
      <div class="ev__meta"><div class="y">{year}</div><h3 {t(*title)}>{title[0]}</h3></div>
      <div class="ev__body"><div>{ps}</div>{fig}</div>
    </article>"""

def main():
    return f"""
<main id="top">

<section class="phero">
  <img data-src="moulton-f-frame-bikes-racing-coventry-cc-1963.jpg" alt="F-frame Moultons racing, Coventry CC, 1963" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow" {t('F-프레임에서 스페이스프레임까지','From F-frame to Spaceframe','Fフレームからスペースフレームへ','从 F 型车架到空间桁架')}>F-프레임에서 스페이스프레임까지</div>
    <h1 {t('디자인의 진화','Design Evolution','デザインの進化','设计演进')}>디자인의 진화</h1>
    <p {t('1962년 얼스코트에서 선보인 F-프레임부터 1977년 구상된 스페이스프레임, 그리고 1998년의 뉴 시리즈까지. 몰튼 자전거가 걸어온 설계의 궤적입니다.',
         'From the F-frame unveiled at Earls Court in 1962, through the spaceframe conceived in 1977, to the New Series of 1998: the design journey of the Moulton bicycle.',
         '1962年アールズコートで披露されたFフレームから、1977年に構想されたスペースフレーム、そして1998年のニューシリーズまで。モールトン自転車が歩んできた設計の軌跡です。',
         '从1962年在伯爵宫亮相的 F 型车架，到1977年构想的空间桁架，再到1998年的 New Series：这是莫尔顿自行车走过的设计之路。')}>1962년 얼스코트에서 선보인 F-프레임부터 1977년 구상된 스페이스프레임, 그리고 1998년의 뉴 시리즈까지. 몰튼 자전거가 걸어온 설계의 궤적입니다.</p>
  </div>
</section>

<section class="lede">
  <div class="wrap">
    <div class="lede__grid rv">
      <div>
        <div class="eyebrow">The Originator</div>
        <h2 {t('자동차에서 자전거로','From the car to the bicycle','自動車から自転車へ','从汽车到自行车')}>자동차에서 자전거로</h2>
      </div>
      <div>
        <p {t('1950년대 후반, 알렉스 몰튼 박사는 자동차 공학 경험과 미니(Mini) 개발 작업을 바탕으로 더 나은 자전거를 설계하기 시작했습니다. 그 결과가 1962년의 F-프레임 몰튼입니다.',
             'In the late 1950s Dr Alex Moulton set out to design an improved bicycle, drawing on his automotive engineering and his work on the Mini. The result was the F-frame Moulton of 1962.',
             '1950年代後半、アレックス・モールトン博士は自動車工学の経験とミニ（Mini）開発の仕事を基に、より優れた自転車の設計に着手しました。その成果が1962年のFフレーム・モールトンです。',
             '20世纪50年代末，亚历克斯·莫尔顿博士凭借其汽车工程经验以及参与 Mini 开发的工作，着手设计一款更好的自行车。成果便是1962年的 F 型车架莫尔顿。')}>1950년대 후반, 알렉스 몰튼 박사는 자동차 공학 경험과 미니(Mini) 개발 작업을 바탕으로 더 나은 자전거를 설계하기 시작했습니다. 그 결과가 1962년의 F-프레임 몰튼입니다.</p>
        <p {t('1980년대 초부터 그는 소량 고품질 생산으로 방향을 틀었고, 스페이스프레임 설계로 원래의 원칙을 다듬어 승차감과 조향, 범용성을 끌어올렸습니다.',
             'From the early 1980s he moved to small-scale, high-quality production, refining his original principles with the spaceframe design to improve comfort, handling and versatility.',
             '1980年代初頭からは少量高品質生産へと舵を切り、スペースフレーム設計によって当初の原則を磨き上げ、快適性、ハンドリング、汎用性を高めていきました。',
             '自80年代初起，他转向小批量高品质生产，以空间桁架设计提炼最初的原则，提升舒适性、操控与多用途性。')}>1980년대 초부터 그는 소량 고품질 생산으로 방향을 틀었고, 스페이스프레임 설계로 원래의 원칙을 다듬어 승차감과 조향, 범용성을 끌어올렸습니다.</p>
      </div>
    </div>
    <div class="frames rv">
      <figure class="frame"><img data-src="john-woodburn-training-f-frame-moulton-bike.jpg" alt="John Woodburn training on an F-frame Moulton" loading="lazy"><span>F Frame · 1962</span></figure>
      <figure class="frame"><img data-src="moulton-am-speed-riden-by-richard-grigsby-1991.jpg" alt="Richard Grigsby on a Moulton AM Speed, 1991" loading="lazy"><span>Spaceframe · 1983</span></figure>
    </div>
  </div>
</section>

<!-- ===== 1960s ===== -->
<section class="decade">
  <div class="wrap">
    <div class="decade__head rv">
      <div class="yr">1960<small>s</small></div>
      <h2 {t('혁신과 초기의 성공','Innovation and Early Success','革新と初期の成功','创新与早期成功')}>혁신과 초기의 성공</h2>
    </div>
    {ev('1962', ('출시','The Launch','発売','问世'), [
      ('몰튼 자전거는 1962년 얼스코트 사이클 쇼에서 처음 공개되어 그 시대를 상징하는 아이콘이 되었습니다. 알렉스 몰튼은 설계를 먼저 롤리(Raleigh)에 제안했지만 협상이 결렬되자 직접 몰튼 바이시클스(Moulton Bicycles Ltd)를 세우고 브래드퍼드온에이번에 공장을 지었습니다.',
       'The Moulton bicycle debuted at the 1962 Earls Court Cycle Show and became a fashionable icon of the decade. Alex Moulton first offered the design to Raleigh, but when talks failed he founded Moulton Bicycles Ltd and built a factory in Bradford-on-Avon.',
       'モールトン自転車は1962年のアールズコート・サイクルショーで初公開され、時代を象徴するアイコンとなりました。アレックス・モールトンはまずラレー（Raleigh）に設計を提案しましたが、交渉決裂を受けて自らモールトン・バイシクルズ社を設立し、ブラッドフォード・オン・エイヴォンに工場を建てました。',
       '莫尔顿自行车于1962年在伯爵宫自行车展上首次亮相，成为那个年代的时尚标志。亚历克斯·莫尔顿最初将设计提供给 Raleigh，谈判失败后，他自行创立 Moulton Bicycles Ltd，并在布拉德福德昂埃文建厂。'),
      ('수요가 공장 규모를 넘어서자 생산은 브리티시 모터 코퍼레이션(BMC)의 자회사 피셔 앤 러드로우로 옮겨졌고, 1년 만에 몰튼은 롤리에 이어 영국 2위의 프레임 제조사가 되었습니다.',
       'Demand soon outgrew the factory and production moved to Fisher & Ludlow, a British Motor Corporation subsidiary. Within a year Moulton was the country’s second-largest frame builder, behind only Raleigh.',
       '需要が工場の規模を超えると、生産はブリティッシュ・モーター・コーポレーション（BMC）の子会社フィッシャー＆ラドローへ移され、1年のうちにモールトンはラレーに次ぐ英国第2位のフレームメーカーとなりました。',
       '需求很快超过工厂产能，生产随之转移到英国汽车公司（BMC）的子公司 Fisher & Ludlow。一年之内，莫尔顿成为英国仅次于 Raleigh 的第二大车架制造商。'),
    ], 'moulton-bike-earls-court-display-stand-plinth-1962.jpg', 'Earls Court Cycle Show, 1962')}
    {ev('1962–67', ("'S' for Special","'S' for Special","'S' for Special","'S' for Special"), [
      ("몰튼 'S' 스토어웨이(MS5)는 1962년부터 1967년 무렵까지 극소량만 만들어진 고사양 모델입니다. 일반 모델은 커크비의 BMC 공장에서 나왔지만, S 라인은 저렴함보다 완성도를 원하는 이들을 위해 브래드퍼드온에이번 공방에서 따로 제작되었습니다. 접이식에 여행에 알맞은 설계, 그리고 크롬 마감 프레임으로 기억됩니다.",
       "The Moulton 'S' Stowaway (MS5) was a rare, high-specification model built in tiny numbers from about 1962 to 1967. Standard bikes came from the BMC plant at Kirkby, while the S range was made separately in the Bradford-on-Avon workshops for buyers who wanted refinement over low cost. Its folding, travel-friendly design is remembered for its chrome frame finish.",
       "モールトン'S'ストウアウェイ（MS5）は、1962年から1967年頃までごく少数のみ製造された高仕様モデルです。標準モデルはカークビーのBMC工場で作られましたが、Sシリーズは安さより完成度を求める人のために、ブラッドフォード・オン・エイヴォンの工房で別途製作されました。折りたたみ式で旅に適した設計、そしてクロームフレーム仕上げで知られています。",
       "莫尔顿 'S' Stowaway（MS5）是一款约在1962至1967年间极少量生产的高规格车型。标准车型出自柯克比的 BMC 工厂，而 S 系列则在布拉德福德昂埃文的工坊单独制作，面向追求精致而非低价的买家。其可折叠、适合旅行的设计以镀铬车架饰面而闻名。"),
    ], 'moulton-s-stowaway-bike-silver-chrome-with-lady-1960s.jpg', "Moulton 'S' Stowaway, 1960s")}
    {ev('1965', ('롤리의 대답','Raleigh’s answer to Moulton','ラレーの回答','Raleigh 的回应'), [
      ('1965년, 경쟁사들은 몰튼의 소경 외형을 따라 하기 시작했습니다. 몰튼의 핵심 기술은 특허로 보호되어 있었으므로 겉모습만 닮은 자전거들이었습니다. 저압 벌룬 타이어를 단 롤리 RSW16이 대표적인데, 성능이 형편없었고 그 인상은 지금까지도 미니벨로에 대한 편견으로 남아 있습니다.',
       'In 1965 rival makers began copying the small-wheel look of the Moulton. Since many Moulton features were patented, these were lookalikes only. The best known was the Raleigh RSW16 with its low-pressure balloon tyres; it performed poorly, and that impression still tarnishes small-wheeled bicycles today.',
       '1965年、競合メーカーはモールトンの小径スタイルを真似し始めました。モールトンの主要技術は特許で守られていたため、外見だけを似せた自転車でした。代表例が低圧バルーンタイヤを履いたラレーRSW16で、走行性能は乏しく、その印象は今もミニベロへの偏見として残っています。',
       '1965年，竞争对手开始模仿莫尔顿的小轮径外观。由于莫尔顿的许多特性受专利保护，这些车只是形似而已。最著名的是装有低压气球胎的 Raleigh RSW16，性能糟糕，而这一印象至今仍拖累着小轮径自行车的声誉。'),
    ], 'raleigh-rsw16-bike-red-white-tyres-1965.jpg', 'Raleigh RSW16, 1965')}
    {ev('1965–66', ('레이싱으로의 진화','Racing Evolution','レーシングへの進化','竞速演进'), [
      ('클럽 사이클리스트의 마음을 얻기 위해 알렉스 몰튼은 6단 디레일러를 갖춘 레이싱·투어링 모델 스피드식스(Speedsix)를 내놓았습니다. 그때까지의 몰튼은 내장 허브 기어를 썼기에, 스피드식스는 6단 디레일러를 단 최초의 양산 자전거로 소개되었습니다.',
       'To win over club cyclists Alex Moulton launched the Speedsix, a racing and touring bike with a six-speed derailleur. Earlier Moultons had used internal hub gears, so the Speedsix was presented as the first mass-produced bicycle with a six-speed derailleur.',
       'クラブサイクリストの心をつかむため、アレックス・モールトンは6段ディレイラーを備えたレーシング／ツーリングモデル、スピードシックス（Speedsix）を発売しました。それまでのモールトンは内装ハブギアを使っていたため、スピードシックスは6段ディレイラーを備えた初の量産自転車として紹介されました。',
       '为赢得俱乐部车手的青睐，亚历克斯·莫尔顿推出了配备六速拨链器的竞速兼旅行车型 Speedsix。此前的莫尔顿均采用内变速花鼓，因此 Speedsix 被称为首款配备六速拨链器的量产自行车。'),
      ('1966년에는 더블 체인링, 짧은 휠베이스, 레이놀즈 531 튜브셋을 갖춘 레이싱 모델 S 스피드(S Speed)가 뒤를 이었습니다.',
       'In 1966 the Moulton S Speed followed as a racing model with double chainrings, a short wheelbase and a Reynolds 531 tubeset.',
       '1966年には、ダブルチェーンリング、ショートホイールベース、レイノルズ531チューブセットを備えたレーシングモデル、Sスピードが続きました。',
       '1966年，采用双盘、短轴距和 Reynolds 531 管材的竞速车型 S Speed 接踵而至。'),
    ], 'moulton-speed-six-advertisement-circa-1965.jpg', 'Speedsix advertisement, c. 1965')}
    {ev('1967', ('몰튼 × 롤리','Moulton × Raleigh','モールトン × ラレー','莫尔顿 × Raleigh'), [
      ('1967년 롤리가 몰튼 사업을 인수했습니다. 알렉스 몰튼은 컨설턴트로 남았습니다. 롤리의 제조력과 몰튼의 설계를 결합한다는 구상이었지만, 두 회사의 동행은 순탄치 않았습니다.',
       'In 1967 Raleigh bought the Moulton business, with Alex Moulton staying on as a consultant. The promise was to combine Raleigh’s manufacturing strength with his design work, but the partnership proved difficult.',
       '1967年、ラレーがモールトン事業を買収しました。アレックス・モールトンはコンサルタントとして残りました。ラレーの製造力とモールトンの設計を組み合わせる構想でしたが、両社の歩みは平坦ではありませんでした。',
       '1967年，Raleigh 收购了莫尔顿业务，亚历克斯·莫尔顿留任顾问。初衷是将 Raleigh 的制造实力与他的设计相结合，但这段合作并不顺利。'),
    ], 'raleigh-moulton-collaboration-logo-circa-1969.jpg', 'Raleigh Moulton logo, c. 1969')}
  </div>
</section>

<!-- ===== 1970s ===== -->
<section class="decade">
  <div class="wrap">
    <div class="decade__head rv">
      <div class="yr">1970<small>s</small></div>
      <h2 {t('롤리, 그리고 실험의 시간','Raleigh & Experimentation','ラレー、そして実験の時代','Raleigh 与探索时期')}>롤리, 그리고 실험의 시간</h2>
    </div>
    {ev('1970–74', ('몰튼 MkIII','Moulton MkIII','モールトン MkIII','莫尔顿 MkIII'), [
      ('롤리 소유 아래에서도 몰튼은 설계를 계속 발전시켰습니다. 1970년의 MkIII는 삼각 구조의 리어 포크를 더한 개량형 F-프레임으로, 콜린 마틴의 영국-호주 횡단을 비롯한 프로토타입 주행에서 다듬어졌습니다. 롤리의 초퍼(Chopper)와 같은 시기에 출시되었고, 롤리와의 협업이 끝난 1974년까지 생산되었습니다.',
       'Under Raleigh ownership Moulton kept developing the design. The 1970 MkIII was a revised F-frame with a triangulated rear fork, shaped by prototypes including Colin Martin’s ride from England to Australia. It launched alongside Raleigh’s Chopper and was produced until 1974, when the Raleigh-Moulton collaboration ended.',
       'ラレー傘下でも、モールトンは設計を進化させ続けました。1970年のMkIIIは、トラス構造のリアフォークを加えた改良型Fフレームで、コリン・マーティンの英国〜オーストラリア走破などプロトタイプでの走行を経て磨かれました。ラレーのチョッパーと同時期に発売され、ラレーとの協業が終わる1974年まで生産されました。',
       '在 Raleigh 旗下，莫尔顿仍持续改进设计。1970年的 MkIII 是采用三角形后叉的改良版 F 型车架，经由包括 Colin Martin 从英国骑行至澳大利亚在内的原型车测试打磨而成。它与 Raleigh 的 Chopper 同期推出，一直生产至1974年 Raleigh 与莫尔顿合作结束。'),
    ], 'raleigh-moulton-smooth-one-MK3-bike-1970s.jpg', 'Raleigh Moulton MkIII, 1970s')}
    {ev('1975–79', ('다시 설계하다','An era of redesign','再設計の時代','重新设计'), [
      ('몰튼은 소량으로 손수 만드는 고품질 자전거로 방향을 바꿨습니다. 거의 완성 단계였던 Y-프레임은 한 친구가 무게를 지적한 뒤 보류되었습니다. 1977년, 알렉스 몰튼은 개방적이고 단단한 구조와 가벼움을 함께 갖춘 스페이스프레임을 구상했고, 이것이 몰튼의 새로운 뼈대가 되었습니다.',
       'Moulton shifted toward small-batch, hand-built bicycles of the highest quality. A near-finished Y-frame was shelved after a friend remarked on its weight. In 1977 Alex Moulton conceived the spaceframe: an open, stiff structure that was also light, and it became the new Moulton architecture.',
       'モールトンは少量生産の高品質ハンドビルド自転車へと方向を変えました。ほぼ完成していたYフレームは、友人が重さを指摘したことで棚上げに。1977年、アレックス・モールトンは開放的で剛性が高く、しかも軽いスペースフレームを構想し、これがモールトンの新しい骨格となりました。',
       '莫尔顿转向小批量、手工制作的高品质自行车。一款近乎完成的 Y 型车架在一位朋友指出其重量后被搁置。1977年，亚历克斯·莫尔顿构想出空间桁架：一种开放、刚性且轻量的结构，它成为莫尔顿新的架构。'),
    ], 'original-moulton-y-frame-green-with-front-rack-circa-1976.jpg', 'Original Y-frame prototype, c. 1976')}
  </div>
</section>

<!-- ===== 1980s ===== -->
<section class="decade">
  <div class="wrap">
    <div class="decade__head rv">
      <div class="yr">1980<small>s</small></div>
      <h2 {t('다음 세대','The Next Generation','次の世代','新一代')}>다음 세대</h2>
    </div>
    {ev('1983', ('스페이스프레임의 등장','The Spaceframe launches','スペースフレームの登場','空间桁架问世'), [
      ('스페이스프레임 설계는 1979년에 완성되었고, 원래의 공장은 새 설비를 갖췄습니다. 긴 시험을 거쳐 1983년 알렉스 몰튼(AM) 자전거가 출시되어 큰 호평을 받았습니다. 그중 AM7은 투어링 라이더들 사이에서 높은 평가를 얻었습니다.',
       'The spaceframe design was finalised by 1979 and the original factory re-equipped. After extensive testing the Alex Moulton (AM) bicycle launched in 1983 to strong acclaim. The AM7 became especially highly regarded among cycle tourers.',
       'スペースフレーム設計は1979年に完成し、元の工場には新たな設備が整えられました。長期のテストを経て、1983年にアレックス・モールトン（AM）自転車が発売され、高い評価を受けました。中でもAM7はツーリングライダーの間で高く評価されました。',
       '空间桁架设计于1979年定型，原工厂也重新配置了设备。经过广泛测试，Alex Moulton（AM）自行车于1983年推出，广受好评。其中 AM7 在旅行骑行者中尤受推崇。'),
    ], 'moulton-am-7-spaceframe-bike-1983.jpg', 'Moulton AM7, 1983')}
    {ev('1985–86', ('성능의 한계를 밀다','Pushing Performance','性能の限界を押し広げる','突破性能极限'), [
      ('1985년 몰튼은 Zzip 디자인의 투명 렉산 페어링을 공장 옵션으로 제공했고, 공기역학자 더그 밀리컨과 함께 완전 페어링 AM을 만들었습니다. 1986년 짐 글로버는 이 자전거로 플라잉 200m 구간에서 시속 51마일(약 82km/h)을 기록했습니다. 이 세계 기록은 지금도 깨지지 않았습니다.',
       'In 1985 Moulton offered a clear Lexan fairing by Zzip Designs as a factory option, and aerodynamicist Doug Milliken helped create a fully faired AM. In 1986 Jim Glover rode it to 51 mph over a flying 200 metres, a world speed record that still stands.',
       '1985年、モールトンはZzipデザイン製の透明レキサン・フェアリングを工場オプションとして提供し、空力学者ダグ・ミリケンと共にフルフェアリングAMを製作しました。1986年、ジム・グローバーはこの自転車でフライング200mを時速51マイル（約82km/h）で走破。この世界記録は今も破られていません。',
       '1985年，莫尔顿将 Zzip Designs 的透明 Lexan 整流罩作为工厂选配，并与空气动力学家 Doug Milliken 合作打造了全整流罩 AM。1986年，Jim Glover 骑着它在200米飞行计时中达到51英里/小时（约82公里/小时），这一世界纪录至今无人打破。'),
    ], 'moulton-am7-bike-with-zzip-fairing-circa-1985.jpg', 'AM7 with Zzip fairing, c. 1985')}
    {ev('1987–88', ('최초의 풀 서스펜션 MTB','Full-suspension MTB','初のフルサスMTB','首款全避震山地车'), [
      ('1987년, 25주년을 기념한 AM 주빌리(Jubilee)는 각도 조절이 가능한 위시본 스템을 처음 선보였습니다. 1988년에는 유선형 스페이스프레임에 20인치 휠을 단 AM-ATB가 나왔는데, 이것이 최초의 풀 서스펜션 마운틴바이크로 꼽힙니다. 마운틴바이크 붐과 함께 북미에서 인기를 얻었습니다.',
       'In 1987, for the 25th anniversary, the AM Jubilee introduced the Wishbone adjustable handlebar stem. In 1988 the AM-ATB, built on a streamlined spaceframe with 20-inch wheels, arrived and is credited as the first full-suspension mountain bike. It became popular in North America as mountain biking took off.',
       '1987年、25周年を記念したAMジュビリーは、角度調整可能なウィッシュボーン・ステムを初めて採用しました。1988年には、流線型スペースフレームに20インチホイールを組み合わせたAM-ATBが登場。これが初のフルサスペンション・マウンテンバイクとされています。マウンテンバイクブームと共に北米で人気を集めました。',
       '1987年，为纪念25周年推出的 AM Jubilee 首次采用可调节的 Wishbone 把立。1988年，基于流线型空间桁架、配备20英寸车轮的 AM-ATB 问世，被公认为首款全避震山地车。随着山地车运动兴起，它在北美广受欢迎。'),
    ], 'moulton-am-atb-bike-first-full-suspension-mtb-in-yellow-1998.jpg', 'Moulton AM-ATB')}
    {ev('1989', ('스피드가 필요했다','The need for SPEED','スピードへの渇望','对速度的渴望'), [
      ('AM 라이더 데이브 보그단이 레이스 어크로스 아메리카에서 성과를 거둔 뒤, 1989년 9월 몰튼 바이시클 클럽 연례 모임에서 AM-SPEED가 공개되었습니다. 분리되지 않는 일체형 레이싱 버전으로, 당시까지 양산된 몰튼 중 가장 가벼웠습니다.',
       'After AM rider Dave Bogdan’s success in the Race Across America, the AM-SPEED was launched in September 1989 at the annual Moulton Bicycle Club meet. This non-separable racing version was the lightest production Moulton yet.',
       'AMライダーのデイブ・ボグダンがレース・アクロス・アメリカで成果を挙げた後、1989年9月のモールトン・バイシクル・クラブ年次集会でAM-SPEEDが発表されました。分割できない一体型のレーシングバージョンで、当時までに量産されたモールトンの中で最軽量でした。',
       '在 AM 车手 Dave Bogdan 于横越美国赛（Race Across America）取得佳绩后，AM-SPEED 于1989年9月在莫尔顿自行车俱乐部年度聚会上发布。这款不可拆分的竞速版本是当时最轻的量产莫尔顿。'),
    ], 'moulton-am-speed-bike-white-with-red-bar-tape-1989.jpg', 'Moulton AM-SPEED, 1989')}
  </div>
</section>

<!-- ===== 1990s ===== -->
<section class="decade">
  <div class="wrap">
    <div class="decade__head rv">
      <div class="yr">1990<small>s</small></div>
      <h2 {t('더 많은 이들에게','Moultons for the masses','より多くの人へ','走向大众')}>더 많은 이들에게</h2>
    </div>
    {ev('1992', ('올 퍼포즈 바이크','The All-Purpose-Bike','オールパーパス・バイク','全能自行车'), [
      ('1992년, 스트랫퍼드어폰에이번의 패슐리 사이클스가 라이선스를 받아 몰튼 APB를 만들기 시작했습니다. AM-ATB에서 파생된 APB는 단순화한 프레임과 효율적인 제조 방식으로, 도시와 교외 어디서든 몰튼의 장점을 더 낮은 가격에 누릴 수 있게 했습니다.',
       'In 1992 Pashley Cycles of Stratford-upon-Avon began building the Moulton APB under licence. Derived from the AM-ATB, it used a simpler frame and more efficient manufacturing to bring Moulton’s advantages to a lower price point, for city, town or country riding.',
       '1992年、ストラトフォード・アポン・エイヴォンのパシュレイ・サイクルズがライセンスを受け、モールトンAPBの製造を始めました。AM-ATBから派生したAPBは、簡素化したフレームと効率的な製造方式により、街でも郊外でも、モールトンの利点をより手頃な価格で楽しめるようにしました。',
       '1992年，埃文河畔斯特拉特福的 Pashley Cycles 获得授权，开始生产莫尔顿 APB。它源自 AM-ATB，采用更简化的车架与更高效的制造方式，以更低的价格将莫尔顿的优势带到城市、城镇与乡间骑行。'),
    ], 'pashley-moulton-atb-yellow-with-rider-and-panniers-1994.jpg', 'Pashley Moulton APB, 1994')}
    {ev('1998', ('뉴 시리즈','A New Series','ニューシリーズ','New Series'), [
      ('AM 스페이스프레임이 나온 지 15년이 지난 1998년, 뉴 시리즈(NS)가 출시되었습니다. AM의 구조는 그대로 두되 플렉시터와 하이드로라스틱 요소를 쓴 새 서스펜션 시스템을 더하고 무게를 한층 줄여, 더 빠르고 더 편안한 자전거가 되었습니다.',
       'In 1998, fifteen years after the AM spaceframe, the New Series (NS) was launched. It kept the AM architecture but added a new suspension system using Flexitor and Hydrolastic elements, together with further weight savings, for a faster and more comfortable ride.',
       'AMスペースフレームの登場から15年後の1998年、ニューシリーズ（NS）が発売されました。AMの構造はそのままに、フレキシターとハイドロラスティック要素を用いた新しいサスペンションシステムを加え、さらに軽量化することで、より速く、より快適な自転車になりました。',
       '1998年，距 AM 空间桁架问世十五年后，New Series（NS）发布。它保留了 AM 的架构，同时加入采用 Flexitor 与 Hydrolastic 元件的全新避震系统，并进一步减重，骑行更快、更舒适。'),
    ], 'moulton-new-series-single-pylon-speed-triathlon-cyclist-2000.jpg', 'New Series Single Pylon Speed, 2000')}
    {ev('2000', ('브리지스톤 × 몰튼','Bridgestone × Moulton','ブリヂストン × モールトン','普利司通 × 莫尔顿'), [
      ('2000년 몰튼은 일본의 브리지스톤과 협업해 1965년의 시리즈 원을 빼닮은 알루미늄 F-프레임을 만들었습니다. 일본에서 분리형과 일체형 두 가지로 생산되었으며, 1960년대 롤리 남아프리카가 라이선스로 F-프레임을 만든 이후 영국 밖에서 제작된 유일한 모델입니다.',
       'In 2000 Moulton collaborated with the Japanese manufacturer Bridgestone on an aluminium F-frame closely resembling the 1965 Series One. Made in Japan in separable and fixed-frame versions, it is the only Moulton built outside the UK since Raleigh South Africa produced F-frames under licence in the 1960s.',
       '2000年、モールトンは日本のブリヂストンと協業し、1965年のシリーズワンに瓜二つのアルミ製Fフレームを製作しました。日本で分割式と一体式の2種類が生産され、1960年代にラレー南アフリカがライセンス生産したFフレーム以来、英国外で作られた唯一のモデルです。',
       '2000年，莫尔顿与日本制造商普利司通合作，打造了一款酷似1965年 Series One 的铝合金 F 型车架。它在日本生产，分为可拆分与固定车架两个版本，是自20世纪60年代 Raleigh 南非授权生产 F 型车架以来，唯一在英国以外制造的莫尔顿。'),
    ], 'moulton-bridgestone-f-frame-bike-size-view-2000.jpg', 'Bridgestone Moulton, 2000')}
  </div>
</section>

<section class="next">
  <div class="wrap">
    <div class="next__grid rv">
      <a href="/suspension/">
        <div class="k">Explore</div>
        <h3 {t('몰튼 서스펜션','Moulton Suspension','モールトンのサスペンション','莫尔顿避震系统')}>몰튼 서스펜션</h3>
        <p {t('하이드로라스틱, 모노스피어, 리딩 링크, 플렉시터. 네 가지 시스템의 원리.','Hydrolastic, Monosphere, Leading Link, Flexitor: how the four systems work.','ハイドロラスティック、モノスフィア、リーディングリンク、フレキシター。4つのシステムの原理。','Hydrolastic、Monosphere、Leading Link、Flexitor：四种系统的原理。')}>하이드로라스틱, 모노스피어, 리딩 링크, 플렉시터. 네 가지 시스템의 원리.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
      <a href="/#bikes">
        <div class="k">The Range</div>
        <h3 {t('현행 모델','Current models','現行モデル','现行车型')}>현행 모델</h3>
        <p {t('뉴 시리즈부터 TSR까지, 지금 만날 수 있는 몰튼 전 모델.','From the New Series to the TSR: every Moulton available today.','ニューシリーズからTSRまで、今出会えるモールトン全モデル。','从 New Series 到 TSR：如今可以选择的全部莫尔顿车型。')}>뉴 시리즈부터 TSR까지, 지금 만날 수 있는 몰튼 전 모델.</p>
        <span class="link" {t('전 모델 보기','View all bikes','全モデルを見る','查看全部车型')}>전 모델 보기</span>
      </a>
    </div>
  </div>
</section>

</main>
"""
