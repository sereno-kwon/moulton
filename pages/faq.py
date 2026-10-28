# -*- coding: utf-8 -*-
"""/faq 페이지 본문 (UK 'Frequently Asked Questions' 페이지를 한국 판매 구조에 맞춰 재구성). build.py가 읽어 faq/index.html 생성.
   질문 추가·수정은 아래 FAQ 목록. 영국 전용 항목(영국 배송·VAT·반품·Cycle to Work·쿠키)은 제외하고
   구매·납기·보증 관련 답변은 한국 공식 디스트리뷰터 루비컴퍼니 기준으로 다시 씀."""
from build import t

SLUG = 'faq'
TITLE_KO = '몰튼 자주 묻는 질문 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'몰튼 자주 묻는 질문 | Moulton Bicycles Korea', en:'FAQ | Moulton Bicycles Korea', ja:'モールトン よくあるご質問 | Moulton Bicycles Korea', zh:'莫尔顿常见问题 | Moulton Bicycles Korea'}"
DESCRIPTION = '몰튼 구매, 사이즈, 납기, 커스텀 빌드, 승차감, 분리형 프레임, 보증과 스페어 파츠까지. 몰튼 코리아에 자주 묻는 질문과 답변.'
OG_TITLE = 'FAQ | Moulton Bicycles Korea'
OG_DESC = 'Answers to the questions we are asked most often about Moulton bicycles in Korea.'

CSS = """
/* ===== FAQ page ===== */
.eyebrow{font-size:14px;letter-spacing:.18em;margin-bottom:16px}
.phero{position:relative;height:min(70vh,640px);min-height:420px;overflow:hidden;background:#161616}
.phero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.phero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.7) 0%,rgba(0,0,0,.35) 45%,rgba(0,0,0,.05) 75%),linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.5) 100%)}
.phero__txt{position:absolute;left:0;right:0;bottom:clamp(40px,8vh,80px);z-index:2;color:#fff}
.phero__txt .eyebrow{color:#fff;opacity:.85;font-size:15px;margin-bottom:22px}
.phero__txt h1{font-size:clamp(36px,6vw,84px);line-height:1;letter-spacing:-.03em;text-shadow:0 2px 24px rgba(0,0,0,.35)}
html[lang="ko"] .phero__txt h1{font-family:var(--ko);font-weight:500;word-break:keep-all}
html[lang="ja"] .phero__txt h1,html[lang="zh"] .phero__txt h1{letter-spacing:0;line-height:1.1}
.phero__txt p{color:rgba(255,255,255,.85);margin-top:20px;max-width:52ch}

/* category nav */
.cats{position:sticky;top:72px;z-index:20;background:rgba(255,255,255,.92);backdrop-filter:saturate(180%) blur(12px);-webkit-backdrop-filter:saturate(180%) blur(12px);border-bottom:1px solid var(--line)}
.cats__in{display:flex;gap:0;overflow-x:auto;scrollbar-width:none}
.cats__in::-webkit-scrollbar{display:none}
.cats a{flex:0 0 auto;font-family:var(--en);font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;padding:18px 22px 16px;border-bottom:2px solid transparent;color:var(--ink-3);white-space:nowrap;transition:color .2s,border-color .2s}
.cats a:first-child{padding-left:0}
.cats a:hover,.cats a.on{color:var(--ink);border-color:var(--red)}
html[lang="ko"] .cats a{font-family:var(--ko);font-weight:500;letter-spacing:.04em;text-transform:none;font-size:13.5px}
html[lang="ja"] .cats a,html[lang="zh"] .cats a{letter-spacing:.04em;text-transform:none;font-size:13.5px}

/* groups */
.grp{padding:clamp(56px,7vw,96px) 0 0}
.grp:last-of-type{padding-bottom:clamp(56px,7vw,96px)}
.grp__grid{display:grid;grid-template-columns:1fr 2fr;gap:clamp(24px,5vw,96px);align-items:start}
.grp__head{position:sticky;top:132px}
.grp__head .num{font-family:var(--en);font-size:13px;letter-spacing:.22em;color:var(--red);margin-bottom:14px}
.grp__head h2{font-size:clamp(26px,3vw,40px)}
.grp__head p{font-size:14.5px;margin-top:14px;color:var(--ink-3)}
.qa{border-top:1px solid var(--ink)}
.qa details{border-bottom:1px solid var(--line)}
.qa summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:1fr 28px;gap:20px;align-items:start;padding:22px 0;font-size:clamp(16px,1.25vw,19px);font-weight:500;line-height:1.45;letter-spacing:-.01em}
html[lang="en"] .qa summary{font-family:var(--en);font-weight:600}
.qa summary::-webkit-details-marker{display:none}
.qa summary:hover{color:var(--red)}
.qa summary .ic{position:relative;width:28px;height:28px;border:1px solid var(--line);border-radius:50%;margin-top:1px;transition:background .25s,border-color .25s}
.qa summary .ic:before,.qa summary .ic:after{content:"";position:absolute;left:50%;top:50%;background:currentColor;transition:transform .3s}
.qa summary .ic:before{width:11px;height:1px;transform:translate(-50%,-50%)}
.qa summary .ic:after{width:1px;height:11px;transform:translate(-50%,-50%)}
.qa details[open] summary .ic{background:var(--ink);border-color:var(--ink);color:#fff}
.qa details[open] summary .ic:after{transform:translate(-50%,-50%) rotate(90deg)}
.qa .a{padding:0 48px 26px 0;animation:fade .35s ease}
.qa .a p{font-size:15.5px}
.qa .a p+p{margin-top:10px}
.qa .a a{border-bottom:1px solid var(--line);transition:border-color .2s}
.qa .a a:hover{border-color:var(--ink)}
@keyframes fade{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}

/* cta */
.cta{background:var(--ink);color:#fff;padding:clamp(64px,8vw,110px) 0;text-align:center}
.cta .eyebrow{color:#fff;opacity:.85}
.cta h2{margin-bottom:16px}
.cta p{color:rgba(255,255,255,.75);margin:0 auto 32px}
.cta .btn{margin:6px}

@media (max-width:820px){
  .grp__grid{grid-template-columns:1fr;gap:20px}
  .grp__head{position:static}
  .cats{top:72px}
  .qa .a{padding-right:0}
}
@media (max-width:560px){.phero{height:60vh}}
"""

