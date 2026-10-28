# -*- coding: utf-8 -*-
"""/sizing 페이지 본문 (UK 'Sizing Guide' 페이지 번역). build.py가 읽어 sizing/index.html 생성.
   모델별 인사이드 레그 범위는 아래 SIZES 목록(인치 기준, cm는 자동 환산)."""
from build import t

SLUG = 'sizing'
TITLE_KO = '몰튼 사이징 가이드 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'몰튼 사이징 가이드 | Moulton Bicycles Korea', en:'Sizing Guide | Moulton Bicycles Korea', ja:'モールトン サイジングガイド | Moulton Bicycles Korea', zh:'莫尔顿尺寸指南 | Moulton Bicycles Korea'}"
DESCRIPTION = '몰튼은 하나의 프레임 사이즈로 신장 160~193cm 라이더에 맞춰 설계됩니다. 모델별 인사이드 레그 범위와 사이즈 선택 안내.'
OG_TITLE = 'Sizing Guide | Moulton Bicycles Korea'
OG_DESC = 'One size fits most. Inside leg length guide for every Moulton model.'

CSS = """
/* ===== Sizing page ===== */
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

.points{background:var(--bg-soft);padding:clamp(56px,7vw,96px) 0}
.points__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.pt{background:var(--bg-soft);padding:32px 28px 36px}
.pt .num{font-family:var(--en);font-size:13px;letter-spacing:.22em;color:var(--red);margin-bottom:18px}
.pt h3{font-size:19px;margin-bottom:12px}
.pt p{font-size:14.5px}

/* guide */
.guide{padding:clamp(64px,8vw,110px) 0}
.guide__grid{display:grid;grid-template-columns:1fr 1.4fr;gap:clamp(32px,6vw,96px);align-items:start}
.guide__img{position:relative;aspect-ratio:3/4;overflow:hidden;background:var(--bg-soft)}
.guide__img img{width:100%;height:100%;object-fit:cover}
.guide h2{margin-bottom:16px}
.guide p+p{margin-top:12px}
.how{margin-top:28px;padding:24px 26px;border:1px solid var(--ink)}
.how b{display:block;font-family:var(--en);font-size:12px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--red);margin-bottom:10px}
.how p{font-size:14.5px}
.tbl{width:100%;border-collapse:collapse;margin-top:36px;font-size:15px}
.tbl th,.tbl td{text-align:left;padding:14px 0;border-bottom:1px solid var(--line);vertical-align:top}
.tbl th{font-family:var(--en);font-weight:600;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);border-bottom:1px solid var(--ink)}
.tbl td.m{font-family:var(--en);font-weight:600;letter-spacing:.02em;width:34%}
.tbl td.m small{display:block;font-weight:400;font-size:12px;color:var(--ink-3);letter-spacing:.08em;margin-top:3px}
.tbl td.v{font-family:var(--en);font-variant-numeric:tabular-nums}
.tbl td.v span{display:block;color:var(--ink-3);font-size:13px;margin-top:2px}
.tbl tr.grp td{padding-top:26px}
.tbl tr.grp td.m small{color:var(--red)}
.foot{margin-top:18px;font-size:13px;color:var(--ink-3)}

/* cta */
.cta{background:var(--ink);color:#fff;padding:clamp(64px,8vw,110px) 0;text-align:center}
.cta .eyebrow{color:#fff;opacity:.85}
.cta h2{margin-bottom:16px}
.cta p{color:rgba(255,255,255,.75);margin:0 auto 32px}
.cta .btn{margin:6px}

@media (max-width:1024px){.points__grid{grid-template-columns:1fr}}
@media (max-width:820px){
  .lede__grid,.guide__grid{grid-template-columns:1fr;gap:28px}
  .guide__img{aspect-ratio:4/3}
  .tbl{font-size:14px}
}
@media (max-width:560px){.lede .stat{grid-template-columns:1fr 1fr}.phero{height:70vh}.tbl td.m{width:44%}}
"""

