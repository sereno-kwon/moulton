# -*- coding: utf-8 -*-
"""/racing 페이지 본문 (UK 'Records & Racing' 페이지 번역). build.py가 읽어 racing/index.html 생성.
   기록은 F_FRAME / SPACEFRAME 목록: (연도, 이미지, 제목(ko,en,ja,zh), 본문(ko,en,ja,zh))"""
from build import t

SLUG = 'racing'
TITLE_KO = '몰튼 레이싱 & 기록 | Moulton Bicycles Korea'
TITLES_JS = "{ko:'몰튼 레이싱 & 기록 | Moulton Bicycles Korea', en:'Records & Racing | Moulton Bicycles Korea', ja:'モールトン レース＆記録 | Moulton Bicycles Korea', zh:'莫尔顿竞速与纪录 | Moulton Bicycles Korea'}"
DESCRIPTION = '1962년 카디프~런던 기록부터 시속 82.54km의 세계 속도 기록, 레이스 어크로스 아메리카, 파리~브레스트~파리까지. 몰튼의 레이싱 역사.'
OG_TITLE = 'Records & Racing | Moulton Bicycles Korea'
OG_DESC = 'From the 1962 Cardiff–London record to a world speed record and the Race Across America.'

CSS = """
/* ===== Racing page ===== */
.eyebrow{font-size:14px;letter-spacing:.18em;margin-bottom:16px}
.phero{position:relative;height:min(78vh,760px);min-height:460px;overflow:hidden;background:#161616}
.phero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 35%;filter:saturate(.8)}
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
.lede .stat b{display:block;font-family:var(--en);font-size:clamp(22px,2.4vw,34px);font-weight:600;letter-spacing:-.02em;line-height:1;font-variant-numeric:tabular-nums}
.lede .stat b small{font-size:.5em;font-weight:400;margin-left:3px}
.lede .stat span{display:block;font-size:13px;letter-spacing:.1em;color:var(--ink-3);margin-top:8px;line-height:1.4}

.wide{position:relative;aspect-ratio:21/9;overflow:hidden;background:var(--bg-soft)}
.wide img{width:100%;height:100%;object-fit:cover;filter:saturate(.85)}

/* era */
.era{padding:clamp(64px,8vw,110px) 0}
.era__head{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:end;margin-bottom:clamp(32px,5vw,56px);padding-bottom:22px;border-bottom:1px solid var(--ink)}
.era__head .yrs{font-family:var(--en);font-size:14px;letter-spacing:.14em;color:var(--ink-3);margin-top:10px}
.era__head p{font-size:15px}
.sil{display:flex;gap:clamp(16px,3vw,48px);justify-content:flex-end;align-items:center}
.sil img{width:min(46%,260px);height:auto;opacity:.85}
.recs{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(32px,4vw,56px) clamp(24px,3vw,48px)}
.rec__img{position:relative;aspect-ratio:4/3;overflow:hidden;background:var(--bg-soft)}
.rec__img img{width:100%;height:100%;object-fit:cover;filter:saturate(.85);transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.rec:hover .rec__img img{transform:scale(1.04)}
.rec__yr{position:absolute;left:0;bottom:0;background:var(--ink);color:#fff;font-family:var(--en);font-weight:600;font-size:15px;letter-spacing:.06em;padding:9px 14px}
.rec h3{font-size:clamp(20px,1.8vw,24px);margin:20px 0 10px;letter-spacing:-.01em}
html[lang="ko"] .rec h3{font-weight:500}
.rec p{font-size:15px}
.rec .fig{display:inline-block;margin-top:14px;font-family:var(--en);font-weight:600;font-size:13px;letter-spacing:.08em;color:var(--red);border-top:1px solid var(--red);padding-top:8px}

.era.dark{background:var(--ink);color:#fff}
.era.dark .era__head{border-bottom-color:rgba(255,255,255,.3)}
.era.dark .era__head p,.era.dark .rec p{color:rgba(255,255,255,.72)}
.era.dark .era__head .yrs{color:rgba(255,255,255,.55)}
.era.dark .eyebrow{color:#ff5a6e}
.era.dark .rec__img{background:#222}
.era.dark .rec__yr{background:#fff;color:var(--ink)}
.era.dark .sil img{filter:invert(1);opacity:.75}
.era.dark .rec .fig{color:#ff5a6e;border-color:#ff5a6e}

/* next */
.next{background:var(--bg-soft);padding:clamp(56px,7vw,96px) 0}
.next__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.next a{display:block;background:var(--bg-soft);padding:32px 28px 36px;transition:background .25s}
.next a:hover{background:#fff}
.next .k{font-family:var(--en);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--red);font-weight:600;margin-bottom:16px}
.next h3{font-size:20px;margin-bottom:10px}
.next p{font-size:14.5px;margin-bottom:20px}

@media (max-width:1024px){.next__grid{grid-template-columns:1fr}}
@media (max-width:820px){
  .lede__grid,.era__head{grid-template-columns:1fr;gap:20px}
  .era__head{align-items:start}
  .sil{justify-content:flex-start}
  .recs{grid-template-columns:1fr}
  .wide{aspect-ratio:16/10}
}
@media (max-width:560px){.lede .stat{grid-template-columns:1fr}.phero{height:70vh}}
"""

