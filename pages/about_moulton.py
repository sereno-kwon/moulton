# -*- coding: utf-8 -*-
"""/about-moulton 페이지 본문 (UK 'The Moulton Bike' 페이지 번역). build.py가 읽어 about-moulton/index.html 생성.
   핵심 특징 5개(스페이스프레임·작은 바퀴·서스펜션·분리형 프레임·스틸)는 FEATURES 목록."""
from build import t

SLUG = 'about-moulton'
TITLE_KO = '몰튼 자전거 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'몰튼 자전거 | Moulton Bicycles Korea', en:'The Moulton Bike | Moulton Bicycles Korea', ja:'モールトンの自転車 | Moulton Bicycles Korea', zh:'莫尔顿自行车 | Moulton Bicycles Korea'}"
DESCRIPTION = '60년 넘게 다듬어 온 풀 서스펜션 미니벨로, 몰튼. 스페이스프레임, 작은 바퀴, 서스펜션, 분리형 프레임, 스틸. 몰튼 자전거의 설계와 엔지니어링.'
OG_TITLE = 'The Moulton Bike | Moulton Bicycles Korea'
OG_DESC = 'Spaceframe, small wheels, suspension, separability and steel. The design and engineering of the Moulton bicycle.'

CSS = """
/* ===== About the Moulton bike ===== */
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

/* quick spec */
.qspec{list-style:none;margin-top:36px;border-top:1px solid var(--ink)}
.qspec li{display:grid;grid-template-columns:170px 1fr;gap:16px;padding:14px 0;border-bottom:1px solid var(--line);font-size:15px}
.qspec li b{font-family:var(--en);font-weight:600;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);padding-top:4px}
.qspec li span{color:var(--ink)}

.wide{position:relative;aspect-ratio:21/9;overflow:hidden;background:var(--bg-soft)}
.wide img{width:100%;height:100%;object-fit:cover}

/* features */
.feats{padding:clamp(40px,6vw,80px) 0 0}
.feats__head{margin-bottom:clamp(28px,4vw,48px)}
.feats__head .eyebrow{margin-bottom:10px}
.unit{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:clamp(32px,6vw,96px);padding:clamp(40px,6vw,80px) 0;border-top:1px solid var(--line)}
.unit__img{position:relative;aspect-ratio:4/3;overflow:hidden;background:var(--bg-soft)}
.unit__img img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.unit:hover .unit__img img{transform:scale(1.04)}
.unit:nth-child(even) .unit__img{order:2}
.unit__txt .tag{font-family:var(--en);font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--red);font-weight:600;margin-bottom:12px}
.unit__txt h3{font-family:var(--en);font-size:clamp(26px,3vw,40px);margin-bottom:18px;letter-spacing:-.02em}
html[lang="ko"] .unit__txt h3{font-family:var(--ko);font-weight:500}
.unit__txt p+p{margin-top:12px}
.unit__txt .link{display:inline-block;margin-top:22px}

/* range */
.range{background:var(--bg-soft);padding:clamp(64px,8vw,110px) 0}
.range__grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,6vw,96px);align-items:center}
.range h2{margin-bottom:16px}
.range p+p{margin-top:12px}
.range .btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.range__img{position:relative;aspect-ratio:4/3;overflow:hidden;background:#fff}
.range__img img{width:100%;height:100%;object-fit:cover}

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
  .lede__grid,.range__grid{grid-template-columns:1fr;gap:28px}
  .unit{grid-template-columns:1fr;gap:22px}
  .unit:nth-child(even) .unit__img{order:0}
  .wide{aspect-ratio:16/10}
  .qspec li{grid-template-columns:120px 1fr}
}
@media (max-width:560px){.phero{height:70vh}}
"""

