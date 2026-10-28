# -*- coding: utf-8 -*-
"""/colors 페이지 본문 (UK 'Colours & Finishes' 페이지 번역). build.py가 읽어 colors/index.html 생성.
   컬러 추가·수정은 아래 POWDER / ENAMEL 목록만 고치면 됨. 스와치 이미지는 UK CDN의 moulton-bike-colour-<slug>.jpg"""
from build import t

SLUG = 'colors'
TITLE_KO = '몰튼 컬러 & 피니시 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'몰튼 컬러 & 피니시 | Moulton Bicycles Korea', en:'Colours & Finishes | Moulton Bicycles Korea', ja:'モールトン カラー＆仕上げ | Moulton Bicycles Korea', zh:'莫尔顿颜色与涂装 | Moulton Bicycles Korea'}"
DESCRIPTION = '몰튼 자전거의 프레임 컬러와 피니시. 파우더 코트 15색과 스토브 에나멜 15색, 기본 컬러와 추가 비용 컬러 안내.'
OG_TITLE = 'Colours & Finishes | Moulton Bicycles Korea'
OG_DESC = 'Powder coat and stove enamel colours for Moulton bicycles.'

CSS = """
/* ===== Colours page ===== */
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

.lede{padding:clamp(64px,8vw,110px) 0;border-bottom:1px solid var(--line)}
.lede__grid{display:grid;grid-template-columns:1fr 1.2fr;gap:clamp(32px,6vw,96px);align-items:start}
.lede h2{font-family:var(--en);font-weight:300;font-size:clamp(28px,3.6vw,48px);letter-spacing:-.02em}
html[lang="ko"] .lede h2,html[lang="ja"] .lede h2,html[lang="zh"] .lede h2{font-weight:300}
.lede p+p{margin-top:16px}
.lede .stat{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px;padding-top:28px;border-top:1px solid var(--line)}
.lede .stat b{display:block;font-family:var(--en);font-size:clamp(26px,3vw,40px);font-weight:600;letter-spacing:-.02em;line-height:1}
.lede .stat span{display:block;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-top:8px;font-family:var(--en)}

/* finish sections */
.finish{padding:clamp(64px,8vw,110px) 0}
.finish+.finish{padding-top:0}
.finish__head{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:end;margin-bottom:clamp(28px,4vw,48px);padding-bottom:22px;border-bottom:1px solid var(--ink)}
.finish__head .eyebrow{margin-bottom:10px}
.finish__head p{font-size:15px}
.finish__count{font-family:var(--en);font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-top:10px}
.swatches{display:grid;grid-template-columns:repeat(5,1fr);gap:clamp(14px,2vw,28px) clamp(12px,1.6vw,22px)}
.sw{display:block}
.sw__img{position:relative;aspect-ratio:1/1;overflow:hidden;background:var(--bg-soft);border:1px solid var(--line)}
.sw__img img{width:100%;height:100%;object-fit:cover;transition:transform 1s cubic-bezier(.2,.7,.2,1)}
.sw:hover .sw__img img{transform:scale(1.05)}
.sw__tag{position:absolute;top:10px;left:10px;font-family:var(--en);font-size:10px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;background:var(--ink);color:#fff;padding:5px 8px}
.sw__name{font-family:var(--en);font-weight:600;font-size:15px;letter-spacing:-.01em;margin-top:12px;line-height:1.3}
.sw__sub{font-size:13px;color:var(--ink-3);margin-top:3px;line-height:1.4}
html[lang="en"] .sw__sub{display:none}

/* notes */
.note{background:var(--bg-soft);padding:clamp(56px,7vw,96px) 0}
.note__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.nt{background:var(--bg-soft);padding:32px 28px 36px}
.nt .num{font-family:var(--en);font-size:13px;letter-spacing:.22em;color:var(--red);margin-bottom:18px}
.nt h3{font-size:19px;margin-bottom:12px}
.nt p{font-size:14.5px}

/* cta */
.cta{background:var(--ink);color:#fff;padding:clamp(64px,8vw,110px) 0;text-align:center}
.cta .eyebrow{color:#fff;opacity:.85}
.cta h2{margin-bottom:16px}
.cta p{color:rgba(255,255,255,.75);margin:0 auto 32px}
.cta .btn{margin:6px}

@media (max-width:1100px){.swatches{grid-template-columns:repeat(4,1fr)}}
@media (max-width:1024px){.note__grid{grid-template-columns:1fr}}
@media (max-width:820px){
  .lede__grid,.finish__head{grid-template-columns:1fr;gap:20px}
  .finish__head{align-items:start}
  .swatches{grid-template-columns:repeat(3,1fr)}
}
@media (max-width:560px){.swatches{grid-template-columns:repeat(2,1fr)}.lede .stat{grid-template-columns:1fr 1fr}.phero{height:70vh}}
"""