# ------------------------------------------------------------
# 모델별 인사이드 레그 (인치). 범위 2개면 ' / '로 표기 (AM Speed 시트튜브 19"/22")
#   (모델명, 시리즈 라벨, [(min, max), ...])
# ------------------------------------------------------------
SIZES = [
  ('NS Speed',    'New Series', [(28, 34.5)]),
  ('NS D-Pylon',  'New Series', [(28, 34.5)]),
  ('NS Safari',   'New Series', [(25, 36)]),
  ('NS Marathon', 'New Series', [(25, 36)]),
  ('Speed',       'Moulton',    [(25, 36)]),
  ('Jubilee',     'AM Series',  [(25, 36)]),
  ('AM 22',       'AM Series',  [(25, 36)]),
  ('AM GT',       'AM Series',  [(25, 36)]),
  ('AM Speed',    'AM Series',  [(27, 34), (30, 37)]),
  ('TSR',         'Y-frame',    [(27, 36)]),
  ('SST',         'Y-frame',    [(27, 36)]),
  ('XTB',         'Y-frame',    [(27, 36)]),
  ('Flyte',       'Y-frame',    [(27, 36)]),
]

def cm(i):
    v = i * 2.54
    return f'{v:.0f}'

def fmt_in(a, b):
    g = lambda x: f'{x:g}'
    return f'{g(a)}–{g(b)}"'

def rows():
    out = []
    last = None
    for name, series, ranges in SIZES:
        grp = ' class="grp"' if series != last else ''
        last = series
        inch = ' / '.join(fmt_in(a, b) for a, b in ranges)
        cms  = ' / '.join(f'{cm(a)}–{cm(b)} cm' for a, b in ranges)
        note = ''
        if name == 'AM Speed':
            note = f'<small {t("시트튜브 19&quot; / 22&quot; 선택","Seat tube 19&quot; / 22&quot;","シートチューブ 19&quot; / 22&quot;","座管 19&quot; / 22&quot;")}>시트튜브 19" / 22" 선택</small>'
        elif name == 'AM 22':
            note = f'<small {t("헤드튜브 10&quot; / 12.5&quot; 선택","Head tube 10&quot; / 12.5&quot;","ヘッドチューブ 10&quot; / 12.5&quot;","头管 10&quot; / 12.5&quot;")}>헤드튜브 10" / 12.5" 선택</small>'
        else:
            note = f'<small>{series}</small>'
        out.append(f'<tr{grp}><td class="m">{name}{note}</td><td class="v">{inch}<span>{cms}</span></td></tr>')
    return '\n'.join(out)

