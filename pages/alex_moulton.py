# -*- coding: utf-8 -*-
"""/alex-moulton 페이지 본문 (UK 'Dr Alex Moulton' 페이지 번역). build.py가 읽어 alex-moulton/index.html 생성.
   갤러리 사진은 GALLERY, 연표는 TIMELINE 목록."""
from build import t

SLUG = 'alex-moulton'
TITLE_KO = '알렉스 몰튼 박사 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'알렉스 몰튼 박사 | Moulton Bicycles Korea', en:'Dr Alex Moulton | Moulton Bicycles Korea', ja:'アレックス・モールトン博士 | Moulton Bicycles Korea', zh:'亚历克斯·莫尔顿博士 | Moulton Bicycles Korea'}"
DESCRIPTION = '미니의 서스펜션을 설계하고 1962년 몰튼 자전거를 세상에 내놓은 영국의 엔지니어, 알렉스 몰튼 박사(1920~2012)의 생애와 철학.'
OG_TITLE = 'Dr Alex Moulton | Moulton Bicycles Korea'
OG_DESC = 'The visionary British engineer behind the Mini suspension and the Moulton bicycle.'

CSS = """
/* ===== Alex Moulton page ===== */
.eyebrow{font-size:14px;letter-spacing:.18em;margin-bottom:16px}
.phero{position:relative;height:min(78vh,760px);min-height:460px;overflow:hidden;background:#161616}
.phero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%;filter:saturate(.8)}
.phero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.7) 0%,rgba(0,0,0,.35) 45%,rgba(0,0,0,.05) 75%),linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.5) 100%)}
.phero__txt{position:absolute;left:0;right:0;bottom:clamp(40px,8vh,80px);z-index:2;color:#fff}
.phero__txt .eyebrow{color:#fff;opacity:.85;font-size:15px;margin-bottom:22px}
.phero__txt h1{font-size:clamp(36px,6vw,84px);line-height:1;letter-spacing:-.03em;text-shadow:0 2px 24px rgba(0,0,0,.35)}
html[lang="ko"] .phero__txt h1{font-family:var(--ko);font-weight:500;word-break:keep-all}
html[lang="ja"] .phero__txt h1,html[lang="zh"] .phero__txt h1{letter-spacing:0;line-height:1.1}
.phero__txt p{color:rgba(255,255,255,.85);margin-top:20px;max-width:52ch}
.phero__txt .dates{font-family:var(--en);font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.7);margin-top:18px}

.lede{padding:clamp(64px,8vw,110px) 0}
.lede__grid{display:grid;grid-template-columns:1fr 1.2fr;gap:clamp(32px,6vw,96px);align-items:start}
.lede h2{font-family:var(--en);font-weight:300;font-size:clamp(28px,3.6vw,48px);letter-spacing:-.02em}
html[lang="ko"] .lede h2,html[lang="ja"] .lede h2,html[lang="zh"] .lede h2{font-weight:300}
.lede p+p{margin-top:16px}
.lede .stat{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px;padding-top:28px;border-top:1px solid var(--line)}
.lede .stat b{display:block;font-family:var(--en);font-size:clamp(24px,2.6vw,36px);font-weight:600;letter-spacing:-.02em;line-height:1}
.lede .stat span{display:block;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-top:8px;font-family:var(--en)}

.wide{position:relative;aspect-ratio:21/9;overflow:hidden;background:var(--bg-soft)}
.wide img{width:100%;height:100%;object-fit:cover;filter:saturate(.85)}

/* chapters */
.chap{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:clamp(32px,6vw,96px);padding:clamp(48px,7vw,96px) 0;border-top:1px solid var(--line)}
.chap:first-of-type{border-top:0}
.chap__img{position:relative;aspect-ratio:4/3;overflow:hidden;background:var(--bg-soft)}
.chap__img img{width:100%;height:100%;object-fit:cover;filter:saturate(.85);transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.chap:hover .chap__img img{transform:scale(1.04)}
.chap:nth-of-type(even) .chap__img{order:2}
.chap__txt .tag{font-family:var(--en);font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--red);font-weight:600;margin-bottom:12px}
.chap__txt h3{font-size:clamp(26px,3vw,40px);margin-bottom:18px;letter-spacing:-.02em}
html[lang="ko"] .chap__txt h3{font-weight:500}
.chap__txt p+p{margin-top:12px}
.chap__txt blockquote{margin-top:22px;padding-left:20px;border-left:2px solid var(--red);font-size:15.5px;color:var(--ink);font-style:italic}

/* gallery */
.gal{background:var(--ink);color:#fff;padding:clamp(64px,8vw,110px) 0}
.gal .eyebrow{color:#fff;opacity:.85}
.gal__head{margin-bottom:clamp(28px,4vw,48px)}
.gal__head p{color:rgba(255,255,255,.7)}
.gal__grid{display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(12px,1.6vw,22px)}
.g{display:block}
.g__img{aspect-ratio:1/1;overflow:hidden;background:#222}
.g__img img{width:100%;height:100%;object-fit:cover;filter:grayscale(.2) saturate(.85);transition:transform 1s cubic-bezier(.2,.7,.2,1)}
.g:hover .g__img img{transform:scale(1.05)}
.g__cap{margin-top:10px;font-size:13.5px;color:rgba(255,255,255,.75);line-height:1.4}
.g__cap b{display:block;font-family:var(--en);font-weight:600;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#fff;margin-bottom:3px}

/* timeline */
.tl{padding:clamp(64px,8vw,110px) 0}
.tl__head{margin-bottom:clamp(28px,4vw,48px)}
.tl ol{list-style:none;border-top:1px solid var(--ink)}
.tl li{display:grid;grid-template-columns:140px 1fr;gap:24px;padding:16px 0;border-bottom:1px solid var(--line);font-size:15px}
.tl li b{font-family:var(--en);font-weight:600;font-size:clamp(16px,1.3vw,19px);letter-spacing:-.01em;color:var(--ink);font-variant-numeric:tabular-nums}
.tl li.key b{color:var(--red)}
.tl li span{color:var(--ink-2);padding-top:2px}

/* next */
.next{background:var(--bg-soft);padding:clamp(56px,7vw,96px) 0}
.next__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.next a{display:block;background:var(--bg-soft);padding:32px 28px 36px;transition:background .25s}
.next a:hover{background:#fff}
.next .k{font-family:var(--en);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--red);font-weight:600;margin-bottom:16px}
.next h3{font-size:20px;margin-bottom:10px}
.next p{font-size:14.5px;margin-bottom:20px}

@media (max-width:1024px){.gal__grid{grid-template-columns:repeat(3,1fr)}.next__grid{grid-template-columns:1fr}}
@media (max-width:820px){
  .lede__grid,.chap{grid-template-columns:1fr;gap:24px}
  .chap:nth-of-type(even) .chap__img{order:0}
  .wide{aspect-ratio:16/10}
  .gal__grid{grid-template-columns:repeat(2,1fr)}
  .tl li{grid-template-columns:90px 1fr;gap:14px}
}
@media (max-width:560px){.lede .stat{grid-template-columns:1fr 1fr}.phero{height:70vh}}
"""