# ------------------------------------------------------------
# 컬러 목록: (slug, 영문명, 한글, 일본어, 중국어, 태그 또는 None)
#   slug → 이미지 moulton-bike-colour-<slug>.jpg (UK CDN, IMG_BASE)
# ------------------------------------------------------------
POWDER = [
  ('airforce-blue',  'Airforce Blue',   '에어포스 블루',   'エアフォースブルー',   '空军蓝', None),
  ('ash-green',      'Ash Green',       '애쉬 그린',       'アッシュグリーン',     '灰绿', None),
  ('black',          'Black',           '블랙',            'ブラック',             '黑色', None),
  ('bright-red',     'Bright Red',      '브라이트 레드',   'ブライトレッド',       '亮红', None),
  ('burgundy',       'Burgundy',        '버건디',          'バーガンディ',         '酒红', None),
  ('camel-yellow',   'Camel Yellow',    '카멜 옐로우',     'キャメルイエロー',     '驼黄', None),
  ('duck-egg-blue',  'Duck Egg Blue',   '덕 에그 블루',    'ダックエッグブルー',   '鸭蛋蓝', None),
  ('forest-green',   'Forest Green',    '포레스트 그린',   'フォレストグリーン',   '森林绿', None),
  ('graphite-grey',  'Graphite Grey',   '그라파이트 그레이','グラファイトグレー',  '石墨灰', None),
  ('hall-green',     'Hall Green',      '홀 그린',         'ホールグリーン',       '霍尔绿', ('The Hall SE','The Hall SE','The Hall SE','The Hall SE')),
  ('orange',         'Orange',          '오렌지',          'オレンジ',             '橙色', None),
  ('powder-blue',    'Powder Blue',     '파우더 블루',     'パウダーブルー',       '粉蓝', None),
  ('powder-pink',    'Powder Pink',     '파우더 핑크',     'パウダーピンク',       '粉红', None),
  ('riviera-blue',   'Riviera Blue',    '리비에라 블루',   'リビエラブルー',       '里维埃拉蓝', None),
  ('sage-grey',      'Sage Grey',       '세이지 그레이',   'セージグレー',         '鼠尾草灰', None),
]
ENAMEL = [
  ('black',                'Black',                '블랙',               'ブラック',                 '黑色', None),
  ('british-racing-green', 'British Racing Green', '브리티시 레이싱 그린','ブリティッシュレーシンググリーン','英国赛车绿', None),
  ('bugatti-blue',         'Bugatti Blue',         '부가티 블루',        'ブガッティブルー',         '布加迪蓝', None),
  ('camel-yellow',         'Camel Yellow',         '카멜 옐로우',        'キャメルイエロー',         '驼黄', None),
  ('ferrari-red',          'Ferrari Red',          '페라리 레드',        'フェラーリレッド',         '法拉利红', None),
  ('grasmere-green',       'Grasmere Green',       '그래스미어 그린',    'グラスミアグリーン',       '格拉斯米尔绿', None),
  ('olive-green',          'Olive Green',          '올리브 그린',        'オリーブグリーン',         '橄榄绿', None),
  ('pale-grey',            'Pale Grey',            '페일 그레이',        'ペールグレー',             '浅灰', None),
  ('pearl-copper',         'Pearl Copper',         '펄 코퍼',            'パールコッパー',           '珠光铜', None),
  ('pearl-white',          'Pearl White',          '펄 화이트',          'パールホワイト',           '珠光白', None),
  ('royal-blue',           'Royal Blue',           '로열 블루',          'ロイヤルブルー',           '宝蓝', None),
  ('silver-grey',          'Silver Grey',          '실버 그레이',        'シルバーグレー',           '银灰', None),
  ('steely-grey',          'Steely Grey',          '스틸리 그레이',      'スティーリーグレー',       '钢灰', None),
  ('sunrise-orange',       'Sunrise Orange',       '선라이즈 오렌지',    'サンライズオレンジ',       '日出橙', None),
  ('willow-green',         'Willow Green',         '윌로우 그린',        'ウィローグリーン',         '柳绿', None),
]