# ------------------------------------------------------------
# 핵심 특징: (번호, 영문 태그, 제목(ko,en,ja,zh), 이미지, 단락들 [(ko,en,ja,zh), ...], 링크(href, 텍스트(ko,en,ja,zh)) 또는 None)
# ------------------------------------------------------------
FEATURES = [
 ('01','Spaceframe',
  ('스페이스프레임','Spaceframe','スペースフレーム','空间车架'),
  'moulton-ns-safari-willow-green-frame-angle-close-up.jpg',
  [('몰튼의 프레임은 고성능 합금강으로 정밀하게 설계된 스페이스프레임입니다. 가는 튜브를 격자로 엮어 강성과 강도, 내구성을 얻습니다.',
    'The Moulton frame is a precision-engineered spaceframe of high-performance alloy steel, a lattice of tubes built for stiffness, strength and durability.',
    'モールトンのフレームは、高性能合金鋼で精密に設計されたスペースフレームです。細いチューブを格子状に組み、剛性、強度、耐久性を得ています。',
    '莫尔顿车架是以高性能合金钢精密打造的空间车架，由细管构成的格构结构带来刚性、强度与耐久性。'),
   ('프레임 강성은 성능에 큰 영향을 미칩니다. 옆으로 휘는 횡방향 변형은 라이더의 힘을 흡수해 효율을 떨어뜨리고, 단단한 프레임은 바퀴가 정확히 궤적을 따르게 해 로드 홀딩과 코너링 자신감을 높입니다.',
    'Frame stiffness strongly affects performance. Lateral flex absorbs rider energy and reduces efficiency, while a stiff frame keeps the wheels tracking precisely for better road holding and cornering confidence.',
    'フレーム剛性は性能に大きく影響します。横方向のたわみはライダーの力を吸収して効率を下げ、剛性の高いフレームはホイールを正確に軌道に沿わせ、ロードホールディングとコーナリングの自信を高めます。',
    '车架刚性对性能影响很大。侧向形变会吸收骑行者的能量、降低效率，而坚固的车架让车轮精确循迹，提升路感与过弯信心。'),
   ('소구경 스틸 튜브로 짠 격자 구조는 일반 프레임보다 더 단단하고 강합니다. 낮은 무게와 높은 횡강성, 강한 비틀림 강성이 결합해 경쾌하고 효율적인 주행감을 만듭니다.',
    'The lattice of small-diameter steel tubes is stiffer and stronger than a conventional frame. Low weight, high lateral stiffness and strong torsional rigidity combine for a lively, efficient ride.',
    '小径スチールチューブで組んだ格子構造は、一般的なフレームより硬く、強いものです。低重量、高い横剛性、強いねじり剛性が組み合わさり、軽快で効率的な走りを生みます。',
    '小直径钢管构成的格构结构比传统车架更坚固、更强韧。低重量、高侧向刚性与强扭转刚性相结合，带来轻快高效的骑行感。')],
  None),
 ('02','Small Wheels',
  ('작은 바퀴','Small Wheels','小径ホイール','小轮径'),
  'moulton-ns-safari-willow-green-front-wheel-close-up.jpg',
  [('작고 고압인 바퀴는 처음부터 몰튼 설계의 중심이었습니다. 작은 바퀴는 접이식이나 어린이용 자전거만을 위한 것이 아닙니다. 큰 바퀴에 비해 더 강하고, 더 단단하고, 더 가볍습니다.',
    'Small, high-pressure wheels have been central to the Moulton design from the start. They are not just for folding or children\'s bikes: compared with larger wheels they are stronger, stiffer and lighter.',
    '小さく高圧のホイールは、当初からモールトン設計の中心でした。小径ホイールは折りたたみ自転車や子供用自転車のためだけのものではありません。大径ホイールに比べ、より強く、より硬く、より軽いのです。',
    '小而高压的车轮从一开始就是莫尔顿设计的核心。小轮径不只属于折叠车或儿童车：与大轮相比，它更坚固、更刚硬、更轻。'),
   ('관성 모멘트가 작아 가속이 빠르고 핸들링이 민첩하며, 크기가 작아 공기 저항도 줄어듭니다.',
    'Their lower moment of inertia gives quicker acceleration and more responsive handling, and their smaller size reduces aerodynamic drag.',
    '慣性モーメントが小さいため加速が速く、ハンドリングは俊敏で、サイズが小さいため空気抵抗も減ります。',
    '转动惯量更小，加速更快、操控更灵敏；体积更小，风阻也更低。'),
   ('기어비는 일반 자전거와 같은 케이던스로 페달을 밟도록 맞춰져 있어, 더 빨리 돌릴 필요가 없습니다.',
    'Gearing is set so that pedalling cadence matches a conventional bike, so there is no need to pedal faster.',
    'ギア比は一般的な自転車と同じケイデンスでペダルを踏むよう設定されているため、速く回す必要はありません。',
    '齿比经过设定，踩踏节奏与普通自行车相同，无需更快地踩踏。')],
  None),
 ('03','Suspension',
  ('서스펜션','Suspension','サスペンション','避震系统'),
  'moulton-ns-safari-willow-green-front-and-rear-suspension-close-up.jpg',
  [('몰튼 서스펜션은 60년 넘게 발전해 왔습니다. 충격을 분리하면서 편안함과 핸들링, 효율을 함께 높이는 것이 목표입니다.',
    'Moulton suspension has been developed for over 60 years to isolate shocks while improving comfort, handling and efficiency.',
    'モールトンのサスペンションは60年以上にわたり発展してきました。衝撃を分離しながら、快適性、ハンドリング、効率を同時に高めることが目標です。',
    '莫尔顿避震系统已发展六十余年，目标是在隔离冲击的同时提升舒适、操控与效率。'),
   ('서스펜션 덕분에 작고 단단한 바퀴, 고압 타이어, 강성 높은 스페이스프레임이 온전히 함께 작동합니다. 주행은 눈에 띄게 부드러워지고 피로는 줄며, 접지력은 좋아지고 구름 저항은 낮아집니다.',
    'It allows the small rigid wheels, high-pressure tyres and stiff spaceframe to work fully together: a noticeably smoother ride, less fatigue, better traction and lower rolling resistance.',
    'サスペンションのおかげで、小さく硬いホイール、高圧タイヤ、剛性の高いスペースフレームが完全に連携します。走りは目に見えて滑らかになり、疲労は減り、グリップは向上し、転がり抵抗は下がります。',
    '有了避震，小而刚性的车轮、高压轮胎与坚固的空间车架才能完全协同：骑行明显更平顺，疲劳更少，抓地力更好，滚动阻力更低。'),
   ('몰튼의 네 가지 서스펜션 시스템은 정기 점검이 필요 없을 만큼 유지보수가 거의 들지 않습니다.',
    'Moulton\'s four suspension systems need little or no maintenance, with no routine servicing required.',
    'モールトンの4つのサスペンションシステムは、定期点検が不要なほどメンテナンスがほとんどかかりません。',
    '莫尔顿的四种避震系统几乎无需保养，不需要定期检修。')],
  ('/suspension/', ('서스펜션 자세히 보기','Explore Suspension','サスペンションを詳しく見る','了解避震系统'))),
 ('04','Separability',
  ('분리형 프레임','Separability','分割フレーム','可分离车架'),
  'moulton-ns-safari-willow-separable-frame-joint-close-up.jpg',
  [('모든 몰튼은 일반 자전거보다 작고, 대부분의 모델은 프레임을 분리해 자동차, 기차, 비행기로 옮길 수 있습니다.',
    'All Moulton bikes are more compact than conventional bikes, and most models have separable frames for transport by road, rail or air.',
    'すべてのモールトンは一般的な自転車よりコンパクトで、ほとんどのモデルはフレームを分割して車、鉄道、飛行機で運ぶことができます。',
    '所有莫尔顿都比普通自行车更紧凑，大多数车型的车架可分离，便于汽车、铁路或航空运输。'),
   ('분리 구조가 더하는 무게는 아주 적고, 강성이나 편안함, 승차감은 줄어들지 않습니다. 전용으로 설계된 변속·브레이크 케이블 커넥터는 재조정 없이 깔끔하게 분리됩니다.',
    'Separation adds only a small amount of weight and does not reduce stiffness, comfort or ride quality. Purpose-designed gear and brake cable connectors disconnect cleanly without readjustment.',
    '分割構造が加える重量はごくわずかで、剛性や快適性、乗り心地は損なわれません。専用設計の変速・ブレーキケーブルコネクターは、再調整なしできれいに分離できます。',
    '分离结构增加的重量极少，且不会降低刚性、舒适与骑行品质。专门设计的变速与刹车线连接器可干净地断开，无需重新调整。'),
   ('분리한 두 부분은 승용차 트렁크나 여행용 케이스에 들어갑니다. 일부 모델은 다섯 부분으로 나뉩니다.',
    'The two halves fit in a car boot or travel case. Some models split into five components.',
    '分割した二つの部分は、乗用車のトランクや旅行用ケースに収まります。一部のモデルは5つのパーツに分かれます。',
    '分离后的两部分可放入轿车后备箱或旅行箱。部分车型可拆成五个部件。')],
  None),
 ('05','Steel',
  ('스틸','Steel','スチール','钢材'),
  'moulton-speed-polished-stainless-centre-frame-section-close-up.jpg',
  [('프레임에는 콜럼버스, 레이놀즈, 카이세이의 프리미엄 스틸 튜브셋을 모델별로 골라 씁니다. 폴리시드 스테인리스 프레임에는 항공우주 등급 스테인리스강을 사용해 강도와 내식성, 내구성을 확보합니다.',
    'Frames use premium steel tube sets from Columbus, Reynolds and Kaisei, chosen for each model. Polished stainless frames use aerospace-grade stainless steel for strength, corrosion resistance and durability.',
    'フレームには、コロンバス、レイノルズ、カイセイのプレミアムスチールチューブセットをモデルごとに選んで使用します。ポリッシュドステンレスフレームには航空宇宙グレードのステンレス鋼を使い、強度、耐食性、耐久性を確保しています。',
    '车架根据车型选用 Columbus、Reynolds 与 Kaisei 的高级钢管组。抛光不锈钢车架采用航空级不锈钢，兼具强度、耐腐蚀与耐久性。'),
   ('현대의 고장력강은 알루미늄이나 티타늄 합금과 같거나 더 나은 강도 대 중량비를 냅니다. 스틸은 피로 하중에 강하고, 작은 손상을 견디며, 수리할 수 있습니다.',
    'Modern high-tensile steel can match or exceed the strength-to-weight ratio of aluminium or titanium alloys. Steel handles fatigue loading well, tolerates minor damage and can be repaired.',
    '現代の高張力鋼は、アルミニウムやチタン合金と同等かそれ以上の強度対重量比を実現します。スチールは疲労荷重に強く、小さな損傷に耐え、修理が可能です。',
    '现代高强度钢的强度重量比可媲美甚至超越铝合金或钛合金。钢材耐疲劳载荷，能承受轻微损伤，且可修复。'),
   ('스틸 고유의 진동 감쇠는 많은 라이더가 선호하는 편안한 승차감을 만듭니다.',
    'Its natural vibration damping gives a comfortable ride that many riders prefer.',
    'スチール固有の振動減衰は、多くのライダーが好む快適な乗り心地を生みます。',
    '钢材天然的减振特性带来许多骑行者偏爱的舒适骑行感。')],
  None),
]