def main():
    return f"""
<main id="top">

<section class="phero">
  <img data-src="moulton-ns-safari-bike-frame-close-up-landscape.jpg" alt="Moulton NS Safari frame close-up" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow" {t('하나의 사이즈, 대부분의 라이더','One Size Fits Most','ワンサイズで、ほとんどのライダーに','一个尺寸，适合大多数骑行者')}>하나의 사이즈, 대부분의 라이더</div>
    <h1 {t('사이징','Sizing','サイジング','尺寸')}>사이징</h1>
    <p {t('몰튼은 정교하게 설계된 하나의 프레임 사이즈로 만들어집니다. 균형 잡힌 지오메트리는 신장 160cm부터 193cm까지의 라이더에게 맞습니다.',
         'Every Moulton is built in one carefully engineered frame size. Its balanced geometry fits riders from 160 to 193 cm (5′3″ to 6′4″).',
         'モールトンは、精密に設計された一つのフレームサイズで作られます。バランスの取れたジオメトリーは、身長160cmから193cmのライダーに適合します。',
         '莫尔顿采用一种精心设计的车架尺寸。均衡的几何结构适合身高 160 至 193 cm 的骑行者。')}>몰튼은 정교하게 설계된 하나의 프레임 사이즈로 만들어집니다. 균형 잡힌 지오메트리는 신장 160cm부터 193cm까지의 라이더에게 맞습니다.</p>
  </div>
</section>

<section class="lede">
  <div class="wrap lede__grid rv">
    <div>
      <div class="eyebrow">One Size Fits Most</div>
      <h2 {t('사이즈를 고르는 대신, 맞추는 자전거','A bike you adjust, not a size you choose','サイズを選ぶのではなく、合わせる自転車','不是选择尺寸，而是调整到合身')}>사이즈를 고르는 대신, 맞추는 자전거</h2>
    </div>
    <div>
      <p {t('몰튼의 낮은 스텝스루 프레임은 타고 내리기를 쉽게 하고, 조절식 스템은 넓은 범위의 핸들바 높이를 제공해 라이더가 자신의 자세를 세밀하게 맞출 수 있습니다.',
           'The low step-through frame makes mounting and dismounting easy, and adjustable stems offer a wide range of handlebar height so riders can fine-tune their position.',
           '低いステップスルーフレームは乗り降りを容易にし、調整式ステムは幅広いハンドルバー高さを提供するため、ライダーは自分のポジションを細かく調整できます。',
           '低跨点车架便于上下车，可调节把立提供宽广的车把高度范围，骑行者可以精细调整自己的姿势。')}>몰튼의 낮은 스텝스루 프레임은 타고 내리기를 쉽게 하고, 조절식 스템은 넓은 범위의 핸들바 높이를 제공해 라이더가 자신의 자세를 세밀하게 맞출 수 있습니다.</p>
      <p {t('그 결과 폭넓은 체형의 라이더에게 편안함과 제어력, 자신감을 주는 다재다능한 핏이 완성됩니다. 모델마다 핏이 조금씩 다르므로 아래 인사이드 레그 가이드를 참고하세요.',
           'The result is a versatile fit that gives comfort, control and confidence to a broad range of riders. Fit varies slightly between models, so use the inside leg guide below.',
           'その結果、幅広い体型のライダーに快適さ、コントロール、自信を与える万能なフィットが完成します。モデルごとにフィットが少し異なるため、下の股下ガイドをご参照ください。',
           '由此形成适合各种体型骑行者的多用途合身效果，带来舒适、掌控与自信。各车型的合身略有差异，请参考下方的内腿长指南。')}>그 결과 폭넓은 체형의 라이더에게 편안함과 제어력, 자신감을 주는 다재다능한 핏이 완성됩니다. 모델마다 핏이 조금씩 다르므로 아래 인사이드 레그 가이드를 참고하세요.</p>
      <div class="stat">
        <div><b>160–193<small style="font-size:.5em;font-weight:400"> cm</small></b><span {t('권장 신장','Rider Height','推奨身長','建议身高')}>권장 신장</span></div>
        <div><b>1</b><span {t('프레임 사이즈','Frame Size','フレームサイズ','车架尺寸')}>프레임 사이즈</span></div>
        <div><b>120<small style="font-size:.5em;font-weight:400"> kg</small></b><span {t('최대 하중','Max Load','最大荷重','最大载重')}>최대 하중</span></div>
      </div>
    </div>
  </div>
</section>

<section class="points">
  <div class="wrap">
    <div class="points__grid rv">
      <div class="pt">
        <div class="num">01</div>
        <h3 {t('낮은 스텝스루 프레임','Low Step-through Frame','低いステップスルーフレーム','低跨点车架')}>낮은 스텝스루 프레임</h3>
        <p {t('프레임을 넘어 올라탈 필요가 없어 타고 내리기가 쉽고, 신호 대기나 좁은 길에서도 안정적으로 발을 디딜 수 있습니다.',
             'No need to swing a leg over the frame. Mounting and dismounting is easy, and you can put a foot down with confidence at lights or in tight spaces.',
             'フレームをまたぐ必要がなく、乗り降りが簡単で、信号待ちや狭い道でも安定して足をつけます。',
             '无需跨过车架，上下车轻松，在等红灯或狭窄路段也能稳稳落脚。')}>프레임을 넘어 올라탈 필요가 없어 타고 내리기가 쉽고, 신호 대기나 좁은 길에서도 안정적으로 발을 디딜 수 있습니다.</p>
      </div>
      <div class="pt">
        <div class="num">02</div>
        <h3 {t('조절식 스템','Adjustable Stem','調整式ステム','可调节把立')}>조절식 스템</h3>
        <p {t('핸들바 높이를 넓은 범위에서 조절할 수 있어, 같은 프레임으로 공격적인 자세부터 편안한 업라이트 자세까지 맞출 수 있습니다.',
             'A wide range of handlebar height adjustment lets the same frame be set up for anything from an aggressive position to a relaxed, upright one.',
             'ハンドルバーの高さを広い範囲で調整できるため、同じフレームで攻撃的なポジションから快適なアップライトポジションまで対応できます。',
             '车把高度可在宽广范围内调节，同一车架既可设置为进取姿势，也可调整为舒适的直立姿势。')}>핸들바 높이를 넓은 범위에서 조절할 수 있어, 같은 프레임으로 공격적인 자세부터 편안한 업라이트 자세까지 맞출 수 있습니다.</p>
      </div>
      <div class="pt">
        <div class="num">03</div>
        <h3 {t('최대 하중 120kg','Max Load 120 kg','最大荷重 120kg','最大载重 120 kg')}>최대 하중 120kg</h3>
        <p {t('모든 모델의 최대 하중은 라이더와 짐을 합쳐 120kg(264lb)입니다. 투어링 짐을 실을 때도 이 범위 안에서 계획해 주세요.',
             'The maximum load for every model is 120 kg (264 lb), rider plus luggage. Plan touring loads within this limit.',
             '全モデルの最大荷重は、ライダーと荷物を合わせて120kg（264lb）です。ツーリングの荷物もこの範囲内で計画してください。',
             '所有车型的最大载重为骑行者加行李共 120 kg（264 lb）。装载旅行行李时请在此范围内规划。')}>모든 모델의 최대 하중은 라이더와 짐을 합쳐 120kg(264lb)입니다. 투어링 짐을 실을 때도 이 범위 안에서 계획해 주세요.</p>
      </div>
    </div>
  </div>
</section>

<section class="guide" id="inseam">
  <div class="wrap guide__grid rv">
    <div class="guide__img">
      <img data-src="moulton-ns-safari-bike-frame-close-up-portrait.jpg" alt="Moulton NS Safari frame" loading="lazy">
    </div>
    <div>
      <div class="eyebrow" {t('인사이드 레그 가이드','Inside Leg Length Guide','股下ガイド','内腿长指南')}>인사이드 레그 가이드</div>
      <h2 {t('모델별 인사이드 레그 범위','Inside leg range by model','モデル別 股下範囲','各车型内腿长范围')}>모델별 인사이드 레그 범위</h2>
      <p {t('프레임 사이즈는 하나지만 모델마다 시트튜브 길이가 달라 맞는 인사이드 레그 범위가 조금씩 다릅니다. 본인의 인사이드 레그를 재어 아래 표에서 확인하세요.',
           'There is one frame size, but seat tube lengths differ between models, so the inside leg range each model suits varies slightly. Measure your inside leg and check the table below.',
           'フレームサイズは一つですが、モデルごとにシートチューブの長さが異なるため、適合する股下の範囲が少しずつ異なります。ご自身の股下を測り、下の表でご確認ください。',
           '车架尺寸只有一种，但各车型座管长度不同，因此适合的内腿长范围略有差异。请测量您的内腿长并对照下表。')}>프레임 사이즈는 하나지만 모델마다 시트튜브 길이가 달라 맞는 인사이드 레그 범위가 조금씩 다릅니다. 본인의 인사이드 레그를 재어 아래 표에서 확인하세요.</p>
      <div class="how">
        <b {t('재는 방법','How to measure','測り方','测量方法')}>재는 방법</b>
        <p {t('신발을 벗고 벽에 등을 대고 선 뒤, 발바닥부터 허벅지 안쪽 가장 위(가랑이)까지의 길이를 잽니다. 바지의 안쪽 기장과는 다른 값이니 주의하세요.',
             'Stand against a wall without shoes and measure from the sole of your foot to the inner top of your thigh. Note this is not the same as your trouser inside leg length.',
             '靴を脱いで壁に背をつけて立ち、足の裏から太ももの内側の一番上（股）までの長さを測ります。ズボンの股下寸法とは異なるのでご注意ください。',
             '脱鞋背靠墙站立，从脚底量到大腿内侧最高处（裆部）。请注意这与裤子的内长不同。')}>신발을 벗고 벽에 등을 대고 선 뒤, 발바닥부터 허벅지 안쪽 가장 위(가랑이)까지의 길이를 잽니다. 바지의 안쪽 기장과는 다른 값이니 주의하세요.</p>
      </div>
      <table class="tbl">
        <thead><tr><th {t('모델','Model','モデル','车型')}>모델</th><th {t('인사이드 레그','Inside Leg Length','股下','内腿长')}>인사이드 레그</th></tr></thead>
        <tbody>
{rows()}
        </tbody>
      </table>
      <div class="foot" {t('cm 값은 인치 기준 환산치입니다. AM Speed는 시트튜브 길이(19" / 22")에 따라 두 범위 중 하나가 적용됩니다.',
                           'Centimetre values are converted from inches. For the AM Speed, one of the two ranges applies depending on seat tube length (19" / 22").',
                           'cm表記はインチからの換算値です。AM Speedはシートチューブ長（19" / 22"）により、2つの範囲のいずれかが適用されます。',
                           'cm 数值由英寸换算而来。AM Speed 根据座管长度（19" / 22"）适用两个范围之一。')}>cm 값은 인치 기준 환산치입니다. AM Speed는 시트튜브 길이(19" / 22")에 따라 두 범위 중 하나가 적용됩니다.</div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap rv">
    <div class="eyebrow" {t('사이징 상담','Sizing Advice','サイジング相談','尺寸咨询')}>사이징 상담</div>
    <h2 {t('어떤 모델이 맞을지 고민되시나요?','Not sure which model fits you?','どのモデルが合うか迷っていますか？','不确定哪款车型适合您？')}>어떤 모델이 맞을지 고민되시나요?</h2>
    <p {t('서울 반포 루비워크샵 쇼룸에서 직접 타 보고 스템과 안장 높이를 맞춰 볼 수 있습니다. 신장과 인사이드 레그, 원하는 모델을 남겨 주시면 상담해 드립니다.',
         'Try a Moulton in person at the Rubi Workshop showroom in Banpo, Seoul, and dial in stem and saddle height. Or tell us your height, inside leg and preferred model and we will advise.',
         'ソウル・盤浦のRubi Workshopショールームで実際に試乗し、ステムとサドルの高さを合わせることができます。身長、股下、ご希望のモデルをお知らせいただければご相談に応じます。',
         '欢迎到首尔盘浦 Rubi Workshop 展厅试骑，调整把立与座高。或留下您的身高、内腿长与心仪车型，我们将为您提供建议。')}>서울 반포 루비워크샵 쇼룸에서 직접 타 보고 스템과 안장 높이를 맞춰 볼 수 있습니다. 신장과 인사이드 레그, 원하는 모델을 남겨 주시면 상담해 드립니다.</p>
    <a class="btn light" href="https://rubiworkshop.com/models" target="_blank" rel="noopener" {t('상담 신청','Consulting','ご相談はこちら','预约咨询')}>상담 신청</a>
    <a class="btn light" href="/authorized-dealer/" {t('공식 딜러 찾기','Find a Dealer','ディーラーを探す','查找经销商')}>공식 딜러 찾기</a>
  </div>
</section>

</main>
"""
