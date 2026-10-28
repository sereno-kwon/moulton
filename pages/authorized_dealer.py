# -*- coding: utf-8 -*-
"""/authorized-dealer 페이지 본문 (공식 쇼룸 · 프라임 딜러 · 인증 딜러). build.py가 읽어 authorized-dealer/index.html 생성.
   딜러 추가·수정은 아래 DEALERS 목록만 고치면 됨.  실행: python3 build.py authorized_dealer"""
from build import t

SLUG = 'authorized-dealer'
TITLE_KO = '몰튼 공식 딜러 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'몰튼 공식 딜러 | Moulton Bicycles Korea', en:'Authorised Dealers | Moulton Bicycles Korea', ja:'正規ディーラー | Moulton Bicycles Korea', zh:'授权经销商 | Moulton Bicycles Korea'}"
DESCRIPTION = '몰튼 코리아 공식 쇼룸 루비워크샵과 전국의 몰튼 프라임 딜러·인증 딜러 안내. 상담, 커스터마이징, 고급 정비까지 가까운 공식 딜러에서 만나보세요.'
OG_TITLE = 'Authorised Dealers | Moulton Bicycles Korea'
OG_DESC = 'Official showroom and authorised Moulton dealers across Korea.'

CSS = """
/* ===== Dealer page ===== */
.eyebrow{font-size:14px;letter-spacing:.18em;margin-bottom:16px}
.dhero .eyebrow{font-size:15px;margin-bottom:22px}
.dealer__region{font-size:13px;letter-spacing:.16em}
.dealer__badge{font-size:12px;letter-spacing:.14em;padding:6px 11px}
.dealer__en{font-size:13px}
.dealer__tags span{font-size:13px}
.tier__count{font-size:14px;letter-spacing:.14em}
.dhero__meta{font-size:14px;letter-spacing:.14em}
.info li b{font-size:13px;letter-spacing:.12em}
.nt .num{font-size:13px}
.dhero{background:var(--ink);color:#fff;padding:clamp(72px,10vw,140px) 0 clamp(56px,7vw,96px)}
.dhero .eyebrow{color:#fff;opacity:.85}
.dhero h1{font-size:clamp(38px,6vw,84px);line-height:1;letter-spacing:-.03em;max-width:14ch}
html[lang="ko"] .dhero h1{font-family:var(--ko);font-weight:500;word-break:keep-all}
html[lang="ja"] .dhero h1,html[lang="zh"] .dhero h1{letter-spacing:0;line-height:1.1}
.dhero p{color:rgba(255,255,255,.78);margin-top:24px;max-width:54ch}
.dhero__meta{display:flex;flex-wrap:wrap;gap:12px 40px;margin-top:40px;padding-top:28px;border-top:1px solid rgba(255,255,255,.16);font-family:var(--en);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.6)}
.dhero__meta b{color:#fff;font-weight:600;margin-right:8px}

/* showroom */
.showroom{padding:clamp(64px,8vw,110px) 0;border-bottom:1px solid var(--line)}
.showroom__grid{display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(32px,6vw,96px);align-items:start}
.showroom h2{font-weight:300;font-size:clamp(28px,3.6vw,48px);letter-spacing:-.02em}
html[lang="ko"] .showroom h2,html[lang="ja"] .showroom h2,html[lang="zh"] .showroom h2{font-weight:300}
.showroom p+p{margin-top:14px}
.info{list-style:none;border-top:1px solid var(--line)}
.info li{display:grid;grid-template-columns:130px 1fr;gap:16px;padding:14px 0;border-bottom:1px solid var(--line);font-size:15px}
.info li b{font-family:var(--en);font-weight:600;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);padding-top:4px}
.info li a{border-bottom:1px solid var(--line);transition:border-color .2s}
.info li a:hover{border-color:var(--ink)}
.showroom .btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}

/* tiers */
.tier{padding:clamp(64px,8vw,110px) 0}
.tier+.tier{padding-top:0}
.tier__head{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:end;margin-bottom:clamp(28px,4vw,48px);padding-bottom:22px;border-bottom:1px solid var(--ink)}
.tier__head .eyebrow{margin-bottom:10px}
.tier__head p{font-size:15px}
.tier__count{font-family:var(--en);font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-3);margin-top:10px}

.dealers{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.dealers.cert{grid-template-columns:repeat(3,1fr)}
.dealer{background:var(--bg);padding:34px 30px 36px;display:flex;flex-direction:column;gap:0;position:relative;transition:background .25s}
.dealer:hover{background:var(--bg-soft)}
.dealer__top{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;margin-bottom:18px}
.dealer__region{font-family:var(--en);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--red);font-weight:600}
.dealer__badge{font-family:var(--en);font-size:10px;letter-spacing:.18em;text-transform:uppercase;padding:5px 9px;border:1px solid var(--ink);color:var(--ink);white-space:nowrap}
.prime .dealer__badge{background:var(--ink);color:#fff}
.dealer h3{font-size:clamp(22px,2.2vw,28px);letter-spacing:-.02em;margin-bottom:6px}
html[lang="ko"] .dealer h3{font-weight:500}
.dealer__en{font-family:var(--en);font-size:12px;letter-spacing:.08em;color:var(--ink-3);margin-bottom:20px}
.dealer__addr{font-size:14.5px;color:var(--ink-2);line-height:1.55;margin-bottom:18px;word-break:keep-all}
.dealer__tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:24px}
.dealer__tags span{font-size:12px;padding:5px 10px;background:var(--bg-soft);color:var(--ink-2);border:1px solid var(--line)}
.dealer:hover .dealer__tags span{background:#fff}
.dealer__tags span.lounge{background:var(--ink);color:#fff;border-color:var(--ink)}
.dealer:hover .dealer__tags span.lounge{background:var(--ink)}
.dealer__links{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:auto;padding-top:20px;border-top:1px solid var(--line)}
.dealer__links a{font-family:var(--en);font-size:13px;font-weight:600;letter-spacing:.08em;border-bottom:1px solid transparent;transition:border-color .2s}
.dealer__links a:hover{border-color:var(--ink)}
.dealer__links a.tel{letter-spacing:.04em}
.dealer__links a.site:after{content:"\\2197";margin-left:6px;font-weight:400}

/* notes */
.note{background:var(--bg-soft);padding:clamp(56px,7vw,96px) 0}
.note__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.nt{background:var(--bg-soft);padding:32px 28px 36px}
.nt .num{font-family:var(--en);font-size:11px;letter-spacing:.22em;color:var(--red);margin-bottom:18px}
.nt h3{font-size:19px;margin-bottom:12px}
.nt p{font-size:14.5px}

/* cta */
.cta{background:var(--ink);color:#fff;padding:clamp(64px,8vw,110px) 0;text-align:center}
.cta h2{margin-bottom:16px}
.cta p{color:rgba(255,255,255,.75);margin:0 auto 32px}
.cta .btn{margin:6px}

@media (max-width:1024px){.dealers.cert{grid-template-columns:repeat(2,1fr)}.note__grid{grid-template-columns:1fr}}
@media (max-width:820px){
  .showroom__grid,.tier__head{grid-template-columns:1fr;gap:20px}
  .tier__head{align-items:start}
  .dealers,.dealers.cert{grid-template-columns:1fr}
  .dealer{padding:28px 22px 30px}
  .info li{grid-template-columns:100px 1fr}
}
"""