# ------------------------------------------------------------
# FAQ: (카테고리 id, 번호, 제목(ko,en,ja,zh), 소개(ko,en,ja,zh), [ (질문(ko,en,ja,zh), 답변 단락들 [(ko,en,ja,zh), ...]) ... ])
# ------------------------------------------------------------
LINK_DEALER = '<a href="/authorized-dealer/">{}</a>'
LINK_SIZING = '<a href="/sizing/">{}</a>'
LINK_COLORS = '<a href="/colors/">{}</a>'
LINK_SUSP   = '<a href="/suspension/">{}</a>'
LINK_RW     = '<a href="https://rubiworkshop.com/models" target="_blank" rel="noopener">{}</a>'
LINK_FRAME  = '<a href="https://www.moultonbicycles.co.uk/pages/moulton-framesets" target="_blank" rel="noopener">{}</a>'
LINK_CLUB   = '<a href="https://www.moultonbuzz.com/preservation/" target="_blank" rel="noopener">{}</a>'

FAQ = [
 ('buy', '01',
  ('구매 안내','Buying a Moulton','購入について','购买指南'),
  ('어디서, 어떻게 살 수 있는지. 사이즈와 납기, 커스텀 빌드, 시승까지.','Where and how to buy, sizing, lead times, custom builds and test rides.','どこで、どのように購入できるか。サイズ、納期、カスタムビルド、試乗まで。','在哪里、如何购买，以及尺寸、交期、定制与试骑。'),
  [
   (('한국에서 몰튼은 어디서 살 수 있나요?','Where can I buy a Moulton in Korea?','韓国ではどこでモールトンを購入できますか？','在韩国哪里可以购买莫尔顿？'),
    [('몰튼 바이시클의 한국 공식 디스트리뷰터는 루비컴퍼니입니다. 서울 반포의 공식 쇼룸 루비워크샵과 전국의 몰튼 공식 딜러에서 구매하실 수 있습니다. 가까운 매장은 '+LINK_DEALER.format('공식 딜러 페이지')+'에서 확인하세요.',
      'Rubi Company is the official Korean distributor for Moulton Bicycles. You can buy at the official showroom, Rubi Workshop in Banpo, Seoul, and from authorised dealers across Korea. See the '+LINK_DEALER.format('dealer page')+' for your nearest store.',
      'モールトン・バイシクルの韓国正規ディストリビューターはRubi Companyです。ソウル・盤浦の公式ショールームRubi Workshopと、韓国各地の正規ディーラーでご購入いただけます。お近くの店舗は'+LINK_DEALER.format('正規ディーラーページ')+'でご確認ください。',
      'Rubi Company 是莫尔顿自行车的韩国官方经销商。您可在首尔盘浦的官方展厅 Rubi Workshop 以及韩国各地的授权经销商处购买。就近门店请查看'+LINK_DEALER.format('经销商页面')+'。'),
     ('전화 문의는 1551-5320 (월~금 12:00~19:00, 토 10:00~15:30)으로 주시면 됩니다.',
      'For enquiries by phone, call 1551-5320 (Mon–Fri 12:00–19:00, Sat 10:00–15:30 KST).',
      'お電話でのお問い合わせは +82 1551-5320（月〜金 12:00〜19:00、土 10:00〜15:30 KST）まで。',
      '电话咨询请致电 +82 1551-5320（周一至周五 12:00–19:00，周六 10:00–15:30 KST）。')]),
   (('영국 본사 온라인 스토어에서 직접 주문할 수 있나요?','Can I order directly from the UK online store?','英国本社のオンラインストアから直接注文できますか？','可以直接从英国官网在线下单吗？'),
    [('몰튼 UK의 온라인 주문은 영국 내 배송에 한정됩니다. 영국 외 지역의 고객은 해당 국가의 공식 디스트리뷰터를 통해 구매하도록 안내되며, 한국은 루비컴퍼니가 담당합니다. 정식 수입 제품만 한국 내 보증과 사후 지원을 받을 수 있습니다.',
      'Moulton UK\'s online store delivers to UK addresses only. Customers outside the UK are referred to the official distributor for their country, which for Korea is Rubi Company. Only officially imported bikes are covered by warranty and after-sales support in Korea.',
      'モールトンUKのオンライン注文は英国内配送に限られます。英国外のお客様は各国の正規ディストリビューターを通じて購入するよう案内され、韓国はRubi Companyが担当します。正規輸入品のみが韓国内での保証とアフターサポートを受けられます。',
      '莫尔顿英国官网的在线订单仅限英国境内配送。英国以外的客户将被引导至所在国家的官方经销商，韩国由 Rubi Company 负责。只有正规进口的车辆才能在韩国享受保修与售后支持。')]),
   (('프레임 사이즈는 어떻게 고르나요?','What frame size should I order?','フレームサイズはどう選べばいいですか？','应该选择什么车架尺寸？'),
    [('몰튼은 대부분의 라이더에게 맞도록 설계된 하나의 프레임 사이즈로 만들어집니다. 균형 잡힌 지오메트리는 신장 160~193cm에 맞고, 낮은 스텝스루 프레임과 조절식 스템으로 자세를 세밀하게 맞출 수 있습니다.',
      'Moulton bikes come in one frame size designed to fit most riders. The balanced geometry suits heights from 160 to 193 cm (5′3″ to 6′4″), and the low step-through frame and adjustable stem let you fine-tune your position.',
      'モールトンは、ほとんどのライダーに合うよう設計された一つのフレームサイズで作られます。バランスの取れたジオメトリーは身長160〜193cmに対応し、低いステップスルーフレームと調整式ステムでポジションを細かく調整できます。',
      '莫尔顿采用一种适合大多数骑行者的车架尺寸。均衡的几何结构适合身高 160–193 cm，低跨点车架与可调节把立可精细调整骑行姿势。'),
     ('모델마다 핏이 조금씩 다르므로 '+LINK_SIZING.format('사이징 가이드')+'의 모델별 인사이드 레그 표를 확인하세요. 쇼룸에서 직접 타 보시는 것이 가장 정확합니다.',
      'Fit varies slightly between models, so check the inside leg table in the '+LINK_SIZING.format('sizing guide')+'. The surest way is to try one at the showroom.',
      'モデルごとにフィットが少し異なるため、'+LINK_SIZING.format('サイジングガイド')+'のモデル別股下表をご確認ください。ショールームでの試乗が最も確実です。',
      '各车型的合身略有差异，请查看'+LINK_SIZING.format('尺寸指南')+'中的各车型内腿长表。最可靠的方式是到展厅试骑。')]),
   (('주문 후 납기는 얼마나 걸리나요?','What is the lead time?','注文後の納期はどのくらいですか？','下单后交期多久？'),
    [('몰튼은 영국 브래드퍼드 온 에이번 공장에서 주문 제작됩니다. 납기는 모델과 사양, 공장의 생산 일정, 부품 수급에 따라 달라지며, 쇼룸과 딜러에 전시·재고 중인 모델은 바로 구매하실 수 있습니다.',
      'Moulton bikes are built to order at the factory in Bradford on Avon, England. Lead time depends on the model, specification, factory schedule and component supply. Bikes in stock at the showroom or a dealer are available immediately.',
      'モールトンは英国ブラッドフォード・オン・エイヴォンの工場で受注生産されます。納期はモデルや仕様、工場の生産スケジュール、部品の供給状況によって異なります。ショールームやディーラーに展示・在庫のあるモデルはすぐにご購入いただけます。',
      '莫尔顿在英国 Bradford on Avon 工厂按订单生产。交期取决于车型、配置、工厂排期与零部件供应。展厅或经销商的现货车型可立即购买。'),
     ('정확한 납기는 주문 시점에 루비워크샵 또는 딜러에서 안내해 드립니다.',
      'Rubi Workshop or your dealer will confirm an estimated delivery date when you order.',
      '正確な納期は、ご注文時にRubi Workshopまたはディーラーがご案内します。',
      '下单时 Rubi Workshop 或经销商会告知预计交付日期。')]),
   (('커스텀 빌드도 가능한가요?','Are custom builds available?','カスタムビルドは可能ですか？','可以定制装配吗？'),
    [('네. 몰튼은 공장 '+LINK_FRAME.format('프레임킷')+'을 기반으로 구동계, 휠, 핸들바, 안장 등 부품을 직접 골라 조립할 수 있습니다. 루비워크샵과 프라임 딜러는 프레임셋 조립 상담을 전문으로 하며, 용도와 예산에 맞는 빌드를 제안해 드립니다.',
      'Yes. Starting from a factory '+LINK_FRAME.format('framekit')+', you can choose the drivetrain, wheels, handlebars, saddle and other components. Rubi Workshop and our prime dealers specialise in frameset builds and will propose a build to suit how you ride and your budget.',
      'はい。モールトンは工場の'+LINK_FRAME.format('フレームキット')+'をベースに、ドライブトレイン、ホイール、ハンドルバー、サドルなどのパーツを自由に選んで組み立てられます。Rubi Workshopとプライムディーラーはフレームセット組立相談を専門とし、用途と予算に合ったビルドをご提案します。',
      '可以。以工厂'+LINK_FRAME.format('车架套件')+'为基础，您可自行选择传动系统、轮组、车把、座垫等零件。Rubi Workshop 与高级经销商专注于车架组装咨询，会根据您的骑行用途与预算提出方案。')]),
   (('어디서 실물을 보고 시승할 수 있나요?','Where can I see and test ride a Moulton?','どこで実物を見て試乗できますか？','在哪里可以看实车并试骑？'),
    [('서울 반포의 공식 쇼룸 루비워크샵에서 전 모델을 보실 수 있습니다. 프라임 딜러인 테이크아웃바이크(고양)와 엠엔스퀘어(서울 마포)에서도 다수의 전시 모델과 테스트 라이딩이 가능합니다.',
      'The full range is on display at the official showroom, Rubi Workshop in Banpo, Seoul. Our prime dealers, Takeout Bike (Goyang) and MN Square (Mapo, Seoul), also keep multiple display models and offer test rides.',
      'ソウル・盤浦の公式ショールームRubi Workshopで全モデルをご覧いただけます。プライムディーラーのテイクアウトバイク（高陽）とMN Square（ソウル・麻浦）でも、多数の展示モデルと試乗が可能です。',
      '首尔盘浦的官方展厅 Rubi Workshop 展示全部车型。高级经销商 Takeout Bike（高阳）与 MN Square（首尔麻浦）也有多款展示车型并提供试骑。'),
     ('전시 모델은 매장마다 다르니 특정 모델을 보고 싶다면 방문 전 전화로 확인해 주세요.',
      'Display models vary by store, so please call ahead if you want to see a particular model.',
      '展示モデルは店舗ごとに異なるため、特定のモデルをご覧になりたい場合は、ご来店前にお電話でご確認ください。',
      '各门店展示车型不同，如需查看特定车型请提前致电确认。')]),
   (('컬러는 어떻게 고르나요?','How do I choose a colour?','カラーはどう選べばいいですか？','如何选择颜色？'),
    [('몰튼은 파우더 코트 15색과 스토브 에나멜 15색을 제공하며, 어떤 피니시가 적용되는지는 모델에 따라 다릅니다. 모델마다 기본 컬러가 정해져 있고 그 외 컬러는 추가 비용이 발생합니다. 전체 컬러는 '+LINK_COLORS.format('컬러 페이지')+'를 참고하세요.',
      'Moulton offers 15 powder coat and 15 stove enamel colours; which finish applies depends on the model. Each model has standard colours and others are available at extra cost. See the '+LINK_COLORS.format('colours page')+' for the full range.',
      'モールトンはパウダーコート15色とストーブエナメル15色を提供しており、どちらの仕上げが適用されるかはモデルによって異なります。モデルごとに標準色が決まっており、それ以外は追加費用が発生します。全カラーは'+LINK_COLORS.format('カラーページ')+'をご覧ください。',
      '莫尔顿提供 15 种粉末涂装与 15 种烤漆颜色，具体工艺取决于车型。每款车型有标准颜色，其他颜色需额外付费。全部颜色请参考'+LINK_COLORS.format('颜色页面')+'。')]),
  ]),

 ('bike', '02',
  ('몰튼 자전거에 대하여','About Moulton Bikes','モールトンの自転車について','关于莫尔顿自行车'),
  ('승차감, 효율, 작은 바퀴, 분리형 프레임. 몰튼이 왜 이렇게 생겼는지.','Comfort, efficiency, small wheels, the separable frame, and why a Moulton looks the way it does.','乗り心地、効率、小径ホイール、分割フレーム。モールトンがなぜこの形なのか。','舒适、效率、小轮径、可分离车架，以及莫尔顿为何长成这样。'),
  [
   (('몰튼은 타기에 편안한가요?','Is a Moulton comfortable to ride?','モールトンは乗り心地が良いですか？','莫尔顿骑起来舒适吗？'),
    [('편안함은 몰튼의 가장 큰 강점 중 하나입니다. 풀 서스펜션이 거친 노면을 부드럽게 걸러 주어 일반 자전거가 몸에 전달하는 충격을 크게 줄입니다. 정제된 지오메트리는 최적의 라이딩 자세를 만들고, 낮은 스텝스루 프레임은 타고 내리기를 쉽게 합니다.',
      'Comfort is one of the Moulton\'s great strengths. Full suspension smooths rough roads and takes away the jarring a conventional bike transmits to your body. The refined geometry gives an optimal riding position, and the low step-through frame makes mounting and dismounting easy.',
      '快適さはモールトンの最大の強みの一つです。フルサスペンションが荒れた路面を滑らかにし、一般的な自転車が体に伝える衝撃を大きく減らします。洗練されたジオメトリーは最適なライディングポジションを作り、低いステップスルーフレームは乗り降りを容易にします。',
      '舒适是莫尔顿最大的优势之一。全避震系统过滤粗糙路面，大幅减少普通自行车传递到身体的震动。精炼的几何结构带来最佳骑行姿势，低跨点车架便于上下车。')]),
   (('서스펜션이 있으면 효율이 떨어지지 않나요?','Does suspension make it less efficient?','サスペンションがあると効率が落ちませんか？','有避震会降低效率吗？'),
    [('아닙니다. 단단한 프레임, 작고 강성 높은 휠, 고압 타이어가 에너지 손실을 최소화해 반응이 빠르고 효율적인 주행을 만듭니다. 서스펜션은 라이더를 노면 충격에서 분리하면서도 바퀴가 지면에 밀착되게 유지합니다.',
      'No. The stiff frame, small rigid wheels and high-pressure tyres minimise energy loss for a responsive, efficient ride. The suspension isolates you from road shock while keeping the wheels in contact with the surface.',
      'いいえ。剛性の高いフレーム、小さく硬いホイール、高圧タイヤがエネルギー損失を最小限に抑え、反応が速く効率的な走りを生みます。サスペンションはライダーを路面の衝撃から分離しつつ、ホイールを路面に密着させ続けます。',
      '不会。坚固的车架、小而刚性的轮组与高压轮胎将能量损失降至最低，带来响应迅速、高效的骑行。避震系统隔离路面冲击，同时保持车轮与地面接触。'),
     ('그 결과 접지력은 좋아지고 진동 손실과 구름 저항은 줄어, 같은 부품을 쓴 일반 자전거보다 더 편안하고 효율적입니다. 원리는 '+LINK_SUSP.format('서스펜션 페이지')+'에서 자세히 볼 수 있습니다.',
      'That improves traction and reduces vibration losses and rolling resistance, making it both more comfortable and more efficient than a rigid bike with the same components. Read more on the '+LINK_SUSP.format('suspension page')+'.',
      'その結果、グリップは向上し、振動損失と転がり抵抗は減少するため、同じ部品を使った一般的な自転車より快適で効率的です。原理は'+LINK_SUSP.format('サスペンションページ')+'で詳しくご覧いただけます。',
      '由此抓地力提升，振动损耗与滚动阻力减少，比使用相同零件的硬架自行车更舒适、更高效。详见'+LINK_SUSP.format('避震系统页面')+'。')]),
   (('작은 바퀴가 성능에 유리한가요?','Are small wheels good for performance?','小径ホイールは性能面で有利ですか？','小轮径对性能有利吗？'),
    [('네. 작은 바퀴는 단단하고 강하며 가볍습니다. 관성 모멘트가 작아 가속이 빠르고 조향이 민첩하며, 공기 저항도 적습니다. 몰튼의 레이싱 역사, 세계 기록, 레이스 어크로스 아메리카에서의 성적이 이를 증명합니다.',
      'Yes. Small wheels are stiff, strong and light. Their lower moment of inertia means quicker acceleration and more responsive steering, and they create less aerodynamic drag. Moulton\'s racing history, a world record and strong results in the Race Across America bear this out.',
      'はい。小径ホイールは硬く、強く、軽量です。慣性モーメントが小さいため加速が速く、ステアリングは俊敏で、空気抵抗も少なくなります。モールトンのレース史、世界記録、レース・アクロス・アメリカでの成績がそれを証明しています。',
      '是的。小轮径刚性强、坚固且轻量。转动惯量更小，加速更快，转向更灵敏，风阻也更低。莫尔顿的竞赛历史、世界纪录以及横穿美国赛（RAAM）的成绩都是佐证。')]),
   (('몰튼은 어떤 라이딩에 어울리나요?','What type of riding is a Moulton suited to?','モールトンはどんなライディングに向いていますか？','莫尔顿适合哪种骑行？'),
    [('몰튼은 다재다능합니다. 레이싱, 투어링, 출퇴근, 일상 주행 어디에나 맞게 구성할 수 있고, 짧은 거리와 장거리 모두에 적합합니다. 서스펜션 덕분에 매끈한 아스팔트에서도, 거친 노면에서도 편안하고 유능합니다.',
      'A Moulton is versatile. It can be set up for racing, touring, commuting or everyday use, and suits short and long journeys alike. Thanks to its suspension it stays comfortable and capable on smooth tarmac and rougher ground.',
      'モールトンは万能です。レース、ツーリング、通勤、日常の走行など、どんな用途にも合わせて構成でき、短距離にも長距離にも適しています。サスペンションのおかげで、滑らかな舗装路でも荒れた路面でも快適で有能です。',
      '莫尔顿用途广泛。可配置为竞赛、旅行、通勤或日常骑行，短途长途皆宜。得益于避震系统，无论平整柏油路还是粗糙路面都舒适从容。')]),
   (('운반과 보관은 쉬운가요?','Can a Moulton be easily transported or stored?','運搬や保管は簡単ですか？','便于运输和存放吗？'),
    [('대부분의 모델은 주행 성능에 영향 없이 프레임을 두 부분으로 분리할 수 있습니다. 분리한 두 부분은 승용차 트렁크나 항공 여행용 대형 슈트케이스에 들어갑니다. 바퀴가 작아 전체 길이도 일반 자전거보다 짧아 주차와 보관이 쉽습니다.',
      'Most models have a frame that separates into two halves without affecting ride quality. The two halves fit in a car boot or a large suitcase for air travel. With its small wheels the bike is also shorter overall than a diamond-frame bike, which makes parking and storage easier.',
      'ほとんどのモデルは、走行性能に影響なくフレームを二つに分割できます。分割した二つの部分は、乗用車のトランクや航空旅行用の大型スーツケースに収まります。ホイールが小さいため全長も一般的な自転車より短く、駐輪や保管が容易です。',
      '大多数车型的车架可一分为二，且不影响骑行品质。两部分可放入轿车后备箱或航空旅行用的大型行李箱。由于轮径小，整车长度也比菱形车架自行车短，停放与存放更方便。')]),
   (('몰튼은 접이식 자전거인가요?','Is the Moulton a folding bike?','モールトンは折りたたみ自転車ですか？','莫尔顿是折叠车吗？'),
    [('아닙니다. 몰튼은 승차감과 주행 성능을 최우선으로 설계되었습니다. 대부분의 모델은 중앙 킹핀으로 프레임을 두 부분으로 분리할 수 있어 강성이나 핸들링, 승차감을 희생하지 않고 트렁크나 여행용 케이스에 넣을 수 있습니다.',
      'No. Moulton bikes are designed first for ride comfort and performance. Most models have a central kingpin that splits the frame into two halves for a car boot or travel case, without losing stiffness, handling or ride quality.',
      'いいえ。モールトンは乗り心地と走行性能を最優先に設計されています。ほとんどのモデルは中央のキングピンでフレームを二つに分割でき、剛性やハンドリング、乗り心地を犠牲にすることなくトランクや旅行用ケースに収められます。',
      '不是。莫尔顿以骑行舒适与性能为首要设计目标。大多数车型通过中央主销将车架一分为二，可放入后备箱或旅行箱，且不损失刚性、操控与骑行品质。'),
     ('뉴 시리즈 모델은 앞 포크와 리어 트라이앵글도 쉽게 분리되어 더 작게 보관하거나 비행기로 이동할 수 있습니다.',
      'New Series models also have easily removable front forks and rear triangles for more compact storage and airline travel.',
      'ニューシリーズモデルは、フロントフォークとリアトライアングルも簡単に取り外せるため、よりコンパクトに保管したり飛行機で移動したりできます。',
      'New Series 车型的前叉与后三角也可轻松拆卸，便于更紧凑地存放或搭乘飞机。')]),
   (('짐을 싣고 다니기에 적합한가요?','Is a Moulton suitable for carrying luggage?','荷物を積んで走るのに適していますか？','适合载物吗？'),
    [('네. 강성 높은 스페이스프레임과 낮은 무게중심 덕분에 몰튼은 뛰어난 짐 운반 능력을 갖췄습니다. 작은 바퀴는 짐을 낮게 실을 수 있게 해 안정성을 높이고, 격자 구조의 프레임은 하중을 고르게 분산합니다. 프레임 안쪽 공간에는 공구나 작은 물건을 넣을 수 있습니다.',
      'Yes. The rigid spaceframe and low centre of gravity make the Moulton a strong load carrier. Small wheels let luggage sit lower for better stability, the lattice frame spreads loads evenly, and there is space within the frame for tools or small items.',
      'はい。剛性の高いスペースフレームと低い重心により、モールトンは優れた積載能力を備えています。小径ホイールは荷物を低く積めるため安定性が高まり、格子構造のフレームは荷重を均等に分散します。フレーム内側のスペースには工具や小物を入れられます。',
      '是的。高刚性空间车架与低重心使莫尔顿具备出色的载物能力。小轮径让行李位置更低、更稳定，格构车架均匀分散负载，车架内部空间还可放置工具或小物件。'),
     ('몰튼은 풀 로드 투어링 자전거의 선두주자로, 전 세계 원정에서 그 능력을 입증해 왔습니다.',
      'Moulton is a leader among fully laden touring bikes and has been proven on expeditions worldwide.',
      'モールトンはフル積載ツーリングバイクの先駆者として、世界各地の遠征でその能力を証明してきました。',
      '莫尔顿是满载旅行车中的佼佼者，已在全球远征中得到验证。')]),
   (('몰튼은 왜 이렇게 다르게 생겼나요?','Why does the Moulton look so different?','モールトンはなぜこんなに違う形なのですか？','莫尔顿为什么长得如此不同？'),
    [('몰튼의 외형은 그 엔지니어링을 그대로 드러냅니다. 모든 요소가 분명한 목적을 가지고 있고, 그 결과가 이 독특한 형태입니다. 몰튼은 이 모습을 즐기고 감상해야 할 것으로 여깁니다.',
      'The Moulton\'s appearance is a direct expression of its engineering. Every element serves a purpose, and this distinctive form is the result. It is a look to be enjoyed and admired.',
      'モールトンの外観は、そのエンジニアリングをそのまま表しています。すべての要素に明確な目的があり、その結果がこの独特な形です。モールトンはこの姿を楽しみ、鑑賞すべきものと考えています。',
      '莫尔顿的外观是其工程设计的直接体现。每一个元素都有明确的目的，这种独特造型便是结果。它值得欣赏与品味。')]),
   (('몰튼은 누가 설계하고 만드나요?','Who designs and makes Moulton bicycles?','モールトンは誰が設計し、作っているのですか？','莫尔顿由谁设计和制造？'),
    [('몰튼은 영국 엔지니어링의 유산에서 태어났습니다. 가능한 최고 품질의 기계를 만들고자 했던 발명가 알렉스 몰튼 박사가 구상했고, 지금도 한 대 한 대 영국 브래드퍼드 온 에이번에서 수작업으로 만들어집니다. 설계, 소재, 조립 품질에 집중해 오래 지속되는 성능과 가치를 제공합니다.',
      'Moulton bikes come from a British engineering heritage. They were conceived by Dr Alex Moulton, an inventor who set out to build the highest-quality machine possible, and each bike is still hand-crafted in Bradford on Avon, England, with a focus on design, materials and build quality for lasting performance and value.',
      'モールトンは英国のエンジニアリングの遺産から生まれました。可能な限り最高品質の機械を作ろうとした発明家アレックス・モールトン博士が構想し、今も一台一台、英国ブラッドフォード・オン・エイヴォンで手作業で作られています。設計、素材、組立品質に集中し、長く続く性能と価値を提供します。',
      '莫尔顿源自英国工程传统。由立志打造最高品质机器的发明家亚历克斯·莫尔顿博士构想，至今每一台仍在英国 Bradford on Avon 手工制造，专注于设计、材料与装配品质，带来持久的性能与价值。')]),
   (('정비는 얼마나 자주 해야 하나요?','How much maintenance does a Moulton need?','メンテナンスはどのくらい必要ですか？','需要多少保养？'),
    [('서스펜션은 거의 손이 가지 않습니다. 뉴 시리즈 모델은 모든 움직임이 토션 러버 피벗에서 일어나기 때문에 마모되거나 굳을 베어링이 없습니다. 그 외 모델은 리어 피벗의 그리스 니플에 1년에 한 번 윤활하면 됩니다.',
      'The suspension needs little or no maintenance. New Series models have no bearings to wear or seize, since all movement happens in torsion rubber pivots. Other models only need the rear pivot lubricated through its grease nipple once a year.',
      'サスペンションはほとんどメンテナンスを必要としません。ニューシリーズモデルは、すべての動きがトーションラバーピボットで起こるため、摩耗したり固着したりするベアリングがありません。その他のモデルは、リアピボットのグリスニップルから年に一度注油するだけです。',
      '避震系统几乎无需保养。New Series 车型的所有运动均由扭转橡胶枢轴完成，没有会磨损或卡死的轴承。其他车型只需每年通过后枢轴的黄油嘴润滑一次。'),
     ('구동계와 브레이크 등 일반 부품은 보통의 자전거와 같이 관리하면 됩니다. 몰튼 고급 정비는 루비워크샵과 몰튼 서비스 라운지 딜러에서 받으실 수 있습니다.',
      'Drivetrain, brakes and other standard components are cared for like any bike. Advanced Moulton servicing is available at Rubi Workshop and at dealers designated as a Moulton Service Lounge.',
      'ドライブトレインやブレーキなどの一般的な部品は、通常の自転車と同様に管理してください。モールトンの高度な整備は、Rubi Workshopとモールトン サービスラウンジに指定されたディーラーで受けられます。',
      '传动、刹车等常规零件与普通自行车一样保养即可。莫尔顿高级维修可在 Rubi Workshop 及指定为莫尔顿服务中心的经销商处进行。')]),
  ]),

 ('support', '03',
  ('부품과 보증','Spares & Warranty','パーツと保証','零件与保修'),
  ('스페어 파츠, 보증 기간과 등록, 프레임 번호 찾는 법.','Spare parts, warranty terms and registration, and where to find your frame number.','スペアパーツ、保証期間と登録、フレーム番号の探し方。','备件、保修期限与登记，以及车架号的位置。'),
  [
   (('스페어 파츠는 어디서 구할 수 있나요?','Where can I buy spare parts?','スペアパーツはどこで入手できますか？','在哪里可以买到备件？'),
    [('몰튼 전용 부품은 한국 공식 디스트리뷰터 루비컴퍼니를 통해 공급됩니다. 루비워크샵 또는 가까운 공식 딜러에 문의하시면 맞는 부품을 확인하고 공장에서 주문해 장착까지 도와드립니다.',
      'Moulton-specific parts are supplied through Rubi Company, the official Korean distributor. Contact Rubi Workshop or your nearest authorised dealer; they will identify the correct part, order it from the factory and fit it if needed.',
      'モールトン専用パーツは、韓国正規ディストリビューターのRubi Companyを通じて供給されます。Rubi Workshopまたはお近くの正規ディーラーにお問い合わせいただければ、適合するパーツを確認し、工場から取り寄せて取り付けまでお手伝いします。',
      '莫尔顿专用零件通过韩国官方经销商 Rubi Company 供应。请联系 Rubi Workshop 或就近的授权经销商，他们会确认正确零件、向工厂订购并协助安装。'),
     ('1980년 이전에 생산된 모델은 공장에서 부품과 서비스 정보를 제공하지 않습니다. 이 경우 '+LINK_CLUB.format('몰튼 바이시클 클럽')+'이 도움이 될 수 있습니다.',
      'The factory cannot supply spares or service information for bikes made before 1980. For those, the '+LINK_CLUB.format('Moulton Bicycle Club')+' may be able to help.',
      '1980年以前に生産されたモデルについては、工場からパーツやサービス情報は提供されません。その場合は'+LINK_CLUB.format('モールトン・バイシクル・クラブ')+'が役立つかもしれません。',
      '1980 年以前生产的车型，工厂不再提供备件与服务信息。此类车辆可向'+LINK_CLUB.format('莫尔顿自行车俱乐部')+'寻求帮助。')]),
   (('보증 기간은 어떻게 되나요?','What is the warranty?','保証期間はどのくらいですか？','保修期限是多久？'),
    [('모든 몰튼은 소재와 제조상의 결함에 대해 기본 1년 보증을 제공합니다. 여기에 더해 구매일로부터 프레임과 포크는 10년, 몰튼 러버 서스펜션 부품은 5년의 연장 보증이 무상으로 적용됩니다. 연장 보증에는 별도의 조건이 있습니다.',
      'Every Moulton comes with a standard one-year guarantee against defects in materials or manufacture. In addition, the frame and fork are guaranteed for ten years and Moulton rubber suspension parts for five years from the date of purchase, free of charge. The extended guarantee has its own conditions.',
      'すべてのモールトンには、素材と製造上の欠陥に対する1年間の標準保証が付いています。さらに、購入日からフレームとフォークは10年、モールトンのラバーサスペンション部品は5年の延長保証が無償で適用されます。延長保証には別途条件があります。',
      '所有莫尔顿均提供一年标准保修，涵盖材料与制造缺陷。此外，自购买之日起车架与前叉保修十年，莫尔顿橡胶避震部件保修五年，均免费提供。延长保修有其附加条件。'),
     ('연장 보증을 받으려면 구매 후 90일 이내에 자전거를 등록해야 합니다. 한국에서 구매한 몰튼의 보증 등록과 접수는 루비컴퍼니가 안내해 드립니다.',
      'To receive the extended guarantee, the bike must be registered within 90 days of purchase. For Moultons bought in Korea, Rubi Company will guide you through registration and any warranty claim.',
      '延長保証を受けるには、購入後90日以内に自転車を登録する必要があります。韓国で購入したモールトンの保証登録と申請は、Rubi Companyがご案内します。',
      '享受延长保修须在购买后 90 天内登记车辆。在韩国购买的莫尔顿，保修登记与申请由 Rubi Company 协助办理。')]),
   (('제품에 결함이 있는 것 같으면 어떻게 하나요?','What if I think my bike is faulty?','製品に不具合があると思われる場合はどうすればいいですか？','如果怀疑产品有缺陷怎么办？'),
    [('모든 몰튼은 엄격한 검사를 거쳐 출고되지만, 제조상의 결함이 의심된다면 구매하신 루비워크샵 또는 딜러에 연락해 주세요. 프레임 번호와 증상, 가능하면 사진을 함께 보내 주시면 루비컴퍼니가 본사와 함께 확인해 처리합니다.',
      'Every Moulton goes through rigorous testing, but if you suspect a manufacturing fault, contact Rubi Workshop or the dealer you bought from. Send the frame number, a description and photos if possible, and Rubi Company will work with the factory to resolve it.',
      'すべてのモールトンは厳格な検査を経て出荷されますが、製造上の欠陥が疑われる場合は、ご購入のRubi Workshopまたはディーラーにご連絡ください。フレーム番号と症状、可能であれば写真を添えてお送りいただければ、Rubi Companyが本社と連携して対応します。',
      '每台莫尔顿出厂前都经过严格检测，但若怀疑存在制造缺陷，请联系购买的 Rubi Workshop 或经销商。请提供车架号、问题描述，如可能附上照片，Rubi Company 将与工厂共同处理。')]),
   (('프레임 번호는 어디서 찾나요?','Where do I find my frame number?','フレーム番号はどこにありますか？','车架号在哪里？'),
    [('여섯 자리 프레임 번호는 중앙 프레임 조인트의 뒤쪽, 또는 바텀 브래킷 튜브 아래에 각인되어 있습니다. 자전거마다 고유한 번호이며 보험 가입이나 도난 시 식별에 필요하니 기록해 두세요.',
      'The six-digit frame number is on the rear of the central frame joint or stamped under the bottom bracket tube. It is unique to your bike and is needed for insurance or identification if the bike is stolen, so keep a note of it.',
      '6桁のフレーム番号は、中央フレームジョイントの後ろ側、またはボトムブラケットチューブの下に刻印されています。自転車ごとに固有の番号で、保険加入や盗難時の識別に必要なので、控えておいてください。',
      '六位车架号位于中央车架接头的后方，或冲压在五通管下方。每辆车的编号唯一，投保或被盗时识别需要用到，请记录保存。'),
     ('일부 모델에는 바텀 브래킷 근처에 다섯 자리 "RP(Replacement Part)" 번호 라벨이 있습니다. 부품을 주문할 때 프레임 번호와 함께 알려 주세요.',
      'Some models also have a five-digit "RP" (Replacement Part) number label near the bottom bracket. Quote it along with the frame number when ordering spares.',
      '一部のモデルには、ボトムブラケット付近に5桁の「RP（Replacement Part）」番号ラベルがあります。パーツを注文する際は、フレーム番号と一緒にお知らせください。',
      '部分车型在五通附近还有五位"RP（Replacement Part）"编号标签。订购备件时请与车架号一并告知。')]),
  ]),
]