def unit(num, tag, title, img, paras, link):
    body = ''.join(f'<p {t(*p)}>{p[0]}</p>' for p in paras)
    lk = ''
    if link:
        href, txt = link
        lk = f'<a class="link" href="{href}" {t(*txt)}>{txt[0]}</a>'
    return f"""
    <article class="unit rv">
      <div class="unit__img"><img data-src="{img}" alt="Moulton {tag}" loading="lazy"></div>
      <div class="unit__txt">
        <div class="tag">{num} · {tag}</div>
        <h3 {t(*title)}>{title[0]}</h3>
        {body}
        {lk}
      </div>
    </article>"""

def main():
    feats = ''.join(unit(*f) for f in FEATURES)
    return f"""
<main id="top">

<section class="phero">
  <img data-src="moulton-ns-safari-willow-green-side-view-landscape.jpg" alt="Moulton NS Safari" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow" {t('설계와 엔지니어링','Design & Engineering','設計とエンジニアリング','设计与工程')}>설계와 엔지니어링</div>
    <h1 {t('몰튼 자전거','The Moulton Bike','モールトンの自転車','莫尔顿自行车')}>몰튼 자전거</h1>
    <p {t('풀 서스펜션 미니벨로의 정점. 60년 넘게 다듬어 왔고, 지금도 영국에서 한 대 한 대 손으로 만듭니다. 속도, 효율, 다재다능함, 그리고 편안함.',
         'The ultimate full-suspension, small-wheeled bicycle. Refined for over 60 years and still hand-built in England. Speed, efficiency, versatility and comfort.',
         'フルサスペンション小径車の頂点。60年以上にわたり磨き上げられ、今も英国で一台一台手作りされています。速さ、効率、多用途性、そして快適さ。',
         '全避震小轮径自行车的巅峰。历经六十余年打磨，至今仍在英国逐台手工制造。速度、效率、多功能与舒适。')}>풀 서스펜션 미니벨로의 정점. 60년 넘게 다듬어 왔고, 지금도 영국에서 한 대 한 대 손으로 만듭니다. 속도, 효율, 다재다능함, 그리고 편안함.</p>
  </div>
</section>

<section class="lede">
  <div class="wrap lede__grid rv">
    <div>
      <div class="eyebrow">The Moulton Bike</div>
      <h2 {t('모든 요소에 이유가 있는 자전거','A bicycle where every element has a reason','すべての要素に理由がある自転車','每个元素都有其道理的自行车')}>모든 요소에 이유가 있는 자전거</h2>
    </div>
    <div>
      <p {t('몰튼은 작은 바퀴와 서스펜션, 스페이스프레임이라는 세 가지 아이디어를 하나로 엮은 자전거입니다. 각각은 따로 떼어 놓으면 낯설어 보이지만, 함께 작동할 때 일반 자전거가 닿지 못하는 속도와 편안함을 만들어 냅니다.',
           'A Moulton brings together three ideas: small wheels, suspension and the spaceframe. Each may look unusual on its own, but working together they deliver a speed and comfort a conventional bicycle cannot reach.',
           'モールトンは、小径ホイール、サスペンション、スペースフレームという三つのアイデアを一つに編み上げた自転車です。それぞれは単独では見慣れないかもしれませんが、共に働くとき、一般的な自転車には届かない速さと快適さを生み出します。',
           '莫尔顿将小轮径、避震与空间车架三个理念融为一体。单独看每一项或许陌生，但协同运作时，便带来普通自行车无法企及的速度与舒适。')}>몰튼은 작은 바퀴와 서스펜션, 스페이스프레임이라는 세 가지 아이디어를 하나로 엮은 자전거입니다. 각각은 따로 떼어 놓으면 낯설어 보이지만, 함께 작동할 때 일반 자전거가 닿지 못하는 속도와 편안함을 만들어 냅니다.</p>
      <ul class="qspec">
        <li><b {t('리어 서스펜션','Rear suspension','リアサスペンション','后避震')}>리어 서스펜션</b><span {t('하이드로라스틱 또는 모노스피어','Hydrolastic or Monosphere','ハイドロラスティックまたはモノスフィア','Hydrolastic 或 Monosphere')}>하이드로라스틱 또는 모노스피어</span></li>
        <li><b {t('프론트 서스펜션','Front suspension','フロントサスペンション','前避震')}>프론트 서스펜션</b><span {t('플렉시터 또는 리딩 링크','Flexitor or Leading Link','フレキシターまたはリーディングリンク','Flexitor 或 Leading Link')}>플렉시터 또는 리딩 링크</span></li>
        <li><b {t('프레임 분리','Frame separation','フレーム分割','车架分离')}>프레임 분리</b><span {t('고정형, 또는 분리·수납형','Fixed, or separable and stowable','固定式、または分割・収納式','固定式，或可分离收纳式')}>고정형, 또는 분리·수납형</span></li>
        <li><b {t('휠','Wheels','ホイール','车轮')}>휠</b><span {t('17인치 또는 20인치 소구경 휠, 고압 타이어','Small 17" or 20" wheels with high-pressure tyres','17インチまたは20インチの小径ホイール、高圧タイヤ','17 或 20 英寸小轮径，高压轮胎')}>17인치 또는 20인치 소구경 휠, 고압 타이어</span></li>
        <li><b {t('프레임 설계','Frame design','フレーム設計','车架设计')}>프레임 설계</b><span {t('낮은 무게와 높은 횡강성의 고도로 설계된 스틸 프레임','Highly engineered steel frame with low weight and high lateral stiffness','低重量と高い横剛性を備えた高度に設計されたスチールフレーム','低重量、高侧向刚性的精密设计钢制车架')}>낮은 무게와 높은 횡강성의 고도로 설계된 스틸 프레임</span></li>
        <li><b {t('프레임 사이즈','Frame size','フレームサイズ','车架尺寸')}>프레임 사이즈</b><span {t('단일 사이즈, 타고 내리기 쉬운 낮은 스텝스루 프레임','One size, with a low step-through frame for easy mounting','ワンサイズ、乗り降りしやすい低いステップスルーフレーム','单一尺寸，便于上下车的低跨点车架')}>단일 사이즈, 타고 내리기 쉬운 낮은 스텝스루 프레임</span></li>
      </ul>
    </div>
  </div>
</section>

<div class="wide rv"><img data-src="moulton-ns-safari-bike-side-grey-background-with-racks-bags.jpg" alt="Moulton NS Safari with racks and bags" loading="lazy"></div>

<section class="feats">
  <div class="wrap">
    <div class="feats__head rv">
      <div class="eyebrow" {t('핵심 특징','Key Features','主な特徴','核心特点')}>핵심 특징</div>
      <h2 {t('몰튼을 몰튼으로 만드는 다섯 가지','Five things that make a Moulton a Moulton','モールトンをモールトンたらしめる五つのこと','让莫尔顿成为莫尔顿的五件事')}>몰튼을 몰튼으로 만드는 다섯 가지</h2>
    </div>
{feats}
  </div>
</section>

<section class="range">
  <div class="wrap range__grid rv">
    <div>
      <div class="eyebrow" {t('라인업','The Range','ラインナップ','产品系列')}>라인업</div>
      <h2 {t('정제된 퍼포먼스부터 일상의 자전거까지','From refined performance to everyday bikes','洗練されたパフォーマンスから日常の自転車まで','从精炼的性能车到日常用车')}>정제된 퍼포먼스부터 일상의 자전거까지</h2>
      <p {t('몰튼의 라인업은 정제된 퍼포먼스 모델에서 도시와 시골, 그 너머를 위한 다재다능한 일상 자전거까지 이어집니다.',
           'The range runs from refined performance models to versatile everyday bikes for town, country and beyond.',
           'モールトンのラインナップは、洗練されたパフォーマンスモデルから、街と田舎、その先のための多用途な日常自転車まで続きます。',
           '莫尔顿的产品线从精炼的性能车型，延伸到适合城市、乡村及更远之地的多功能日常自行车。')}>몰튼의 라인업은 정제된 퍼포먼스 모델에서 도시와 시골, 그 너머를 위한 다재다능한 일상 자전거까지 이어집니다.</p>
      <p {t('모든 자전거는 작은 바퀴와 서스펜션이라는 설계 철학을 중심으로 영국에서 설계되고 손으로 만들어집니다.',
           'Every bike is designed and hand-built in Britain around the small-wheel, suspended design philosophy.',
           'すべての自転車は、小径ホイールとサスペンションという設計思想を中心に、英国で設計され手作りされています。',
           '每一台车都围绕小轮径与避震的设计哲学，在英国设计并手工制造。')}>모든 자전거는 작은 바퀴와 서스펜션이라는 설계 철학을 중심으로 영국에서 설계되고 손으로 만들어집니다.</p>
      <div class="btns">
        <a class="btn" href="/#bikes" {t('전 모델 보기','View all bikes','全モデルを見る','查看全部车型')}>전 모델 보기</a>
        <a class="btn red" href="https://rubiworkshop.com/models" target="_blank" rel="noopener" {t('상담 신청','Consulting','ご相談はこちら','预约咨询')}>상담 신청</a>
      </div>
    </div>
    <div class="range__img"><img data-src="moulton-ns-safari-willow-green.jpg" alt="Moulton NS Safari" loading="lazy"></div>
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
      <a href="/design/">
        <div class="k">Heritage</div>
        <h3 {t('디자인의 진화','Design Evolution','デザインの進化','设计演进')}>디자인의 진화</h3>
        <p {t('1962년 F-프레임에서 스페이스프레임까지, 알렉스 몰튼 박사의 설계가 걸어온 길.','From the 1962 F-frame to the spaceframe: the path of Dr Alex Moulton’s design.','1962年のFフレームからスペースフレームまで、アレックス・モールトン博士の設計が歩んだ道。','从 1962 年的 F 型车架到空间车架：亚历克斯·莫尔顿博士设计的演进之路。')}>1962년 F-프레임에서 스페이스프레임까지, 알렉스 몰튼 박사의 설계가 걸어온 길.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
      <a href="/sizing/">
        <div class="k">Fit</div>
        <h3 {t('사이징 가이드','Sizing Guide','サイジングガイド','尺寸指南')}>사이징 가이드</h3>
        <p {t('하나의 프레임 사이즈가 신장 160~193cm에 맞는 이유, 모델별 인사이드 레그 범위.','Why one frame size fits riders from 160 to 193 cm, and the inside leg range for each model.','一つのフレームサイズが身長160〜193cmに合う理由と、モデル別の股下範囲。','为何一种车架尺寸适合身高 160–193 cm 的骑行者，以及各车型的内腿长范围。')}>하나의 프레임 사이즈가 신장 160~193cm에 맞는 이유, 모델별 인사이드 레그 범위.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
    </div>
  </div>
</section>

</main>
"""