# 딜러별 서비스 태그 (코드 → 4개 언어)
TAGS = {
    'ns':     ('뉴시리즈 & 플래그십 상담',  'New Series & flagship consulting', 'ニューシリーズ＆フラッグシップ相談', '新系列与旗舰车型咨询'),
    'frame':  ('프레임셋 조립 상담',        'Frameset build consulting',        'フレームセット組立相談',             '车架组装咨询'),
    'display':('다수의 전시 모델',          'Multiple display models',          '展示モデル多数',                     '多款展示车型'),
    'service':('몰튼 고급 정비',            'Advanced Moulton service',         'モールトン高度整備',                 '莫尔顿高级维修'),
    'test':   ('테스트 라이딩 가능',        'Test rides available',             '試乗可能',                           '可试骑'),
}

# ------------------------------------------------------------
# DEALERS  — tier: prime | cert
#   name:   (ko, en)
#   region: (ko, en, ja, zh)   카드 좌상단 지역 표기
#   addr:   (ko, en)            일본어·중국어는 영문 주소 사용
#   lounge: 몰튼 서비스 라운지 담당 지역 (ko, en, ja, zh) 또는 None
#   tags:   TAGS 키 목록
# ------------------------------------------------------------
DEALERS = [
  dict(tier='prime', name=('테이크아웃바이크','Takeout Bike'),
       region=('경기 고양 · 일산','Goyang, Gyeonggi','京畿道 高陽','京畿道 高阳'),
       addr=('경기도 고양시 일산서구 중앙로 1470 문촌마을10단지아파트','1470 Jungang-ro, Ilsanseo-gu, Goyang-si, Gyeonggi-do'),
       tel='070-7737-7733', site='https://takeoutbike.com/product/list.html?cate_no=100',
       lounge=None, tags=['ns','frame','display','service','test']),
  dict(tier='prime', name=('엠엔스퀘어','MN Square'),
       region=('서울 마포','Mapo, Seoul','ソウル 麻浦','首尔 麻浦'),
       addr=('서울시 마포구 신수로 5','5 Sinsu-ro, Mapo-gu, Seoul'),
       tel='0507-1320-1977', site='https://smartstore.naver.com/mnsquare',
       lounge=None, tags=['ns','frame','display','service','test']),

  dict(tier='cert', name=('화신자전거','Hwashin Bicycle'),
       region=('광주','Gwangju','光州','光州'),
       addr=('광주광역시 광산구 신가동 906-3','906-3 Singa-dong, Gwangsan-gu, Gwangju'),
       tel='062-531-6140', site='https://smartstore.naver.com/hwashinbicycle/category/01ce394ff9c848748336a3162e736c8e?cp=1',
       lounge=('광주 · 전라','Gwangju & Jeolla','光州・全羅','光州及全罗'), tags=['display','service']),
  dict(tier='cert', name=('파라마운트','Paramount'),
       region=('대구 수성','Suseong, Daegu','大邱 寿城','大邱 寿城'),
       addr=('대구광역시 수성구 중동 135-7','135-7 Jung-dong, Suseong-gu, Daegu'),
       tel='053-766-1212', site='https://smartstore.naver.com/paramount/category/f5b244e1a5d74a3da5750b84c18f70a0?cp=1',
       lounge=('대구 · 경북','Daegu & Gyeongbuk','大邱・慶北','大邱及庆北'), tags=['display','service']),
  dict(tier='cert', name=('쿠샵','Kushop'),
       region=('경기 성남 · 분당','Seongnam, Gyeonggi','京畿道 城南','京畿道 城南'),
       addr=('경기도 성남시 분당구 황새울로 132번길 22 1층','1F, 22 Hwangsaeul-ro 132beon-gil, Bundang-gu, Seongnam-si, Gyeonggi-do'),
       tel='031-714-9896', site='https://smartstore.naver.com/kushop/category/466eee3bf2244958beeff74f1e8b47d3?cp=1',
       lounge=('성남 · 수도권','Seongnam & Greater Seoul','城南・首都圏','城南及首都圈'), tags=['service']),
  dict(tier='cert', name=('라이드위드유','Ride With You'),
       region=('울산','Ulsan','蔚山','蔚山'),
       addr=('울산 중구 염포로 80 1층','1F, 80 Yeompo-ro, Jung-gu, Ulsan'),
       tel='0507-1314-5678', site='https://www.ridewithyou.net/goods/goods_list.php?cateCd=002009011',
       lounge=('울산 · 경남','Ulsan & Gyeongnam','蔚山・慶南','蔚山及庆南'), tags=['service']),
  dict(tier='cert', name=('레드도트','Red Dot'),
       region=('대구 수성','Suseong, Daegu','大邱 寿城','大邱 寿城'),
       addr=('대구 수성구 파동로 253 수성빌딩 1층','1F Suseong Bldg, 253 Padong-ro, Suseong-gu, Daegu'),
       tel='053-763-1232', site='https://smartstore.naver.com/reddotshop',
       lounge=None, tags=[]),
  dict(tier='cert', name=('벨로하우스','Velo House'),
       region=('서울 송파','Songpa, Seoul','ソウル 松坡','首尔 松坡'),
       addr=('서울시 송파구 백제고분로 31길 41 1층','1F, 41 Baekjegobun-ro 31-gil, Songpa-gu, Seoul'),
       tel='0507-1392-5880', site='https://www.velohouse.co.kr/goods/goods_list.php?cateCd=014',
       lounge=None, tags=[]),
]