def swatch(c):
    slug, en, ko, ja, zh, tag = c
    tag_html = f'<span class="sw__tag" {t(*tag)}>{tag[0]}</span>' if tag else ''
    return f"""
      <div class="sw">
        <div class="sw__img">{tag_html}<img data-src="moulton-bike-colour-{slug}.jpg" alt="Moulton {en}" loading="lazy"></div>
        <div class="sw__name">{en}</div>
        <div class="sw__sub" {t(ko,'',ja,zh)}>{ko}</div>
      </div>"""

def grid(colors):
    return ''.join(swatch(c) for c in colors)

def main():
    return f"""
<main id="top">

<section class="phero">
  <img data-src="moulton-ns-rapide-sunrise-orange-grey-bg-close-up.jpg" alt="Moulton NS Rapide in Sunrise Orange" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow" {t('컬러 & 피니시','Colours & Finishes','カラー＆仕上げ','颜色与涂装')}>컬러 & 피니시</div>
    <h1 {t('몰튼 컬러','Moulton Colours','モールトンのカラー','莫尔顿颜色')}>몰튼 컬러</h1>
    <p {t('프레임, 하이라이트, 액세서리까지. 몰튼의 모든 모델에 적용되는 페인트 컬러와 두 가지 피니시를 소개합니다.',
         'Frames, highlights and accessories. The paint colours and two finishes available across every Moulton model.',
         'フレーム、ハイライト、アクセサリーまで。すべてのモールトンに適用されるペイントカラーと2種類の仕上げをご紹介します。',
         '从车架、高光到配件。莫尔顿全系车型可选的涂装颜色与两种表面处理。')}>프레임, 하이라이트, 액세서리까지. 몰튼의 모든 모델에 적용되는 페인트 컬러와 두 가지 피니시를 소개합니다.</p>
  </div>
</section>

<section class="lede">
  <div class="wrap lede__grid rv">
    <div>
      <div class="eyebrow">Colours &amp; Finishes</div>
      <h2 {t('한 대의 몰튼, 서른 가지 표정','One Moulton, thirty expressions','一台のモールトン、三十の表情','一台莫尔顿，三十种表情')}>한 대의 몰튼, 서른 가지 표정</h2>
    </div>
    <div>
      <p {t('이 페이지는 몰튼 각 모델의 프레임 컬러와 프레임 하이라이트, 액세서리에 적용되는 페인트 컬러를 보여 줍니다. 일부 컬러는 기본으로 제공되며, 일부는 추가 비용이 발생합니다.',
           'This page shows the paint colours available for the frame, frame highlights and accessories of each Moulton model. Some colours come as standard and some are available for an additional cost.',
           'このページでは、モールトン各モデルのフレーム、フレームハイライト、アクセサリーに適用されるペイントカラーをご紹介します。一部のカラーは標準で、一部は追加費用が発生します。',
           '本页展示莫尔顿各车型的车架、车架高光与配件可选的涂装颜色。部分颜色为标准配置，部分需额外付费。')}>이 페이지는 몰튼 각 모델의 프레임 컬러와 프레임 하이라이트, 액세서리에 적용되는 페인트 컬러를 보여 줍니다. 일부 컬러는 기본으로 제공되며, 일부는 추가 비용이 발생합니다.</p>
      <p {t('몰튼은 파우더 코트와 스토브 에나멜 두 가지 피니시를 사용하며, 어떤 피니시가 적용되는지는 모델에 따라 다릅니다. 화면의 스와치는 참고용이며 실제 색상과 차이가 있을 수 있습니다. 컬러에 관한 문의는 루비워크샵으로 연락해 주세요.',
           'Moulton uses two finishes, powder coat and stove enamel, and which one is applied depends on the model. On-screen swatches are a guide only and may differ from the actual colour. Please contact Rubi Workshop with any questions about colours.',
           'モールトンはパウダーコートとストーブエナメルの2種類の仕上げを使用しており、どちらが適用されるかはモデルによって異なります。画面上の色見本は参考用で、実際の色と異なる場合があります。カラーに関するご質問はRubi Workshopまでお問い合わせください。',
           '莫尔顿采用粉末涂装与烤漆两种表面处理，具体取决于车型。屏幕上的色样仅供参考，可能与实物存在差异。关于颜色的问题，请联系 Rubi Workshop。')}>몰튼은 파우더 코트와 스토브 에나멜 두 가지 피니시를 사용하며, 어떤 피니시가 적용되는지는 모델에 따라 다릅니다. 화면의 스와치는 참고용이며 실제 색상과 차이가 있을 수 있습니다. 컬러에 관한 문의는 루비워크샵으로 연락해 주세요.</p>
      <div class="stat">
        <div><b>{len(POWDER)}</b><span {t('파우더 코트','Powder Coat','パウダーコート','粉末涂装')}>파우더 코트</span></div>
        <div><b>{len(ENAMEL)}</b><span {t('스토브 에나멜','Stove Enamel','ストーブエナメル','烤漆')}>스토브 에나멜</span></div>
        <div><b>2</b><span {t('피니시','Finishes','仕上げ','表面处理')}>피니시</span></div>
      </div>
    </div>
  </div>
</section>

<section class="finish" id="powder">
  <div class="wrap">
    <div class="finish__head rv">
      <div>
        <div class="eyebrow" {t('피니시 01','Finish 01','仕上げ 01','表面处理 01')}>피니시 01</div>
        <h2 {t('파우더 코트 컬러','Powder Coat Colours','パウダーコートカラー','粉末涂装颜色')}>파우더 코트 컬러</h2>
        <div class="finish__count">{len(POWDER)} <span {t('컬러','Colours','色','色')}>컬러</span></div>
      </div>
      <p {t('파우더 코트는 건조한 분말 도료를 프레임에 입힌 뒤 열로 경화시키는 피니시입니다. 내구성이 뛰어나고 긁힘과 마모에 강하며, 매끄럽고 균일한 질감으로 일상의 라이딩에 잘 어울립니다.',
           'Powder coat is a dry powder applied to the frame and cured under heat. It is durable, resists chips and wear, and gives a smooth, consistent finish well suited to everyday riding.',
           'パウダーコートは、乾いた粉体塗料をフレームに塗布し、熱で硬化させる仕上げです。耐久性に優れ、欠けや摩耗に強く、滑らかで均一な質感は日常のライディングによく合います。',
           '粉末涂装是将干粉涂料附着于车架后经高温固化的工艺。耐久性强，抗刮擦与磨损，光滑均匀的质感适合日常骑行。')}>파우더 코트는 건조한 분말 도료를 프레임에 입힌 뒤 열로 경화시키는 피니시입니다. 내구성이 뛰어나고 긁힘과 마모에 강하며, 매끄럽고 균일한 질감으로 일상의 라이딩에 잘 어울립니다.</p>
    </div>
    <div class="swatches rv">{grid(POWDER)}
    </div>
  </div>
</section>

<section class="finish" id="enamel">
  <div class="wrap">
    <div class="finish__head rv">
      <div>
        <div class="eyebrow" {t('피니시 02','Finish 02','仕上げ 02','表面处理 02')}>피니시 02</div>
        <h2 {t('스토브 에나멜 컬러','Stove Enamel Colours','ストーブエナメルカラー','烤漆颜色')}>스토브 에나멜 컬러</h2>
        <div class="finish__count">{len(ENAMEL)} <span {t('컬러','Colours','色','色')}>컬러</span></div>
      </div>
      <p {t('스토브 에나멜은 오븐에서 구워 내는 전통적인 도장 방식입니다. 깊이 있는 색감과 매끄러운 광택이 특징이며, 몰튼의 클래식한 아름다움을 가장 잘 살려 주는 피니시입니다.',
           'Stove enamel is a traditional paint finish baked in an oven. Prized for its depth of colour and smooth gloss, it is the finish that best brings out the classic beauty of a Moulton.',
           'ストーブエナメルは、オーブンで焼き付ける伝統的な塗装方法です。深みのある色合いと滑らかな光沢が特徴で、モールトンのクラシックな美しさを最もよく引き出す仕上げです。',
           '烤漆是在烤箱中烘烤固化的传统涂装工艺。色泽深邃、光泽细腻，最能展现莫尔顿的经典之美。')}>스토브 에나멜은 오븐에서 구워 내는 전통적인 도장 방식입니다. 깊이 있는 색감과 매끄러운 광택이 특징이며, 몰튼의 클래식한 아름다움을 가장 잘 살려 주는 피니시입니다.</p>
    </div>
    <div class="swatches rv">{grid(ENAMEL)}
    </div>
  </div>
</section>

<section class="note">
  <div class="wrap">
    <div class="note__grid rv">
      <div class="nt">
        <div class="num">01</div>
        <h3 {t('기본 컬러와 추가 비용 컬러','Standard and Extra-cost Colours','標準色と追加費用色','标准色与加价色')}>기본 컬러와 추가 비용 컬러</h3>
        <p {t('모델마다 기본으로 제공되는 컬러가 정해져 있으며, 그 외 컬러는 추가 비용이 발생합니다. 원하시는 모델과 컬러를 알려 주시면 적용 가능 여부와 비용을 안내해 드립니다.',
             'Each model has a set of standard colours; other colours are available for an additional cost. Tell us the model and colour you have in mind and we will confirm availability and cost.',
             'モデルごとに標準色が決まっており、それ以外のカラーは追加費用が発生します。ご希望のモデルとカラーをお知らせいただければ、適用の可否と費用をご案内します。',
             '每款车型均有指定的标准颜色，其他颜色需额外付费。告知您想要的车型与颜色，我们将确认可行性与费用。')}>모델마다 기본으로 제공되는 컬러가 정해져 있으며, 그 외 컬러는 추가 비용이 발생합니다. 원하시는 모델과 컬러를 알려 주시면 적용 가능 여부와 비용을 안내해 드립니다.</p>
      </div>
      <div class="nt">
        <div class="num">02</div>
        <h3 {t('피니시는 모델에 따라','Finish Depends on the Model','仕上げはモデルによって','表面处理因车型而异')}>피니시는 모델에 따라</h3>
        <p {t('파우더 코트와 스토브 에나멜 중 어느 피니시가 적용되는지는 모델과 프레임 구조에 따라 정해집니다. 블랙과 카멜 옐로우처럼 두 피니시 모두에서 제공되는 컬러도 있습니다.',
             'Whether a model is finished in powder coat or stove enamel is determined by the model and its frame construction. Some colours, such as Black and Camel Yellow, are offered in both finishes.',
             'パウダーコートとストーブエナメルのどちらが適用されるかは、モデルとフレーム構造によって決まります。ブラックやキャメルイエローのように、両方の仕上げで提供されるカラーもあります。',
             '采用粉末涂装还是烤漆，由车型与车架结构决定。黑色、驼黄等部分颜色在两种工艺中均有提供。')}>파우더 코트와 스토브 에나멜 중 어느 피니시가 적용되는지는 모델과 프레임 구조에 따라 정해집니다. 블랙과 카멜 옐로우처럼 두 피니시 모두에서 제공되는 컬러도 있습니다.</p>
      </div>
      <div class="nt">
        <div class="num">03</div>
        <h3 {t('실물로 확인하세요','See It in Person','実物でご確認を','现场查看实物')}>실물로 확인하세요</h3>
        <p {t('화면의 스와치는 참고용입니다. 서울 반포 루비워크샵 쇼룸에서 실제 프레임과 컬러 샘플을 직접 보고 고르실 수 있습니다.',
             'On-screen swatches are a guide only. Visit the Rubi Workshop showroom in Banpo, Seoul to see actual frames and colour samples before you decide.',
             '画面上の色見本は参考用です。ソウル・盤浦のRubi Workshopショールームで、実際のフレームとカラーサンプルをご覧いただいてお選びいただけます。',
             '屏幕上的色样仅供参考。欢迎到首尔盘浦 Rubi Workshop 展厅，现场查看实车与色样后再做选择。')}>화면의 스와치는 참고용입니다. 서울 반포 루비워크샵 쇼룸에서 실제 프레임과 컬러 샘플을 직접 보고 고르실 수 있습니다.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap rv">
    <div class="eyebrow" {t('컬러 상담','Colour Consulting','カラー相談','颜色咨询')}>컬러 상담</div>
    <h2 {t('나만의 몰튼 컬러를 찾고 계신가요?','Looking for your Moulton colour?','あなただけのモールトンカラーをお探しですか？','寻找属于您的莫尔顿颜色？')}>나만의 몰튼 컬러를 찾고 계신가요?</h2>
    <p {t('모델과 컬러, 피니시 조합은 루비워크샵에서 상담해 드립니다. 원하는 모델과 컬러를 남겨 주세요.',
         'Rubi Workshop can advise on model, colour and finish combinations. Tell us the model and colour you have in mind.',
         'モデルとカラー、仕上げの組み合わせはRubi Workshopがご相談に応じます。ご希望のモデルとカラーをお知らせください。',
         '车型、颜色与表面处理的搭配，欢迎咨询 Rubi Workshop。请留下您想要的车型与颜色。')}>모델과 컬러, 피니시 조합은 루비워크샵에서 상담해 드립니다. 원하는 모델과 컬러를 남겨 주세요.</p>
    <a class="btn light" href="https://rubiworkshop.com/models" target="_blank" rel="noopener" {t('상담 신청','Consulting','ご相談はこちら','预约咨询')}>상담 신청</a>
    <a class="btn light" href="/#bikes" {t('전 모델 보기','View all bikes','全モデルを見る','查看全部车型')}>전 모델 보기</a>
  </div>
</section>

</main>
"""