# ------------------------------------------------------------
# 갤러리: (이미지 파일명, 캡션 제목(en), 설명(ko,en,ja,zh))
# ------------------------------------------------------------
GALLERY = [
 ('young-alex-moulton-astride-a-scott-flying-squirrel-motorbike-circa-late-1930s.jpg','A young Alex Moulton',
  ('1931년식 스콧 TT 레플리카 모터사이클에 올라탄 젊은 알렉스, 1930년대 말','With his 1931 Scott TT Replica motorcycle, late 1930s','1931年製スコットTTレプリカに跨る若き日のアレックス、1930年代末','骑在 1931 年 Scott TT Replica 摩托车上的年轻亚历克斯，1930 年代末')),
 ('alex-moulton-working-at-bristol-aeroplane-company-second-world-war.jpg','Bristol Aeroplane Co.',
  ('2차 세계대전 중 브리스톨 에어로플레인 컴퍼니 엔진 연구부에서','In the Engine Research Department during the Second World War','第二次世界大戦中、ブリストル・エアロプレーン・カンパニーのエンジン研究部にて','二战期间在布里斯托飞机公司发动机研究部')),
 ('alex-moulton-and-alec-issigonis-by-hydrolastic-suspension-chart-1962.jpg','Alex & Alec Issigonis',
  ('하이드로라스틱 서스펜션 도표 앞에서, 모리스 1100 출시, 1962년','By the Hydrolastic suspension chart at the Morris 1100 launch, 1962','ハイドロラスティック・サスペンションの図表の前で、モーリス1100発表、1962年','在 Hydrolastic 避震图表前，Morris 1100 发布会，1962 年')),
 ('alex-moulton-with-brian-cottrell-in-moulton-drawing-office-1962.jpg','Moulton Design Development',
  ('몰튼 설계실에서 브라이언 코트렐과 함께, 1962년','With Brian Cottrell in the Moulton drawing office, 1962','モールトン設計室でブライアン・コットレルと、1962年','与 Brian Cottrell 在莫尔顿设计室，1962 年')),
 ('alex-moulton-with-first-new-bicycle-for-70-years-display-1962.jpg','The New Bike',
  ('"70년 만의 새로운 자전거" 전시와 함께, 1962년','With the "first new bicycle for 70 years" display, 1962','「70年ぶりの新しい自転車」の展示と共に、1962年','与"70 年来首款新型自行车"展示，1962 年')),
 ('alex-moulton-and-david-duffield-moulton-factory-1963.jpg','The New Factory',
  ('브래드퍼드 온 에이번의 새 공장에서 데이비드 더필드와 함께, 1963년','With David Duffield at the new Bradford-on-Avon factory, 1963','ブラッドフォード・オン・エイヴォンの新工場でデイヴィッド・ダフィールドと、1963年','与 David Duffield 在 Bradford-on-Avon 新工厂，1963 年')),
 ('alex-moulton-inspecting-a-moulton-mini-bike-circa-1960s.jpg','Production Inspection',
  ('몰튼 미니 자전거를 검수하는 모습, 1960년대','Inspecting a Moulton Mini bike, 1960s','モールトン・ミニを検査する様子、1960年代','检查一辆 Moulton Mini 自行车，1960 年代')),
 ('alex-moulton-outside-the-hall-astride-white-moulton-s-speed-circa-1960s.jpg','Moulton S Speed',
  ('홀 앞에서 흰색 몰튼 S 스피드에 올라, 1960년대','Astride a white Moulton S Speed outside The Hall, 1960s','ホールの前で白いモールトンSスピードに跨って、1960年代','在 The Hall 前骑着白色 Moulton S Speed，1960 年代')),
 ('alex-moulton-on-bmw-750-motorbike-1969.jpg','Alex\'s BMW 750',
  ('BMW 750 모터사이클 위에서, 1969년','On his BMW 750 motorcycle, 1969','BMW 750に乗って、1969年','骑在 BMW 750 摩托车上，1969 年')),
 ('alex-moulton-sitting-on-moulton-coach-during-testing-with-tony-best-circa-1970.jpg','The Moulton Coach',
  ('하이드라가스 서스펜션과 지오데틱 구조의 8륜 몰튼 코치 시험 중 토니 베스트와 함께, 1970년경','Testing the eight-wheeled Moulton Coach (Hydragas suspension, geodetic construction) with Tony Best, c. 1970','ハイドラガス・サスペンションとジオデティック構造の8輪モールトン・コーチの試験中、トニー・ベストと、1970年頃','与 Tony Best 测试八轮 Moulton Coach（Hydragas 避震、网格结构），约 1970 年')),
 ('alex-moulton-holding-car-and-bike-suspension-next-to-mini-cooper.jpg','Mini & Moulton Suspension',
  ('미니 쿠퍼 옆에서 자동차용과 자전거용 서스펜션을 들고','Holding car and bicycle suspension units beside a Mini Cooper','ミニ・クーパーの横で自動車用と自転車用のサスペンションを手に','在 Mini Cooper 旁手持汽车与自行车避震部件')),
 ('alex-moulton-testing-atb-bike-1988.jpg','AM-ATB',
  ('20인치 휠의 AM-ATB를 시험하는 모습, 1988년. 최초의 풀 서스펜션 산악자전거로 자주 꼽힘','Testing the 20-inch-wheeled AM-ATB, 1988, often regarded as the first full-suspension mountain bike','20インチホイールのAM-ATBを試験、1988年。最初のフルサスペンション・マウンテンバイクとしばしば言われる','测试 20 英寸轮径的 AM-ATB，1988 年，常被视为首款全避震山地车')),
 ('alex-moulton-working-on-moulton-pashley-apb-bike-circa-1992.jpg','All-Purpose-Bike',
  ('파슐리-몰튼 APB 작업 중, 1992년경','Working on the Pashley–Moulton APB, c. 1992','パシュレー・モールトンAPBの作業中、1992年頃','研制 Pashley–Moulton APB，约 1992 年')),
 ('alex-moulton-speed-stainless-toby-cat-2009.jpg','Alex, the SPEED and Toby',
  ('홀에서 스테인리스 스피드, 그리고 고양이 토비와 함께, 2009년','With the stainless SPEED and Toby the cat at The Hall, 2009','ホールでステンレスのSPEEDと猫のトビーと、2009年','在 The Hall 与不锈钢 SPEED 及猫咪 Toby，2009 年')),
]