# ------------------------------------------------------------
# (연도, 이미지, 제목(ko,en,ja,zh), 본문(ko,en,ja,zh), 핵심 수치 또는 '')
# ------------------------------------------------------------
F_FRAME = [
 ('1962','john-woodburn-with-alex-moulton-cardiff-london-record-9th-dec-1962.jpg',
  ('존 우드번, 카디프~런던 기록','John Woodburn Record','ジョン・ウッドバーン、カーディフ〜ロンドン記録','John Woodburn 卡迪夫至伦敦纪录'),
  ('출시 한 달 만에 존 우드번이 몰튼 스피드로 카디프~런던 기록을 18분 31초 앞당겼습니다. 162마일(약 261km)을 6시간 43분 29초, 평균 시속 약 24마일로 달렸습니다.',
   'One month after launch, John Woodburn broke the Cardiff–London record on a Moulton Speed by 18 min 31 s, covering 162 miles (261 km) in 6:43:29, an average of about 24 mph.',
   '発売からわずか1か月後、ジョン・ウッドバーンがモールトン・スピードでカーディフ〜ロンドン記録を18分31秒更新しました。162マイル（約261km）を6時間43分29秒、平均時速約24マイルで走りました。',
   '上市仅一个月，John Woodburn 便骑莫尔顿 Speed 将卡迪夫至伦敦纪录缩短 18 分 31 秒，以 6 小时 43 分 29 秒完成 162 英里（约 261 公里），平均时速约 24 英里。'),
  '162 mi · 6:43:29'),
 ('1963','4-man-pursuit-team-on-moulton-bikes-coventry-race-track-1963.jpg',
  ('코번트리 더 버츠 트랙','The Butts, Coventry','コヴェントリー、ザ・バッツ','考文垂 The Butts 赛道'),
  ('몰튼을 탄 코번트리 사이클링 클럽 4인 추발팀이 4,000m 단체 추발에서 클럽 기록을 경신하며, 일반 바퀴 자전거를 탄 레스터 팀을 큰 차이로 이겼습니다.',
   'A four-man Coventry Cycling Club pursuit team on Moultons broke the club record over 4,000 m, beating a conventional-wheeled Leicester team by a clear margin.',
   'モールトンに乗ったコヴェントリー・サイクリングクラブの4人チームが4,000m団体追い抜きでクラブ記録を更新し、通常ホイールのレスター・チームに大差で勝利しました。',
   '骑莫尔顿的考文垂自行车俱乐部四人追逐赛车队在 4,000 米团体追逐赛中刷新俱乐部纪录，并以明显优势击败使用常规轮径的莱斯特车队。'),
  '4,000 m pursuit'),
 ('1963','tom-simpson-cyclist-moulton-speed-bike-herne-hill-london-1963.jpg',
  ('톰 심슨','Tom Simpson','トム・シンプソン','Tom Simpson'),
  ('런던 허니 힐 벨로드롬에서 몰튼 스피드를 시승한 톰 심슨은 이 자전거로 레이스에 나가겠다고 말했습니다. 하지만 그는 푸조와 계약된 몸이었습니다.',
   'After test riding a Moulton Speed at Herne Hill velodrome in London, Tom Simpson said he would race it. He was, however, under contract to Peugeot.',
   'ロンドンのハーンヒル・ヴェロドロームでモールトン・スピードに試乗したトム・シンプソンは、これでレースに出たいと語りました。しかし彼はプジョーと契約中でした。',
   '在伦敦 Herne Hill 赛车场试骑莫尔顿 Speed 后，Tom Simpson 表示愿意骑它参赛，但当时他已与标致签约。'),
  ''),
 ('1965–67','vic-nicholson-cardiff-to-london-record-on-moulton-speedsix-bike-1965.jpg',
  ('빅 니콜슨의 승리','Vic Nicholson Wins','ヴィック・ニコルソンの勝利','Vic Nicholson 的胜利'),
  ('빅 니콜슨은 1965년 스피드식스로 주요 타임 트라이얼 15개 대회에서 우승했습니다. 1967년에는 세번 브리지 경로로 런던~카디프 기록을 되찾았는데, 151마일을 6시간 14분 54초에 달려 3개월 전 브라이언 캣이 세운 기록을 18분 가까이 앞당겼습니다.',
   'Vic Nicholson won 15 major time trials on the Speedsix in 1965. In 1967 he reclaimed the London–Cardiff record over the Severn Bridge route, covering 151 miles in 6:14:54, nearly 18 minutes faster than Brian Catt’s three-month-old record.',
   'ヴィック・ニコルソンは1965年、スピードシックスで主要タイムトライアル15大会に優勝しました。1967年にはセヴァーン橋ルートでロンドン〜カーディフ記録を奪還し、151マイルを6時間14分54秒で走って、3か月前のブライアン・キャットの記録を18分近く更新しました。',
   'Vic Nicholson 于 1965 年骑 Speedsix 赢得 15 场重要计时赛。1967 年他经塞文桥路线夺回伦敦至卡迪夫纪录，以 6 小时 14 分 54 秒完成 151 英里，比 Brian Catt 三个月前的纪录快近 18 分钟。'),
  '151 mi · 6:14:54'),
 ('1978','daved-sanders-paris-harrogate-medal-1978-moulton.jpg',
  ('파리~해러게이트 51시간','Paris to Harrogate in 51 Hours','パリ〜ハロゲート51時間','巴黎至哈罗盖特 51 小时'),
  ('데이브드 샌더스는 몰튼 MKIII로 800km 센테너리 라이드를 51시간 만에 완주했습니다. 공식 거리 531마일, 출전자 108명 중 완주자는 32명이었습니다.',
   'Daved Sanders completed the 800 km Centenary Ride on a Moulton MKIII in 51 hours, officially 531 miles. He was one of 32 finishers from 108 entries.',
   'デイヴド・サンダースはモールトンMKIIIで800kmのセンテナリー・ライドを51時間で完走しました。公式距離531マイル、108人の出走者のうち完走者は32人でした。',
   'Daved Sanders 骑莫尔顿 MKIII 以 51 小时完成 800 公里百年纪念骑行，官方距离 531 英里，108 名参赛者中仅 32 人完赛。'),
  '531 mi · 51 h'),
]