def dealer_card(d):
    badge = {'prime': t('프라임 딜러','Prime Dealer','プライムディーラー','高级经销商'),
             'cert':  t('인증 딜러','Authorised Dealer','正規ディーラー','授权经销商')}[d['tier']]
    tags = ''
    if d['lounge']:
        ko,en,ja,zh = d['lounge']
        tags += f'<span class="lounge" {t("몰튼 서비스 라운지 · "+ko, "Moulton Service Lounge · "+en, "モールトン サービスラウンジ · "+ja, "莫尔顿服务中心 · "+zh)}>몰튼 서비스 라운지 · {ko}</span>'
    for k in d['tags']:
        ko,en,ja,zh = TAGS[k]
        tags += f'<span {t(ko,en,ja,zh)}>{ko}</span>'
    tags_html = f'<div class="dealer__tags">{tags}</div>' if tags else ''
    ko_name, en_name = d['name']
    ko_addr, en_addr = d['addr']
    r_ko, r_en, r_ja, r_zh = d['region']
    return f"""
      <article class="dealer {d['tier']}">
        <div class="dealer__top">
          <div class="dealer__region" {t(r_ko,r_en,r_ja,r_zh)}>{r_ko}</div>
          <div class="dealer__badge" {badge}>{'프라임 딜러' if d['tier']=='prime' else '인증 딜러'}</div>
        </div>
        <h3 {t(ko_name,en_name,ko_name,ko_name)}>{ko_name}</h3>
        <div class="dealer__en" {t(en_name,ko_name,en_name,en_name)}>{en_name}</div>
        <div class="dealer__addr" {t(ko_addr,en_addr,en_addr,en_addr)}>{ko_addr}</div>
        {tags_html}
        <div class="dealer__links">
          <a class="tel" href="tel:{d['tel'].replace('-','')}">{d['tel']}</a>
          <a class="site" href="{d['site']}" target="_blank" rel="noopener" {t('온라인 스토어','Online Store','オンラインストア','在线商店')}>온라인 스토어</a>
        </div>
      </article>"""