# ------------------------------------------------------------
# 연표: (연도 표기, 내용(ko,en,ja,zh), 강조 여부)
# ------------------------------------------------------------
TIMELINE = [
 ('1920', ('4월 9일 출생','Born on 9 April','4月9日生まれ','4 月 9 日出生'), True),
 ('1939–45', ('브리스톨 에어로플레인 컴퍼니 엔진 연구부, 수석 엔지니어 로이 페든 경의 개인 조수로 2년','Engine Research Department, Bristol Aeroplane Company; two years as personal assistant to chief engineer Sir Roy Fedden','ブリストル・エアロプレーン・カンパニーのエンジン研究部で、主任技師ロイ・フェデン卿の個人助手を2年間','布里斯托飞机公司发动机研究部，担任总工程师 Roy Fedden 爵士的私人助理两年'), False),
 ('1945–', ('가업인 고무 회사 스펜서 몰튼에 입사, 기술 이사로 차량용 고무 서스펜션 연구부 설립','Joins the family rubber firm Spencer Moulton & Co. as technical director and sets up a research department for rubber vehicle suspension','家業のゴム会社スペンサー・モールトンに入社、技術取締役として車両用ゴムサスペンションの研究部門を設立','加入家族橡胶企业 Spencer Moulton & Co. 任技术总监，创立车辆橡胶避震研究部门'), False),
 ('1956', ('수에즈 위기의 석유 파동을 계기로 소구경 자전거 개발 시작','Begins developing a small-wheeled bicycle, prompted by the Suez Crisis oil shock','スエズ危機の石油ショックを契機に小径自転車の開発を開始','受苏伊士危机石油冲击启发，开始研发小轮径自行车'), True),
 ('1950s 말', ('가업을 에이번 러버에 매각, 몰튼 디벨롭먼트 설립. 알렉 이시고니스의 미니를 위한 서스펜션 설계','Family firm sold to Avon Rubber; founds Moulton Developments Ltd. Designs the suspension for Alec Issigonis\'s Mini','家業をエイヴォン・ラバーに売却、モールトン・ディベロップメントを設立。アレック・イシゴニスのミニのサスペンションを設計','家族企业出售给 Avon Rubber，创立 Moulton Developments。为 Alec Issigonis 的 Mini 设计避震系统'), False),
 ('1962', ('얼스 코트 사이클 쇼에서 첫 몰튼 자전거 발표. 같은 해 모리스 1100에 하이드로라스틱 서스펜션 적용','The first Moulton bicycle launches at the Earls Court Cycle Show. Hydrolastic suspension debuts on the Morris 1100','アールズ・コート・サイクルショーで最初のモールトン自転車を発表。同年、モーリス1100にハイドロラスティック・サスペンションを採用','首款莫尔顿自行车在 Earls Court 自行车展发布。同年 Hydrolastic 避震应用于 Morris 1100'), True),
 ('1963', ('브래드퍼드 온 에이번에 새 공장 설립','New factory at Bradford-on-Avon','ブラッドフォード・オン・エイヴォンに新工場を設立','在 Bradford-on-Avon 建立新工厂'), False),
 ('1966경', ('몰튼 S 스피드','Moulton S Speed','モールトンSスピード','Moulton S Speed'), False),
 ('1970경', ('하이드라가스 서스펜션과 지오데틱 구조의 8륜 몰튼 코치','Eight-wheeled Moulton Coach with Hydragas suspension and geodetic construction','ハイドラガス・サスペンションとジオデティック構造の8輪モールトン・コーチ','采用 Hydragas 避震与网格结构的八轮 Moulton Coach'), False),
 ('1976', ('대영제국 훈장(CBE) 수훈','Appointed CBE','大英帝国勲章（CBE）を受章','获颁大英帝国司令勋章（CBE）'), False),
 ('1977', ('알렉스 몰튼 자선 신탁 설립','Alex Moulton Charitable Trust established','アレックス・モールトン慈善信託を設立','成立亚历克斯·莫尔顿慈善信托'), False),
 ('1983', ('스페이스프레임 설계 스케치','Spaceframe design sketch','スペースフレームの設計スケッチ','空间车架设计草图'), True),
 ('1988', ('20인치 휠의 AM-ATB. 최초의 풀 서스펜션 산악자전거로 자주 꼽힘','AM-ATB with 20-inch wheels, often regarded as the first full-suspension mountain bike','20インチホイールのAM-ATB。最初のフルサスペンション・マウンテンバイクとしばしば言われる','20 英寸轮径的 AM-ATB，常被视为首款全避震山地车'), False),
 ('1992', ('파슐리-몰튼 APB','Pashley–Moulton APB','パシュレー・モールトンAPB','Pashley–Moulton APB'), False),
 ('2009', ('스피드(SPEED) 출시','SPEED released','SPEEDを発表','SPEED 发布'), False),
 ('2012', ('12월 9일 별세','Died on 9 December','12月9日逝去','12 月 9 日逝世'), True),
]