def esc(s):
    return s.replace('"', '&quot;')

def qa(q, paras):
    qk, qe, qj, qz = q
    body = ''.join(f'<p {t(*p)}>{p[0]}</p>' for p in paras)
    return f"""
        <details>
          <summary><span {t(qk,qe,qj,qz)}>{qk}</span><span class="ic" aria-hidden="true"></span></summary>
          <div class="a">{body}</div>
        </details>"""

def group(cid, num, title, intro, items):
    return f"""
<section class="grp" id="{cid}">
  <div class="wrap grp__grid">
    <div class="grp__head rv">
      <div class="num">{num}</div>
      <h2 {t(*title)}>{title[0]}</h2>
      <p {t(*intro)}>{intro[0]}</p>
    </div>
    <div class="qa rv">{''.join(qa(q, p) for q, p in items)}
    </div>
  </div>
</section>"""

def main():
    cats = ''.join(f'<a href="#{cid}" {t(*title)}>{title[0]}</a>' for cid, num, title, intro, items in FAQ)
    groups = ''.join(group(*g) for g in FAQ)
    return f"""
<main id="top">

<section class="phero">
  <img data-src="moulton-ns-safari-bike-frame-close-up-landscape.jpg" alt="Moulton NS Safari frame close-up" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow" {t('자주 묻는 질문','Frequently Asked Questions','よくあるご質問','常见问题')}>자주 묻는 질문</div>
    <h1>FAQ</h1>
    <p {t('몰튼 코리아에 가장 자주 들어오는 질문들을 모았습니다. 찾는 답이 없다면 루비워크샵으로 편하게 문의해 주세요.',
         'The questions we are asked most often about Moulton bicycles in Korea. If yours is not here, get in touch with Rubi Workshop.',
         'モールトン・コリアに最もよく寄せられる質問をまとめました。お探しの答えがなければ、お気軽にRubi Workshopまでお問い合わせください。',
         '汇集了莫尔顿韩国最常收到的问题。如果没有找到您要的答案，欢迎联系 Rubi Workshop。')}>몰튼 코리아에 가장 자주 들어오는 질문들을 모았습니다. 찾는 답이 없다면 루비워크샵으로 편하게 문의해 주세요.</p>
  </div>
</section>

<nav class="cats" aria-label="FAQ categories"><div class="wrap cats__in">{cats}</div></nav>
{groups}

<section class="cta">
  <div class="wrap rv">
    <div class="eyebrow" {t('더 궁금한 점이 있으신가요?','Still have a question?','他にご質問はありますか？','还有其他问题？')}>더 궁금한 점이 있으신가요?</div>
    <h2 {t('루비워크샵에 물어보세요','Ask Rubi Workshop','Rubi Workshopにお尋ねください','请咨询 Rubi Workshop')}>루비워크샵에 물어보세요</h2>
    <p {t('모델, 사이즈, 컬러, 납기, 보증까지. 몰튼에 관한 어떤 질문이든 서울 반포 쇼룸에서 답해 드립니다.',
         'Models, sizing, colours, lead times, warranty. Whatever your question about Moulton, the showroom in Banpo, Seoul has the answer.',
         'モデル、サイズ、カラー、納期、保証まで。モールトンに関するどんなご質問にも、ソウル・盤浦のショールームがお答えします。',
         '车型、尺寸、颜色、交期、保修。关于莫尔顿的任何问题，首尔盘浦展厅都会为您解答。')}>모델, 사이즈, 컬러, 납기, 보증까지. 몰튼에 관한 어떤 질문이든 서울 반포 쇼룸에서 답해 드립니다.</p>
    <a class="btn light" href="https://rubiworkshop.com/models" target="_blank" rel="noopener" {t('상담 신청','Consulting','ご相談はこちら','预约咨询')}>상담 신청</a>
    <a class="btn light" href="tel:15515320">1551-5320</a>
  </div>
</section>

</main>
<script>
(function(){{
  const links=[...document.querySelectorAll('.cats a')], secs=links.map(a=>document.querySelector(a.getAttribute('href')));
  const io=new IntersectionObserver(es=>{{es.forEach(e=>{{ if(e.isIntersecting){{ links.forEach(a=>a.classList.toggle('on', a.getAttribute('href')==='#'+e.target.id)); }} }});}},{{rootMargin:'-40% 0px -55% 0px'}});
  secs.forEach(s=>s&&io.observe(s));
}})();
</script>
"""