SPACEFRAME = [
 ('1984','elgar-vaivars-toronto-criterium-am7-moulton-bike-1984.jpg',
  ('AM7을 탄 엘가','Elgar on AM7','AM7に乗るエルガー','骑 AM7 的 Elgar'),
  ('엘가 바이바스는 1984년 6월 20일 토론토에서 열린 30마일 베롤리나 CC 크리테리움에서 우승했습니다.',
   'Elgar Vaivars won the 30-mile Berolina CC Criterium in Toronto on 20 June 1984.',
   'エルガー・ヴァイヴァースは1984年6月20日、トロントで開催された30マイルのベロリナCCクリテリウムで優勝しました。',
   'Elgar Vaivars 于 1984 年 6 月 20 日在多伦多赢得 30 英里的 Berolina CC 绕圈赛。'),
  ''),
 ('1985–86','jim-glover-world-speed-record-moulton-am-speed-with-fairing-1986.jpg',
  ('세계 속도 기록','World Speed Record','世界速度記録','世界速度纪录'),
  ('국제 인력 속도 선수권에서 짐 글로버는 1985년 가을 200m 플라잉 스타트 기록 시속 50.21마일을 세웠고, 1986년 8월 29일 더그 밀리컨의 페어링을 단 AM 스피드로 시속 51.29마일(82.54km)까지 끌어올렸습니다. 일반적인 승차 자세 기준으로는 지금도 깨지지 않은 기록입니다.',
   'At the International Human Powered Speed Championships, Jim Glover set a 200 m flying-start record of 50.21 mph in autumn 1985. On 29 August 1986 he raised it to 51.29 mph (82.54 km/h) on an AM SPEED with a fairing by Doug Milliken, a record that still stands for the conventional riding position.',
   '国際人力速度選手権でジム・グローバーは1985年秋、200mフライングスタートで時速50.21マイルの記録を樹立。1986年8月29日にはダグ・ミリケンのフェアリングを付けたAMスピードで時速51.29マイル（82.54km）に更新しました。通常の乗車姿勢では今も破られていない記録です。',
   '在国际人力速度锦标赛上，Jim Glover 于 1985 年秋创下 200 米飞行起步时速 50.21 英里的纪录；1986 年 8 月 29 日，他骑装有 Doug Milliken 整流罩的 AM SPEED 将其提升至时速 51.29 英里（82.54 公里）。以常规骑姿而言，这一纪录至今未被打破。'),
  '82.54 km/h'),
 ('1987–88','dave-bogdan-raam-1988-moulton-am-speed-bike.jpg',
  ('레이스 어크로스 아메리카','Race Across America','レース・アクロス・アメリカ','横穿美国赛（RAAM）'),
  ('데이브 보그던은 1987년 양산 전 AM 주빌리로 RAAM을 11일 8시간 2분에 완주했습니다. 1988년에는 AM 스피드 프로토타입으로 10일 15시간 1분까지 기록을 줄이며 출전자 35명 중 8위에 올랐습니다.',
   'Dave Bogdan rode RAAM in 1987 on a pre-production AM-Jubilee in 11 days, 8 h, 2 min. In 1988 he improved to 10 days, 15 h, 1 min on a prototype AM SPEED, finishing 8th of 35 starters.',
   'デイヴ・ボグダンは1987年、量産前のAMジュビリーでRAAMを11日8時間2分で完走。1988年にはAMスピードのプロトタイプで10日15時間1分に短縮し、35人中8位に入りました。',
   'Dave Bogdan 于 1987 年骑预量产 AM-Jubilee 以 11 天 8 小时 2 分完成 RAAM；1988 年骑 AM SPEED 原型车将成绩提升至 10 天 15 小时 1 分，在 35 名出发者中名列第 8。'),
  '10 d 15 h 1 min'),
 ('1990','richard-grigsby-fowey-triathlon-1990-moulton-am-speed-bike.jpg',
  ('리처드 그릭스비','Richard Grigsby','リチャード・グリグスビー','Richard Grigsby'),
  ('배스 사이클링 클럽 소속으로 AM 스피드를 탄 리처드 그릭스비는 출전자 180명의 포위 트라이애슬론에서 우승했고, 킹스우드 트라이애슬론 사이클 구간에서는 3위를 기록했습니다.',
   'Riding an AM SPEED for Bath Cycling Club, Richard Grigsby won the Fowey Triathlon from 180 starters and took third in the cycling split of the Kingswood Triathlon.',
   'バース・サイクリングクラブ所属でAMスピードに乗ったリチャード・グリグスビーは、180人が出走したフォーイ・トライアスロンで優勝し、キングスウッド・トライアスロンのバイクパートで3位に入りました。',
   '代表巴斯自行车俱乐部骑 AM SPEED 的 Richard Grigsby 在 180 人参赛的 Fowey 铁人三项中夺冠，并在 Kingswood 铁人三项骑行赛段获得第三。'),
  '1st / 180'),
 ('2003','chloe-williams-moulton-ns-speed-bike-pbp-2003.jpg',
  ('파리~브레스트~파리','Paris–Brest–Paris','パリ〜ブレスト〜パリ','巴黎-布雷斯特-巴黎'),
  ('NS 스피드를 탄 클로이 윌리엄스는 22세로 최연소 여성 완주자가 되어 오닥스 UK 메리트 트로피를 받았습니다. 댄 패럴도 TSR 프로토타입으로 PBP에 출전했습니다.',
   'Riding an NS SPEED, Chloe Williams became the youngest female finisher at 22 and won the Audax UK Merit Trophy. Dan Farrell also rode PBP on a prototype TSR.',
   'NSスピードに乗ったクロエ・ウィリアムズは22歳で最年少女性完走者となり、オダックスUKメリット・トロフィーを受賞しました。ダン・ファレルもTSRのプロトタイプでPBPに出走しました。',
   '骑 NS SPEED 的 Chloe Williams 以 22 岁成为最年轻的女性完赛者，并获得 Audax UK 荣誉奖杯。Dan Farrell 也骑 TSR 原型车参加了 PBP。'),
  '1,200 km'),
 ('2007','kazuhiro-yamamoto-ns-double-pylon-suzuka-japan-2007.jpg',
  ('일본 스즈카 엔듀로','Suzuka Enduro, Japan','鈴鹿エンデューロ','日本铃鹿耐力赛'),
  ('캐논데일 디아도라 레이싱의 야마모토 가즈히로는 NS 더블 파일런으로 4시간 솔로 클래스에서 320명 중 6위에 올랐습니다. 다섯 해 연속 출전이었습니다.',
   'Kazuhiro Yamamoto of Cannondale Diadora Racing finished 6th of 320 in the four-hour solo class on an NS Double Pylon, his fifth consecutive year at the event.',
   'キャノンデール・ディアドラ・レーシングのカズヒロ・ヤマモトは、NSダブルパイロンで4時間ソロクラス320人中6位に入りました。5年連続の出場でした。',
   'Cannondale Diadora Racing 的 Kazuhiro Yamamoto 骑 NS Double Pylon 在 4 小时个人组 320 人中获得第 6 名，这是他连续第五年参赛。'),
  '6th / 320'),
]