prime_cards = ''.join(dealer_card(d) for d in DEALERS if d['tier']=='prime')
cert_cards  = ''.join(dealer_card(d) for d in DEALERS if d['tier']=='cert')
n_prime = sum(1 for d in DEALERS if d['tier']=='prime')
n_cert  = sum(1 for d in DEALERS if d['tier']=='cert')

def main():
    return f"""
<main id="top">

<section class="dhero">
  <div class="wrap">
    <div class="eyebrow" {t('구매 안내 · 공식 딜러','Where to Buy · Authorised Dealers','購入案内 · 正規ディーラー','购买指南 · 授权经销商')}>구매 안내 · 공식 딜러</div>
    <h1 {t('몰튼 공식 딜러','Authorised Dealers','モールトン正規ディーラー','莫尔顿授权经销商')}>몰튼 공식 딜러</h1>
    <p {t('몰튼에 대한 자세한 상담과 커스터마이징, 숙련된 정비까지. 몰튼 코리아가 인증한 전국의 공식 딜러에서 몰튼 라이프를 시작해 보세요.',
         'Detailed consultation, customisation and skilled servicing. Begin your Moulton life at an authorised dealer certified by Moulton Korea.',
         'モールトンに関する詳しいご相談、カスタマイズ、熟練の整備まで。モールトン・コリアが認定した正規ディーラーで、モールトンのある暮らしを始めてください。',
         '从详细咨询、定制到专业维修。在莫尔顿韩国认证的授权经销商处，开启您的莫尔顿生活。')}>몰튼에 대한 자세한 상담과 커스터마이징, 숙련된 정비까지. 몰튼 코리아가 인증한 전국의 공식 딜러에서 몰튼 라이프를 시작해 보세요.</p>
    <div class="dhero__meta">
      <div><b>01</b><span {t('공식 쇼룸','Official Showroom','公式ショールーム','官方展厅')}>공식 쇼룸</span></div>
      <div><b>{n_prime:02d}</b><span {t('프라임 딜러','Prime Dealers','プライムディーラー','高级经销商')}>프라임 딜러</span></div>
      <div><b>{n_cert:02d}</b><span {t('인증 딜러','Authorised Dealers','正規ディーラー','授权经销商')}>인증 딜러</span></div>
    </div>
  </div>
</section>

<section class="showroom">
  <div class="wrap showroom__grid rv">
    <div>
      <div class="eyebrow" {t('공식 쇼룸','Official Showroom','公式ショールーム','官方展厅')}>공식 쇼룸</div>
      <h2 {t('루비워크샵, 서울 반포','Rubi Workshop, Banpo Seoul','Rubi Workshop ソウル・盤浦','Rubi Workshop 首尔盘浦')}>루비워크샵, 서울 반포</h2>
      <p style="margin-top:20px" {t('루비워크샵은 몰튼 한국 공식 디스트리뷰터 루비컴퍼니가 운영하는 몰튼 코리아 공식 쇼룸입니다. 전 모델을 직접 보고, 사이즈와 빌드 구성을 상담받을 수 있습니다.',
         'Rubi Workshop is the official Moulton Korea showroom, run by Rubi Company, the official Korean distributor for Moulton. See the full range in person and get sizing and build advice.',
         'Rubi Workshopは、モールトン韓国正規ディストリビューターのRubi Companyが運営するモールトン・コリア公式ショールームです。全モデルを実際にご覧いただき、サイズやビルド構成のご相談が可能です。',
         'Rubi Workshop 是莫尔顿韩国官方经销商 Rubi Company 运营的莫尔顿韩国官方展厅。可现场查看全部车型，并获得尺寸与装配建议。')}>루비워크샵은 몰튼 한국 공식 디스트리뷰터 루비컴퍼니가 운영하는 몰튼 코리아 공식 쇼룸입니다. 전 모델을 직접 보고, 사이즈와 빌드 구성을 상담받을 수 있습니다.</p>
      <p {t('신모델 입고, 한정 컬러, 코리안 에디션 등 몰튼 코리아의 모든 소식이 가장 먼저 닿는 곳입니다.',
         'It is also the first place to see new arrivals, limited colours and Korean editions from Moulton Korea.',
         '新モデルの入荷、限定カラー、コリアンエディションなど、モールトン・コリアのすべてのニュースが最初に届く場所です。',
         '新车型到货、限量颜色、韩国特别版等莫尔顿韩国的所有资讯都会第一时间在这里呈现。')}>신모델 입고, 한정 컬러, 코리안 에디션 등 몰튼 코리아의 모든 소식이 가장 먼저 닿는 곳입니다.</p>
      <div class="btns">
        <a class="btn" href="https://rubiworkshop.com" target="_blank" rel="noopener">rubiworkshop.com</a>
        <a class="btn red" href="https://rubiworkshop.com/models" target="_blank" rel="noopener" {t('상담 신청','Consulting','ご相談はこちら','预约咨询')}>상담 신청</a>
      </div>
    </div>
    <ul class="info">
      <li><b {t('주소','Address','住所','地址')}>주소</b><span {t('서울특별시 서초구 신반포로 320 루비빌딩','Rubi Building, 320 Sinbanpo-ro, Seocho-gu, Seoul','Rubi Building, 320 Sinbanpo-ro, Seocho-gu, Seoul','Rubi Building, 320 Sinbanpo-ro, Seocho-gu, Seoul')}>서울특별시 서초구 신반포로 320 루비빌딩</span></li>
      <li><b {t('전화','Phone','電話','电话')}>전화</b><span><a href="tel:15515320">1551-5320</a></span></li>
      <li><b {t('운영시간','Hours','営業時間','营业时间')}>운영시간</b><span {t('월~금 12:00~19:00<br>토 10:00~15:30 · 일요일 휴무','Mon–Fri 12:00–19:00<br>Sat 10:00–15:30 · Closed Sunday','月〜金 12:00〜19:00<br>土 10:00〜15:30 · 日曜休','周一至周五 12:00–19:00<br>周六 10:00–15:30 · 周日休息')}>월~금 12:00~19:00<br>토 10:00~15:30 · 일요일 휴무</span></li>
      <li><b>Instagram</b><span><a href="https://www.instagram.com/rubi.workshop" target="_blank" rel="noopener">@rubi.workshop</a></span></li>
      <li><b {t('온라인','Online','オンライン','在线')}>온라인</b><span><a href="https://rubiworkshop.com" target="_blank" rel="noopener">rubiworkshop.com</a></span></li>
    </ul>
  </div>
</section>

<section class="tier">
  <div class="wrap">
    <div class="tier__head rv">
      <div>
        <div class="eyebrow" {t('프라임 딜러','Prime Dealers','プライムディーラー','高级经销商')}>프라임 딜러</div>
        <h2 {t('몰튼 프라임 딜러','Moulton Prime Dealers','モールトン プライムディーラー','莫尔顿高级经销商')}>몰튼 프라임 딜러</h2>
        <div class="tier__count">{n_prime} <span {t('개 매장','Stores','店舗','家门店')}>개 매장</span></div>
      </div>
      <p {t('뉴시리즈와 플래그십 모델 상담, 프레임셋 조립 상담에 특화된 최상위 딜러입니다. 다수의 전시 모델과 테스트 라이딩, 몰튼 고급 정비까지 쇼룸에 준하는 경험을 제공합니다.',
           'Our top-tier dealers, specialising in New Series and flagship consultation and frameset builds. Multiple display models, test rides and advanced Moulton servicing offer a showroom-level experience.',
           'ニューシリーズとフラッグシップモデルの相談、フレームセット組立相談に特化した最上位ディーラーです。多数の展示モデル、試乗、高度な整備まで、ショールームに準じた体験を提供します。',
           '专注于新系列与旗舰车型咨询、车架组装咨询的顶级经销商。多款展示车型、试骑及莫尔顿高级维修，提供媲美展厅的体验。')}>뉴시리즈와 플래그십 모델 상담, 프레임셋 조립 상담에 특화된 최상위 딜러입니다. 다수의 전시 모델과 테스트 라이딩, 몰튼 고급 정비까지 쇼룸에 준하는 경험을 제공합니다.</p>
    </div>
    <div class="dealers rv">{prime_cards}
    </div>
  </div>
</section>

<section class="tier">
  <div class="wrap">
    <div class="tier__head rv">
      <div>
        <div class="eyebrow" {t('인증 딜러','Authorised Dealers','正規ディーラー','授权经销商')}>인증 딜러</div>
        <h2 {t('몰튼 인증 딜러','Moulton Authorised Dealers','モールトン正規ディーラー','莫尔顿授权经销商')}>몰튼 인증 딜러</h2>
        <div class="tier__count">{n_cert} <span {t('개 매장','Stores','店舗','家门店')}>개 매장</span></div>
      </div>
      <p {t('몰튼 코리아가 인증한 전국의 딜러입니다. 재고 확인과 주문, 기본 상담이 가능하며, 몰튼 서비스 라운지로 지정된 딜러에서는 해당 지역의 고급 정비를 담당합니다.',
           'Dealers across Korea certified by Moulton Korea. Check stock, place orders and get advice; dealers designated as a Moulton Service Lounge handle advanced servicing for their region.',
           'モールトン・コリアが認定した韓国各地のディーラーです。在庫確認、ご注文、基本的なご相談が可能で、モールトン サービスラウンジに指定されたディーラーは、その地域の高度な整備を担当します。',
           '莫尔顿韩国认证的全国经销商。可查询库存、下单及基本咨询；被指定为莫尔顿服务中心的经销商负责所在地区的高级维修。')}>몰튼 코리아가 인증한 전국의 딜러입니다. 재고 확인과 주문, 기본 상담이 가능하며, 몰튼 서비스 라운지로 지정된 딜러에서는 해당 지역의 고급 정비를 담당합니다.</p>
    </div>
    <div class="dealers cert rv">{cert_cards}
    </div>
  </div>
</section>

<section class="note">
  <div class="wrap">
    <div class="note__grid rv">
      <div class="nt">
        <div class="num">01</div>
        <h3 {t('정품 보증','Genuine Guarantee','正規品保証','正品保证')}>정품 보증</h3>
        <p {t('공식 쇼룸과 딜러를 통해 판매되는 몰튼은 몰튼 바이시클 컴퍼니의 정식 수입 제품으로, 한국 공식 디스트리뷰터 루비컴퍼니의 보증과 사후 지원을 받습니다.',
             'Every Moulton sold through the official showroom and dealers is a genuine import from the Moulton Bicycle Company, backed by the warranty and after-sales support of Rubi Company, the official Korean distributor.',
             '公式ショールームと正規ディーラーで販売されるモールトンは、モールトン・バイシクル・カンパニーの正規輸入品であり、韓国正規ディストリビューターRubi Companyの保証とアフターサポートを受けられます。',
             '通过官方展厅与授权经销商销售的莫尔顿均为莫尔顿自行车公司的正规进口产品，享有韩国官方经销商 Rubi Company 的保修与售后支持。')}>공식 쇼룸과 딜러를 통해 판매되는 몰튼은 몰튼 바이시클 컴퍼니의 정식 수입 제품으로, 한국 공식 디스트리뷰터 루비컴퍼니의 보증과 사후 지원을 받습니다.</p>
      </div>
      <div class="nt">
        <div class="num">02</div>
        <h3 {t('몰튼 서비스 라운지','Moulton Service Lounge','モールトン サービスラウンジ','莫尔顿服务中心')}>몰튼 서비스 라운지</h3>
        <p {t('서비스 라운지로 지정된 딜러는 몰튼 서스펜션과 프레임 구조에 대한 교육을 거쳐 해당 지역의 고급 정비를 담당합니다. 가까운 라운지에서 점검과 정비를 받으실 수 있습니다.',
             'Dealers designated as a Service Lounge have been trained on Moulton suspension and frame construction and handle advanced servicing for their region. Visit your nearest lounge for inspection and maintenance.',
             'サービスラウンジに指定されたディーラーは、モールトンのサスペンションとフレーム構造に関する教育を受け、その地域の高度な整備を担当します。お近くのラウンジで点検・整備をお受けいただけます。',
             '被指定为服务中心的经销商经过莫尔顿避震系统与车架结构培训，负责所在地区的高级维修。您可在就近的服务中心进行检查与保养。')}>서비스 라운지로 지정된 딜러는 몰튼 서스펜션과 프레임 구조에 대한 교육을 거쳐 해당 지역의 고급 정비를 담당합니다. 가까운 라운지에서 점검과 정비를 받으실 수 있습니다.</p>
      </div>
      <div class="nt">
        <div class="num">03</div>
        <h3 {t('방문 전 확인','Before You Visit','ご来店前に','到访前确认')}>방문 전 확인</h3>
        <p {t('전시 모델과 재고는 매장마다 다릅니다. 특정 모델이나 컬러를 보고 싶다면 방문 전 전화로 확인해 주세요. 운영시간은 각 매장에 문의하시기 바랍니다.',
             'Display models and stock vary by store. If you wish to see a particular model or colour, please call ahead. Opening hours are available from each store.',
             '展示モデルと在庫は店舗ごとに異なります。特定のモデルやカラーをご覧になりたい場合は、ご来店前にお電話でご確認ください。営業時間は各店舗にお問い合わせください。',
             '各门店的展示车型与库存不同。如需查看特定车型或颜色，请在到访前致电确认。营业时间请咨询各门店。')}>전시 모델과 재고는 매장마다 다릅니다. 특정 모델이나 컬러를 보고 싶다면 방문 전 전화로 확인해 주세요. 운영시간은 각 매장에 문의하시기 바랍니다.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap rv">
    <div class="eyebrow" style="color:#fff;opacity:.85" {t('딜러 문의','Become a Dealer','ディーラーのお問い合わせ','经销商咨询')}>딜러 문의</div>
    <h2 {t('몰튼 딜러를 희망하시나요?','Interested in becoming a Moulton dealer?','モールトンのディーラーをご希望ですか？','想成为莫尔顿经销商？')}>몰튼 딜러를 희망하시나요?</h2>
    <p {t('몰튼 공식 딜러 프로그램은 한국 공식 디스트리뷰터 루비컴퍼니의 B2B 채널, 루비서플라이에서 운영합니다.',
         'The Moulton dealer programme in Korea is run by Rubi Supply, the B2B channel of Rubi Company, the official Korean distributor.',
         '韓国のモールトン正規ディーラープログラムは、韓国正規ディストリビューターRubi CompanyのB2BチャネルRubi Supplyが運営しています。',
         '韩国的莫尔顿授权经销商计划由韩国官方经销商 Rubi Company 的 B2B 渠道 Rubi Supply 运营。')}>몰튼 공식 딜러 프로그램은 한국 공식 디스트리뷰터 루비컴퍼니의 B2B 채널, 루비서플라이에서 운영합니다.</p>
    <a class="btn light" href="https://rubisupply.com" target="_blank" rel="noopener">rubisupply.com</a>
    <a class="btn light" href="tel:025168465">02-516-8465</a>
  </div>
</section>

</main>
"""