def gallery():
    out = []
    for img, title, cap in GALLERY:
        out.append(f"""
      <figure class="g">
        <div class="g__img"><img data-src="{img}" alt="{title}" loading="lazy"></div>
        <figcaption class="g__cap"><b>{title}</b><span {t(*cap)}>{cap[0]}</span></figcaption>
      </figure>""")
    return ''.join(out)

def timeline():
    out = []
    for yr, txt, key in TIMELINE:
        cls = ' class="key"' if key else ''
        out.append(f'<li{cls}><b>{yr}</b><span {t(*txt)}>{txt[0]}</span></li>')
    return ''.join(out)

def main():
    return f"""
<main id="top">

<section class="phero">
  <img data-src="dr-alex-moulton-working-at-his-desk-landscape.jpg" alt="Dr Alex Moulton at his desk" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow" {t('위대한 영국의 엔지니어','A Great British Engineer','偉大な英国のエンジニア','伟大的英国工程师')}>위대한 영국의 엔지니어</div>
    <h1 {t('알렉스 몰튼 박사','Dr Alex Moulton','アレックス・モールトン博士','亚历克斯·莫尔顿博士')}>알렉스 몰튼 박사</h1>
    <div class="dates">CBE RDI FEng · 1920 – 2012</div>
    <p {t('서스펜션 설계로 세계에 이름을 알린 영국의 엔지니어이자 발명가. 미니의 서스펜션을 만들었고, 1962년 몰튼 자전거로 자전거의 역사를 바꿨습니다.',
         'An English engineer and inventor known internationally for suspension design. He created the suspension of the Mini and, in 1962, changed the history of the bicycle with the Moulton.',
         'サスペンション設計で世界に名を知られた英国のエンジニアであり発明家。ミニのサスペンションを生み出し、1962年にはモールトン自転車で自転車の歴史を変えました。',
         '以避震设计享誉国际的英国工程师与发明家。他创造了 Mini 的避震系统，并于 1962 年以莫尔顿自行车改写了自行车的历史。')}>서스펜션 설계로 세계에 이름을 알린 영국의 엔지니어이자 발명가. 미니의 서스펜션을 만들었고, 1962년 몰튼 자전거로 자전거의 역사를 바꿨습니다.</p>
  </div>
</section>

<section class="lede">
  <div class="wrap lede__grid rv">
    <div>
      <div class="eyebrow">Dr Alex Moulton CBE RDI FEng</div>
      <h2 {t('고무, 서스펜션, 그리고 작은 바퀴','Rubber, suspension and small wheels','ゴム、サスペンション、そして小さな車輪','橡胶、避震与小轮径')}>고무, 서스펜션, 그리고 작은 바퀴</h2>
    </div>
    <div>
      <p {t('알렉스 몰튼(1920년 4월 9일 ~ 2012년 12월 9일)은 고무 산업의 선구자 스티븐 몰튼의 증손자로 태어났습니다. 말버러와 케임브리지 킹스 칼리지에서 공부해 공학 학위를 받았습니다.',
           'Alex Moulton (9 April 1920 – 9 December 2012) was the great-grandson of rubber pioneer Stephen Moulton. He was educated at Marlborough and at King\'s College, Cambridge, where he graduated in engineering.',
           'アレックス・モールトン（1920年4月9日〜2012年12月9日）は、ゴム産業の先駆者スティーブン・モールトンの曾孫として生まれました。マールボロとケンブリッジのキングス・カレッジで学び、工学の学位を取得しました。',
           '亚历克斯·莫尔顿（1920 年 4 月 9 日 – 2012 年 12 月 9 日）是橡胶业先驱 Stephen Moulton 的曾孙。他先后就读于 Marlborough 与剑桥国王学院，获工程学位。')}>알렉스 몰튼(1920년 4월 9일 ~ 2012년 12월 9일)은 고무 산업의 선구자 스티븐 몰튼의 증손자로 태어났습니다. 말버러와 케임브리지 킹스 칼리지에서 공부해 공학 학위를 받았습니다.</p>
      <p {t('2차 세계대전 중에는 브리스톨 에어로플레인 컴퍼니 엔진 연구부에서 수석 엔지니어 로이 페든 경의 개인 조수로 2년을 일했습니다. 전쟁이 끝난 뒤 가업인 고무 회사 스펜서 몰튼에 입사해 기술 이사가 되었고, 차량용 고무 서스펜션 시스템을 연구하는 부서를 세웠습니다.',
           'During the Second World War he spent two years in the Engine Research Department of the Bristol Aeroplane Company as personal assistant to chief engineer Sir Roy Fedden. After the war he joined the family rubber firm, Spencer Moulton & Co., becoming technical director and setting up a research department for rubber vehicle suspension systems.',
           '第二次世界大戦中はブリストル・エアロプレーン・カンパニーのエンジン研究部で、主任技師ロイ・フェデン卿の個人助手として2年間働きました。戦後は家業のゴム会社スペンサー・モールトンに入社して技術取締役となり、車両用ゴムサスペンションシステムの研究部門を設立しました。',
           '二战期间，他在布里斯托飞机公司发动机研究部担任总工程师 Roy Fedden 爵士的私人助理两年。战后加入家族橡胶企业 Spencer Moulton & Co.，任技术总监，并创立了车辆橡胶避震系统研究部门。')}>2차 세계대전 중에는 브리스톨 에어로플레인 컴퍼니 엔진 연구부에서 수석 엔지니어 로이 페든 경의 개인 조수로 2년을 일했습니다. 전쟁이 끝난 뒤 가업인 고무 회사 스펜서 몰튼에 입사해 기술 이사가 되었고, 차량용 고무 서스펜션 시스템을 연구하는 부서를 세웠습니다.</p>
      <div class="stat">
        <div><b>1962</b><span {t('첫 몰튼 자전거','First Moulton Bicycle','最初のモールトン自転車','首款莫尔顿自行车')}>첫 몰튼 자전거</span></div>
        <div><b>CBE</b><span {t('1976년 수훈','Appointed 1976','1976年受章','1976 年获颁')}>1976년 수훈</span></div>
        <div><b>92</b><span {t('생애','Years','年の生涯','岁')}>생애</span></div>
      </div>
    </div>
  </div>
</section>

<div class="wide rv"><img data-src="mini-motor-car-cornering-on-race-track-1950s.jpg" alt="Mini cornering on a race track, 1950s" loading="lazy"></div>

<section class="chaps">
  <div class="wrap">
    <article class="chap rv">
      <div class="chap__img"><img data-src="dr-alex-moulton-standing-beside-grey-car-with-series-1-billiard-cue-f-frame.jpg" alt="Alex Moulton beside a car with a Series 1 F-frame" loading="lazy"></div>
      <div class="chap__txt">
        <div class="tag">01 · Small Wheels, Smart Suspension</div>
        <h3 {t('작은 바퀴, 영리한 서스펜션','Small wheels, smart suspension','小さな車輪、賢いサスペンション','小轮径，聪明的避震')}>작은 바퀴, 영리한 서스펜션</h3>
        <p {t('1950년대 말 가업이 에이번 러버에 매각되자, 몰튼은 차량 설계와 서스펜션에 집중하기 위해 몰튼 디벨롭먼트를 설립했습니다.',
             'In the late 1950s the family business was sold to Avon Rubber, and Moulton founded Moulton Developments Limited to focus on vehicle design and suspension.',
             '1950年代末に家業がエイヴォン・ラバーに売却されると、モールトンは車両設計とサスペンションに集中するためモールトン・ディベロップメントを設立しました。',
             '1950 年代末，家族企业出售给 Avon Rubber，莫尔顿随即创立 Moulton Developments，专注于车辆设计与避震。')}>1950년대 말 가업이 에이번 러버에 매각되자, 몰튼은 차량 설계와 서스펜션에 집중하기 위해 몰튼 디벨롭먼트를 설립했습니다.</p>
        <p {t('그는 친구 알렉 이시고니스 경이 설계한 오스틴 미니의 서스펜션을 설계하고 개발해 생산했습니다. 원뿔형 고무 스프링과 작은 바퀴는 미니의 콤팩트한 크기를 가능하게 한 핵심이었습니다.',
             'He designed, developed and produced the suspension for the Austin Mini, designed by his friend Sir Alec Issigonis. Conical rubber springs and small wheels were key to making the Mini\'s compact size possible.',
             '彼は友人のアレック・イシゴニス卿が設計したオースチン・ミニのサスペンションを設計・開発・生産しました。円錐形のゴムスプリングと小さな車輪は、ミニのコンパクトなサイズを可能にした鍵でした。',
             '他为好友 Alec Issigonis 爵士设计的 Austin Mini 设计、研发并生产了避震系统。锥形橡胶弹簧与小轮径是 Mini 得以如此紧凑的关键。')}>그는 친구 알렉 이시고니스 경이 설계한 오스틴 미니의 서스펜션을 설계하고 개발해 생산했습니다. 원뿔형 고무 스프링과 작은 바퀴는 미니의 콤팩트한 크기를 가능하게 한 핵심이었습니다.</p>
      </div>
    </article>

    <article class="chap rv">
      <div class="chap__img"><img data-src="moulton-1983-sketch-spaceframe.jpg" alt="Alex Moulton's 1983 spaceframe sketch" loading="lazy"></div>
      <div class="chap__txt">
        <div class="tag">02 · Engineering a Cycling Revolution</div>
        <h3 {t('자전거의 혁명을 설계하다','Engineering a cycling revolution','自転車の革命を設計する','设计一场自行车革命')}>자전거의 혁명을 설계하다</h3>
        <p {t('1956년, 수에즈 위기의 석유 파동과 자동차 분야의 경험을 계기로 몰튼은 소구경 자전거 개발을 시작했습니다. 첫 몰튼 자전거는 1962년 얼스 코트 사이클 쇼에서 세상에 공개되었습니다.',
             'In 1956, prompted by the Suez Crisis oil shock and his automotive work, Moulton began developing a small-wheeled bicycle. The first Moulton bicycle was launched at the Earls Court Cycle Show in 1962.',
             '1956年、スエズ危機の石油ショックと自動車分野での経験を契機に、モールトンは小径自転車の開発を始めました。最初のモールトン自転車は1962年のアールズ・コート・サイクルショーで公開されました。',
             '1956 年，受苏伊士危机石油冲击与汽车领域经验的启发，莫尔顿开始研发小轮径自行车。首款莫尔顿自行车于 1962 年在 Earls Court 自行车展上面世。')}>1956년, 수에즈 위기의 석유 파동과 자동차 분야의 경험을 계기로 몰튼은 소구경 자전거 개발을 시작했습니다. 첫 몰튼 자전거는 1962년 얼스 코트 사이클 쇼에서 세상에 공개되었습니다.</p>
        <p {t('그의 목표는 19세기 말 영국에서 스탈리 등이 완성한 큰 바퀴의 다이아몬드 프레임 자전거를 넘어서는 것이었습니다. 몰튼 F-프레임은 풀사이즈 자전거에도 작은 바퀴를 쓸 수 있음을 증명했고, 출시 때부터 앞뒤 서스펜션을 갖추고 있었습니다.',
             'His aim was to improve on the classic large-wheeled diamond-frame bicycle, a design dating back to Starley and others in late-19th-century England. The Moulton F-frame proved that a full-size bicycle could have small wheels, and it has had front and rear suspension since launch.',
             '彼の目標は、19世紀末の英国でスターレーらが完成させた大径ホイールのダイヤモンドフレーム自転車を超えることでした。モールトンFフレームはフルサイズの自転車にも小さな車輪が使えることを証明し、発売当初から前後サスペンションを備えていました。',
             '他的目标是超越 19 世纪末由 Starley 等人在英国定型的大轮径菱形车架自行车。莫尔顿 F 型车架证明了全尺寸自行车也可以采用小轮径，并自推出之日起就配备前后避震。')}>그의 목표는 19세기 말 영국에서 스탈리 등이 완성한 큰 바퀴의 다이아몬드 프레임 자전거를 넘어서는 것이었습니다. 몰튼 F-프레임은 풀사이즈 자전거에도 작은 바퀴를 쓸 수 있음을 증명했고, 출시 때부터 앞뒤 서스펜션을 갖추고 있었습니다.</p>
        <p {t('몰튼 자전거는 이후 끊임없이 다듬어져 20세기 자전거 설계의 가장 중요한 진보 가운데 하나로 평가받습니다.',
             'Continually refined ever since, the Moulton bicycle is regarded as one of the most significant advances in bicycle design of the 20th century.',
             'モールトン自転車はその後も絶えず磨き上げられ、20世紀の自転車設計における最も重要な進歩の一つと評価されています。',
             '此后莫尔顿自行车不断精进，被视为 20 世纪自行车设计最重要的进步之一。')}>몰튼 자전거는 이후 끊임없이 다듬어져 20세기 자전거 설계의 가장 중요한 진보 가운데 하나로 평가받습니다.</p>
      </div>
    </article>

    <article class="chap rv">
      <div class="chap__img"><img data-src="alex-moulton-outside-the-hall-astride-white-moulton-s-speed-circa-1960s.jpg" alt="Alex Moulton on a Moulton S Speed outside The Hall" loading="lazy"></div>
      <div class="chap__txt">
        <div class="tag">03 · The Spirit of Moulton</div>
        <h3 {t('몰튼의 정신','The spirit of Moulton','モールトンの精神','莫尔顿精神')}>몰튼의 정신</h3>
        <p {t('몰튼은 엔지니어링이 인간의 경험을 더 낫게 만들어야 한다고 믿었습니다. 브리지스톤과의 인연을 통해, 사물에는 설계와 장인정신, 쓰임새를 통해 드러나는 정신이 깃들어 있다는 일본의 생각에 영향을 받았습니다.',
             'Moulton believed engineering should improve the human experience. Through his association with Bridgestone he was influenced by the Japanese idea that objects have a spirit, revealed through their design, craftsmanship and purpose.',
             'モールトンは、エンジニアリングは人間の経験をより良くすべきだと信じていました。ブリヂストンとの縁を通じて、物には設計、職人技、用途を通して現れる精神が宿るという日本の考え方に影響を受けました。',
             '莫尔顿相信工程应当改善人的体验。通过与普利司通的合作，他受到日本观念的影响：物件自有其精神，通过设计、工艺与用途得以显现。')}>몰튼은 엔지니어링이 인간의 경험을 더 낫게 만들어야 한다고 믿었습니다. 브리지스톤과의 인연을 통해, 사물에는 설계와 장인정신, 쓰임새를 통해 드러나는 정신이 깃들어 있다는 일본의 생각에 영향을 받았습니다.</p>
        <p {t('그는 무언가를 잘 만드는 일은 도덕적으로 보람 있는 일이며, 이익이 성실함과 정성, 쓰는 즐거움보다 앞서서는 안 된다고 여겼습니다. 1976년 CBE를 받았고, 이후로도 엔지니어링 설계와 교육에 힘썼습니다. 1977년에는 알렉스 몰튼 자선 신탁을 세웠습니다.',
             'He held that making things well is morally rewarding, and that profit should never outweigh integrity, care and the enjoyment of use. Appointed CBE in 1976, he remained active in engineering design and education, and established the Alex Moulton Charitable Trust in 1977.',
             '彼は、物をよく作ることは道徳的に報われる仕事であり、利益が誠実さ、丁寧さ、使う喜びより優先されてはならないと考えました。1976年にCBEを受章し、その後もエンジニアリング設計と教育に力を注ぎました。1977年にはアレックス・モールトン慈善信託を設立しました。',
             '他认为把东西做好在道德上是值得的，利润永远不应凌驾于诚信、用心与使用的乐趣之上。1976 年获颁 CBE 后，他仍活跃于工程设计与教育，并于 1977 年成立亚历克斯·莫尔顿慈善信托。')}>그는 무언가를 잘 만드는 일은 도덕적으로 보람 있는 일이며, 이익이 성실함과 정성, 쓰는 즐거움보다 앞서서는 안 된다고 여겼습니다. 1976년 CBE를 받았고, 이후로도 엔지니어링 설계와 교육에 힘썼습니다. 1977년에는 알렉스 몰튼 자선 신탁을 세웠습니다.</p>
      </div>
    </article>
  </div>
</section>

<section class="gal">
  <div class="wrap">
    <div class="gal__head rv">
      <div class="eyebrow" {t('AM 갤러리','AM Gallery','AMギャラリー','AM 影像集')}>AM 갤러리</div>
      <h2 {t('사진으로 보는 알렉스 몰튼','Alex Moulton in pictures','写真で見るアレックス・モールトン','影像中的亚历克斯·莫尔顿')}>사진으로 보는 알렉스 몰튼</h2>
    </div>
    <div class="gal__grid rv">{gallery()}
    </div>
  </div>
</section>

<section class="tl">
  <div class="wrap">
    <div class="tl__head rv">
      <div class="eyebrow" {t('연표','Timeline','年表','年表')}>연표</div>
      <h2 {t('1920년부터 2012년까지','From 1920 to 2012','1920年から2012年まで','从 1920 年到 2012 年')}>1920년부터 2012년까지</h2>
    </div>
    <ol class="rv">{timeline()}</ol>
  </div>
</section>

<section class="next">
  <div class="wrap">
    <div class="next__grid rv">
      <a href="/the-hall/">
        <div class="k">Where it all began</div>
        <h3 {t('홀 에스테이트','The Hall Estate','ホール・エステート','The Hall 庄园')}>홀 에스테이트</h3>
        <p {t('브래드퍼드 온 에이번의 몰튼 가문 저택이자 지금도 몰튼이 만들어지는 곳.','The Moulton family home in Bradford-on-Avon, where Moultons are still made today.','ブラッドフォード・オン・エイヴォンのモールトン家の邸宅であり、今もモールトンが作られる場所。','位于 Bradford-on-Avon 的莫尔顿家族宅邸，至今仍是莫尔顿的制造之地。')}>브래드퍼드 온 에이번의 몰튼 가문 저택이자 지금도 몰튼이 만들어지는 곳.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
      <a href="/design/">
        <div class="k">Heritage</div>
        <h3 {t('디자인의 진화','Design Evolution','デザインの進化','设计演进')}>디자인의 진화</h3>
        <p {t('1962년 F-프레임에서 스페이스프레임까지, 몰튼 설계가 걸어온 길.','From the 1962 F-frame to the spaceframe: the path of Moulton design.','1962年のFフレームからスペースフレームまで、モールトン設計が歩んだ道。','从 1962 年的 F 型车架到空间车架：莫尔顿设计的演进之路。')}>1962년 F-프레임에서 스페이스프레임까지, 몰튼 설계가 걸어온 길.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
      <a href="/about-moulton/">
        <div class="k">The Bike</div>
        <h3 {t('몰튼 자전거','The Moulton Bike','モールトンの自転車','莫尔顿自行车')}>몰튼 자전거</h3>
        <p {t('스페이스프레임, 작은 바퀴, 서스펜션, 분리형 프레임, 스틸. 몰튼의 설계와 엔지니어링.','Spaceframe, small wheels, suspension, separability and steel: the design and engineering of the Moulton.','スペースフレーム、小径ホイール、サスペンション、分割フレーム、スチール。モールトンの設計とエンジニアリング。','空间车架、小轮径、避震、可分离车架与钢材：莫尔顿的设计与工程。')}>스페이스프레임, 작은 바퀴, 서스펜션, 분리형 프레임, 스틸. 몰튼의 설계와 엔지니어링.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
    </div>
  </div>
</section>

</main>
"""