def recs(items):
    out = []
    for yr, img, title, body, fig in items:
        fig_html = f'<span class="fig">{fig}</span>' if fig else ''
        out.append(f"""
      <article class="rec">
        <div class="rec__img"><img data-src="{img}" alt="{title[1]}, {yr}" loading="lazy"><span class="rec__yr">{yr}</span></div>
        <h3 {t(*title)}>{title[0]}</h3>
        <p {t(*body)}>{body[0]}</p>
        {fig_html}
      </article>""")
    return ''.join(out)

def main():
    return f"""
<main id="top">

<section class="phero">
  <img data-src="john-woodburn-training-f-frame-moulton-bike.jpg" alt="John Woodburn training on an F-frame Moulton" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow">The Speed Machine</div>
    <h1 {t('레이싱 & 기록','Records & Racing','レース＆記録','竞速与纪录')}>레이싱 &amp; 기록</h1>
    <p {t('작은 바퀴는 느리다는 편견을 기록으로 깨 온 60년. 1962년 카디프~런던에서 시속 82.54km의 세계 속도 기록, 그리고 대륙 횡단 레이스까지.',
         'Sixty years of breaking the small-wheel prejudice with results. From Cardiff–London in 1962 to an 82.54 km/h world speed record and racing across a continent.',
         '小径車は遅いという偏見を記録で覆してきた60年。1962年のカーディフ〜ロンドンから時速82.54kmの世界速度記録、そして大陸横断レースまで。',
         '用成绩打破"小轮慢"偏见的六十年。从 1962 年的卡迪夫至伦敦，到时速 82.54 公里的世界速度纪录，再到横穿大陆的比赛。')}>작은 바퀴는 느리다는 편견을 기록으로 깨 온 60년. 1962년 카디프~런던에서 시속 82.54km의 세계 속도 기록, 그리고 대륙 횡단 레이스까지.</p>
  </div>
</section>

<section class="lede">
  <div class="wrap lede__grid rv">
    <div>
      <div class="eyebrow">Records &amp; Racing</div>
      <h2 {t('신뢰는 기록으로 증명되었습니다','Credibility, proven by the clock','信頼は記録で証明された','以成绩证明的信誉')}>신뢰는 기록으로 증명되었습니다</h2>
    </div>
    <div>
      <p {t('1962년에 나온 성인용 소구경 자전거 몰튼에게는 신뢰가 필요했습니다. 알렉스 몰튼은 이를 미리 계획했고, 그 자신이 기록 보유 사이클리스트였던 마케팅 매니저 데이비드 더필드가 여러 라이더를 후원했습니다. 코번트리 CC의 추발팀과 소구경 로드 라이더들은 클럽 사이클리스트들 사이에서 몰튼의 자리를 굳혔습니다.',
           'Launched in 1962, Moulton’s small-wheeled adult bicycle needed credibility. Alex Moulton planned for this, and marketing manager David Duffield, himself a record-breaking cyclist, backed several riders. Coventry CC’s pursuit team and small-wheel road riders helped establish the bike among club cyclists.',
           '1962年に登場した大人向け小径車モールトンには、信頼が必要でした。アレックス・モールトンはこれを見越し、自身も記録保持者だったマーケティング・マネージャーのデイヴィッド・ダフィールドが何人ものライダーを支援しました。コヴェントリーCCの追い抜きチームと小径ロードライダーたちが、クラブサイクリストの間でモールトンの地位を築きました。',
           '1962 年推出的成人小轮径自行车莫尔顿需要建立信誉。亚历克斯·莫尔顿早有规划，本身就是纪录保持者的市场经理 David Duffield 赞助了多名车手。考文垂 CC 的追逐赛车队与小轮公路车手让莫尔顿在俱乐部骑手中站稳了脚跟。')}>1962년에 나온 성인용 소구경 자전거 몰튼에게는 신뢰가 필요했습니다. 알렉스 몰튼은 이를 미리 계획했고, 그 자신이 기록 보유 사이클리스트였던 마케팅 매니저 데이비드 더필드가 여러 라이더를 후원했습니다. 코번트리 CC의 추발팀과 소구경 로드 라이더들은 클럽 사이클리스트들 사이에서 몰튼의 자리를 굳혔습니다.</p>
      <p {t('이후 UCI 규정 1.3.018로 몰튼은 로드 레이스 출전이 금지되었지만, 타임 트라이얼과 울트라 디스턴스 대회에서는 지금도 출전할 수 있습니다.',
           'UCI rule 1.3.018 later barred Moultons from road racing, but they remain legal in time trials and ultra-distance events.',
           'その後UCI規則1.3.018によりモールトンはロードレースから締め出されましたが、タイムトライアルとウルトラディスタンス競技には今も出場できます。',
           '此后 UCI 第 1.3.018 条规定禁止莫尔顿参加公路赛，但在计时赛与超长距离赛事中至今仍可参赛。')}>이후 UCI 규정 1.3.018로 몰튼은 로드 레이스 출전이 금지되었지만, 타임 트라이얼과 울트라 디스턴스 대회에서는 지금도 출전할 수 있습니다.</p>
      <div class="stat">
        <div><b>6:43:29</b><span {t('1962 카디프~런던 162마일','1962 Cardiff–London, 162 mi','1962 カーディフ〜ロンドン 162マイル','1962 卡迪夫至伦敦 162 英里')}>1962 카디프~런던 162마일</span></div>
        <div><b>82.54<small>km/h</small></b><span {t('1986 세계 속도 기록','1986 world speed record','1986 世界速度記録','1986 世界速度纪录')}>1986 세계 속도 기록</span></div>
        <div><b>10d 15h</b><span {t('1988 레이스 어크로스 아메리카','1988 Race Across America','1988 レース・アクロス・アメリカ','1988 横穿美国赛')}>1988 레이스 어크로스 아메리카</span></div>
      </div>
    </div>
  </div>
</section>

<div class="wide rv"><img data-src="moulton-f-frames-racing-at-the-butts-track-coventry-1963.jpg" alt="Moulton F-frames racing at The Butts, Coventry, 1963" loading="lazy"></div>

<section class="era" id="f-frame">
  <div class="wrap">
    <div class="era__head rv">
      <div>
        <div class="eyebrow" {t('F-프레임 시대','The F-frame Era','Fフレーム時代','F 型车架时代')}>F-프레임 시대</div>
        <h2 {t('F-프레임의 승리','F-frame Triumphs','Fフレームの勝利','F 型车架的胜利')}>F-프레임의 승리</h2>
        <div class="yrs">1962 – 1978</div>
      </div>
      <div class="sil">
        <img data-src="moulton-bike-f-frame-silhouette-non-drive-side.png" alt="" loading="lazy">
        <img data-src="moulton-bike-f-frame-silhouette-drive-side.png" alt="" loading="lazy">
      </div>
    </div>
    <div class="recs rv">{recs(F_FRAME)}
    </div>
  </div>
</section>

<div class="wide rv"><img data-src="dave-bogdan-raam-1988-moulton-am-speed-bike-countryside.jpg" alt="Dave Bogdan on an AM SPEED in the Race Across America, 1988" loading="lazy"></div>

<section class="era dark" id="spaceframe">
  <div class="wrap">
    <div class="era__head rv">
      <div>
        <div class="eyebrow" {t('스페이스프레임 시대','The Spaceframe Era','スペースフレーム時代','空间车架时代')}>스페이스프레임 시대</div>
        <h2 {t('스페이스프레임의 성공','Spaceframe Success','スペースフレームの成功','空间车架的成功')}>스페이스프레임의 성공</h2>
        <div class="yrs">1984 – 2007</div>
      </div>
      <div class="sil">
        <img data-src="moulton-bike-space-frame-silhouette-non-drive-side.png" alt="" loading="lazy">
        <img data-src="moulton-bike-space-frame-silhouette-drive-side.png" alt="" loading="lazy">
      </div>
    </div>
    <div class="recs rv">{recs(SPACEFRAME)}
    </div>
  </div>
</section>

<div class="wide rv"><img data-src="moulton-s-speed-f-frame-bike-racing-against-larger-wheeled-racing-bikes-1967.jpg" alt="Moulton S Speed racing against larger-wheeled bikes, 1967" loading="lazy"></div>

<section class="next">
  <div class="wrap">
    <div class="next__grid rv">
      <a href="/about-moulton/">
        <div class="k">Small Wheels</div>
        <h3 {t('몰튼 자전거','The Moulton Bike','モールトンの自転車','莫尔顿自行车')}>몰튼 자전거</h3>
        <p {t('작은 바퀴와 스페이스프레임이 왜 빠른지, 몰튼의 설계와 엔지니어링.','Why small wheels and a spaceframe are fast: the design and engineering of the Moulton.','小径ホイールとスペースフレームがなぜ速いのか、モールトンの設計とエンジニアリング。','小轮径与空间车架为何快：莫尔顿的设计与工程。')}>작은 바퀴와 스페이스프레임이 왜 빠른지, 몰튼의 설계와 엔지니어링.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
      <a href="/design/">
        <div class="k">Heritage</div>
        <h3 {t('디자인의 진화','Design Evolution','デザインの進化','设计演进')}>디자인의 진화</h3>
        <p {t('기록을 세운 F-프레임과 AM 스피드가 태어난 과정.','How the record-setting F-frame and AM SPEED came to be.','記録を打ち立てたFフレームとAMスピードが生まれた過程。','创造纪录的 F 型车架与 AM SPEED 的诞生历程。')}>기록을 세운 F-프레임과 AM 스피드가 태어난 과정.</p>
        <span class="link" {t('자세히 보기','Read more','詳しく見る','了解更多')}>자세히 보기</span>
      </a>
      <a href="/#bikes">
        <div class="k">The Range</div>
        <h3 {t('현행 모델','Current models','現行モデル','现行车型')}>현행 모델</h3>
        <p {t('NS 스피드, NS 더블 파일런, 스피드. 오늘의 퍼포먼스 몰튼.','NS Speed, NS D-Pylon, Speed: today’s performance Moultons.','NSスピード、NSダブルパイロン、スピード。今日のパフォーマンス・モールトン。','NS Speed、NS D-Pylon、Speed：今日的性能型莫尔顿。')}>NS 스피드, NS 더블 파일런, 스피드. 오늘의 퍼포먼스 몰튼.</p>
        <span class="link" {t('전 모델 보기','View all bikes','全モデルを見る','查看全部车型')}>전 모델 보기</span>
      </a>
    </div>
  </div>
</section>

</main>
"""
