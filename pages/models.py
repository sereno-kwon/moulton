# -*- coding: utf-8 -*-
"""모델 페이지 14종 (/<slug>/). 데이터는 pages/_model_data.py, 가격은 /models.js.
   build.py 가 PAGES 목록을 읽어 각 페이지를 생성한다."""
import re, html
from types import SimpleNamespace
from build import t
from pages._model_data import MODELS

GRID_ORDER = ['ns-double-pylon', 'ns-speed', 'ns-rapide', 'speed', 'ns-safari', 'ns-marathon', 'am-gt',
              'jubilee', 'am-speed', 'am-22', 'xtb', 'sst', 'the-hall-se', 'tsr']

# ---------------------------------------------------------------- i18n tables
SECTIONS = [
  ('overview', ('개요', 'Overview', '概要', '概览'),
     ['Ride Category', 'Brake Type', 'Handlebar Type', 'Gear System']),
  ('drive', ('구동계', 'Drive Train', 'ドライブトレイン', '传动系统'),
     ['Front Mech', 'Rear Mech', 'Crankset', 'Cassette', 'Chain', 'Bottom Bracket', 'Gear Range (inches)']),
  ('brakes', ('브레이크', 'Brakes', 'ブレーキ', '刹车'), ['Brakes', 'Gear/Brake Levers']),
  ('cockpit', ('콕핏', 'Cockpit', 'コックピット', '操控'), ['Handlebar', 'Tapes/Grips', 'Handlebar Stem', 'Headset']),
  ('seat', ('시트', 'Seat', 'シート', '座椅'), ['Saddle', 'Seatpost']),
  ('wheels', ('휠', 'Wheels', 'ホイール', '轮组'), ['Tyres', 'Rims', 'Rear Hub', 'Front Hub', 'Spokes']),
  ('mudguards', ('머드가드', 'Mudguards', 'マッドガード', '挡泥板'), ['Mudguards', 'Mudguard Clearance']),
  ('other', ('기타', 'Other', 'その他', '其他'), ['Pedals', 'Weight']),
]

LABELS = {
  'Wheel Size': ('휠 사이즈', 'ホイールサイズ', '车轮尺寸'),
  'Front Suspension': ('프론트 서스펜션', 'フロントサスペンション', '前避震'),
  'Rear Suspension': ('리어 서스펜션', 'リアサスペンション', '后避震'),
  'Separability': ('분리 여부', '分割', '可拆分性'),
  'Frame Coupling': ('프레임 결합 방식', 'フレーム結合方式', '车架连接方式'),
  'Frame Material': ('프레임 소재', 'フレーム素材', '车架材质'),
  'Frame Construction': ('프레임 구조', 'フレーム構造', '车架工艺'),
  'Bottle Mounts': ('물병 케이지 마운트', 'ボトルマウント', '水壶架孔位'),
  'Frame Finish': ('프레임 마감', 'フレーム仕上げ', '车架涂装'),
  'Ride Category': ('라이딩 카테고리', 'ライドカテゴリー', '骑行类别'),
  'Brake Type': ('브레이크 타입', 'ブレーキタイプ', '刹车类型'),
  'Handlebar Type': ('핸들바 타입', 'ハンドルバータイプ', '车把类型'),
  'Gear System': ('변속 방식', '変速方式', '变速系统'),
  'Front Mech': ('프론트 디레일러', 'フロントディレイラー', '前拨'),
  'Rear Mech': ('리어 디레일러', 'リアディレイラー', '后拨'),
  'Crankset': ('크랭크셋', 'クランクセット', '牙盘'),
  'Cassette': ('카세트', 'カセット', '飞轮'),
  'Chain': ('체인', 'チェーン', '链条'),
  'Bottom Bracket': ('바텀 브래킷', 'ボトムブラケット', '中轴'),
  'Gear Range (inches)': ('기어 레인지 (인치)', 'ギアレンジ（インチ）', '齿比范围（英寸）'),
  'Brakes': ('브레이크', 'ブレーキ', '刹车'),
  'Gear/Brake Levers': ('변속·브레이크 레버', 'シフト／ブレーキレバー', '变速/刹车手柄'),
  'Handlebar': ('핸들바', 'ハンドルバー', '车把'),
  'Tapes/Grips': ('바 테이프·그립', 'バーテープ／グリップ', '把带/握把'),
  'Handlebar Stem': ('스템', 'ステム', '把立'),
  'Headset': ('헤드셋', 'ヘッドセット', '车头碗组'),
  'Saddle': ('안장', 'サドル', '坐垫'),
  'Seatpost': ('시트포스트', 'シートポスト', '座管'),
  'Tyres': ('타이어', 'タイヤ', '轮胎'),
  'Rims': ('림', 'リム', '轮圈'),
  'Rear Hub': ('리어 허브', 'リアハブ', '后花鼓'),
  'Front Hub': ('프론트 허브', 'フロントハブ', '前花鼓'),
  'Spokes': ('스포크', 'スポーク', '辐条'),
  'Mudguards': ('머드가드', 'マッドガード', '挡泥板'),
  'Mudguard Clearance': ('머드가드 클리어런스', 'マッドガードクリアランス', '挡泥板间隙'),
  'Pedals': ('페달', 'ペダル', '脚踏'),
  'Weight': ('무게', '重量', '重量'),
}

VALUES = {  # en -> (ko, ja, zh)
  'Road & Race': ('로드 & 레이스', 'ロード＆レース', '公路与竞速'),
  'Touring & Adventure': ('투어링 & 어드벤처', 'ツーリング＆アドベンチャー', '旅行与探险'),
  'City & Leisure': ('시티 & 레저', 'シティ＆レジャー', '城市与休闲'),
  'City & Leisure (flat bar)': ('시티 & 레저 (플랫바)', 'シティ＆レジャー（フラットバー）', '城市与休闲（平把）'),
  'Gravel & Off-road': ('그래블 & 오프로드', 'グラベル＆オフロード', '砂石与越野'),
  'Caliper': ('캘리퍼', 'キャリパー', '夹器'),
  'Hydraulic Disc': ('유압 디스크', '油圧ディスク', '液压碟刹'),
  'V-brake': ('V 브레이크', 'Vブレーキ', 'V刹'),
  'Caliper or V-brake': ('캘리퍼 또는 V 브레이크', 'キャリパーまたはVブレーキ', '夹器或V刹'),
  'Front V-brake + Rear Mech. Disc': ('프론트 V 브레이크 + 리어 기계식 디스크', 'フロントVブレーキ＋リア機械式ディスク', '前V刹＋后机械碟刹'),
  'Front Caliper or V-brake + Rear Mech. Disc': ('프론트 캘리퍼 또는 V 브레이크 + 리어 기계식 디스크', 'フロント キャリパーまたはVブレーキ＋リア機械式ディスク', '前夹器或V刹＋后机械碟刹'),
  'Drop': ('드롭', 'ドロップ', '弯把'),
  'Flat': ('플랫', 'フラット', '平把'),
  'Flat or Drop': ('플랫 또는 드롭', 'フラットまたはドロップ', '平把或弯把'),
  'Derailleur': ('디레일러', 'ディレイラー', '拨链器变速'),
  'Wireless Derailleur': ('무선 디레일러', 'ワイヤレスディレイラー', '无线拨链器变速'),
  'Hub': ('내장 허브', '内装ハブ', '内变速花鼓'),
  'n/a': ('–', '–', '–'),
  'Available as accessory': ('액세서리로 별도 구매 가능', 'アクセサリーとして別売', '可作为配件选购'),
  'none supplied': ('미포함', '付属なし', '不附带'),
  'Separable': ('분리형', '分割式', '可拆分'),
  'Fixed': ('일체형', '一体型', '固定式'),
  'Polished Stainless': ('폴리시드 스테인리스', 'ポリッシュドステンレス', '抛光不锈钢'),
  'Stove Enamel': ('스토브 에나멜', 'ストーブエナメル', '烤漆'),
  'Powder Coat': ('파우더 코트', 'パウダーコート', '粉末喷涂'),
  'Hybrid (Powder/Enamel)': ('하이브리드 (파우더/에나멜)', 'ハイブリッド（パウダー／エナメル）', '混合（粉末喷涂/烤漆）'),
  'Polished Stainless w/ Enamel Highlights or Stove Enamel': ('에나멜 하이라이트 폴리시드 스테인리스 또는 스토브 에나멜', 'エナメルハイライト付きポリッシュドステンレス、またはストーブエナメル', '抛光不锈钢配烤漆点缀，或全烤漆'),
  'Kingpin + stainless locknut': ('킹핀 + 스테인리스 로크너트', 'キングピン＋ステンレスロックナット', '主销＋不锈钢锁紧螺母'),
  'Centre bolt + alloy locknut': ('센터 볼트 + 알루미늄 로크너트', 'センターボルト＋アルミロックナット', '中心螺栓＋铝合金锁紧螺母'),
  'Leading Link (crown)': ('리딩 링크 (크라운)', 'リーディングリンク（クラウン）', 'Leading Link（叉肩式）'),
  'Leading Link (unicrown)': ('리딩 링크 (유니크라운)', 'リーディングリンク（ユニクラウン）', 'Leading Link（一体叉肩式）'),
  "2 sets: front and rear of 'Pylon' seat mast": ('2세트: 파일런 시트 마스트 앞·뒤', '2セット：パイロンシートマストの前後', "2组：塔柱座管前后"),
  '2 sets: seat tube & lower rail': ('2세트: 시트 튜브, 로어 레일', '2セット：シートチューブ、ロワーレール', '2组：座管与下梁'),
  '1 set: seat tube': ('1세트: 시트 튜브', '1セット：シートチューブ', '1组：座管'),
  '4 sets: seat tube, lower rail, 2x head tube': ('4세트: 시트 튜브, 로어 레일, 헤드 튜브 2곳', '4セット：シートチューブ、ロワーレール、ヘッドチューブ×2', '4组：座管、下梁、头管×2'),
  "Silver fillet brazed. Twin tube 'pylon' seat mast and head tube. Tubular zig-zags.": ("실버 필렛 브레이징. 트윈 튜브 '파일런' 시트 마스트와 헤드 튜브. 튜블러 지그재그.", "シルバーフィレットブレージング。ツインチューブの「パイロン」シートマストとヘッドチューブ。チューブラー・ジグザグ。", "银焊填角焊。双管“塔柱”座管与头管。管状之字形支撑。"),
  "Silver fillet brazed. Twin tube 'pylon' seat mast. Tubular zig-zags.": ("실버 필렛 브레이징. 트윈 튜브 '파일런' 시트 마스트. 튜블러 지그재그.", "シルバーフィレットブレージング。ツインチューブの「パイロン」シートマスト。チューブラー・ジグザグ。", "银焊填角焊。双管“塔柱”座管。管状之字形支撑。"),
  "Fillet-brazed with 'shot-in' tubes. Tubular zig-zags.": ("'샷인' 튜브 필렛 브레이징. 튜블러 지그재그.", "「ショットイン」チューブのフィレットブレージング。チューブラー・ジグザグ。", "“嵌入式”管件填角焊。管状之字形支撑。"),
  "Silver fillet brazed with 'shot-in' tubes. Tubular zig-zags.": ("'샷인' 튜브 실버 필렛 브레이징. 튜블러 지그재그.", "「ショットイン」チューブのシルバーフィレットブレージング。チューブラー・ジグザグ。", "“嵌入式”管件银焊填角焊。管状之字形支撑。"),
  "Fillet brazed (with silver for stainless frame) with 'shot-in' tubes. Tubular zig-zags.": ("'샷인' 튜브 필렛 브레이징 (스테인리스 프레임은 실버). 튜블러 지그재그.", "「ショットイン」チューブのフィレットブレージング（ステンレスフレームはシルバー）。チューブラー・ジグザグ。", "“嵌入式”管件填角焊（不锈钢车架为银焊）。管状之字形支撑。"),
  'Fillet brazed, hairpin construction. Tubular zig-zags.': ('필렛 브레이징, 헤어핀 구조. 튜블러 지그재그.', 'フィレットブレージング、ヘアピン構造。チューブラー・ジグザグ。', '填角焊，发夹式结构。管状之字形支撑。'),
  'Fillet brazed, hairpin construction. Solid zig-zags.': ('필렛 브레이징, 헤어핀 구조. 솔리드 지그재그.', 'フィレットブレージング、ヘアピン構造。ソリッド・ジグザグ。', '填角焊，发夹式结构。实心之字形支撑。'),
  'Aerospace stainless steel and Reynolds 931 stainless steel (forks)': ('항공우주 스테인리스 스틸, Reynolds 931 스테인리스 (포크)', '航空宇宙ステンレススチール、Reynolds 931 ステンレス（フォーク）', '航空级不锈钢、Reynolds 931 不锈钢（前叉）'),
  'Columbus Spirit, Kaisei NiCrMo and Reynolds 853 steels (stainless steel dropouts)': ('Columbus Spirit, Kaisei NiCrMo, Reynolds 853 스틸 (스테인리스 드롭아웃)', 'Columbus Spirit、Kaisei NiCrMo、Reynolds 853 スチール（ステンレスドロップアウト）', 'Columbus Spirit、Kaisei NiCrMo、Reynolds 853 钢（不锈钢勾爪）'),
  'Columbus XCr, Reynolds 921 (fork), and Aerospace stainless steels': ('Columbus XCr, Reynolds 921 (포크), 항공우주 스테인리스 스틸', 'Columbus XCr、Reynolds 921（フォーク）、航空宇宙ステンレススチール', 'Columbus XCr、Reynolds 921（前叉）、航空级不锈钢'),
  'Reynolds 853 (forks) with Aerospace stainless steel or Columbus Spirit/Kaisei NiCrMo': ('Reynolds 853 (포크) + 항공우주 스테인리스 또는 Columbus Spirit/Kaisei NiCrMo', 'Reynolds 853（フォーク）＋航空宇宙ステンレスまたは Columbus Spirit/Kaisei NiCrMo', 'Reynolds 853（前叉）＋航空级不锈钢或 Columbus Spirit/Kaisei NiCrMo'),
  'Columbus Spirit and Kaisei NiCroMo steels (stainless steel dropouts)': ('Columbus Spirit, Kaisei NiCrMo 스틸 (스테인리스 드롭아웃)', 'Columbus Spirit、Kaisei NiCrMo スチール（ステンレスドロップアウト）', 'Columbus Spirit、Kaisei NiCrMo 钢（不锈钢勾爪）'),
  'Reynolds 725 and Kaisei NiCroMo steels (stainless steel dropouts)': ('Reynolds 725, Kaisei NiCrMo 스틸 (스테인리스 드롭아웃)', 'Reynolds 725、Kaisei NiCrMo スチール（ステンレスドロップアウト）', 'Reynolds 725、Kaisei NiCrMo 钢（不锈钢勾爪）'),
  'Columbus Spirit and Reynolds 525 CrMo steels (stainless steel dropouts)': ('Columbus Spirit, Reynolds 525 CrMo 스틸 (스테인리스 드롭아웃)', 'Columbus Spirit、Reynolds 525 CrMo スチール（ステンレスドロップアウト）', 'Columbus Spirit、Reynolds 525 CrMo 钢（不锈钢勾爪）'),
  'Columbus Spirit and Reynolds 525 CrMo steels': ('Columbus Spirit, Reynolds 525 CrMo 스틸', 'Columbus Spirit、Reynolds 525 CrMo スチール', 'Columbus Spirit、Reynolds 525 CrMo 钢'),
  'Up to 28mm (Caliper) or 40mm (V-brakes) tyre section': ('최대 28mm (캘리퍼) / 40mm (V 브레이크) 타이어', '最大28mm（キャリパー）／40mm（Vブレーキ）タイヤ', '最大28mm（夹器）/40mm（V刹）轮胎'),
  'Up to 40mm tyre section (V-brakes)': ('최대 40mm 타이어 (V 브레이크)', '最大40mmタイヤ（Vブレーキ）', '最大40mm轮胎（V刹）'),
}

ICONS = {
  'hydrolastic': ('moulton-bike-key-feature-icon-hydrolastic-suspension.png', ('Hydrolastic®',)*4, 'Hydrolastic®'),
  'flexitor': ('moulton-bike-key-feature-icon-flexitor-suspension.png', ('Flexitor®',)*4, 'Flexitor®'),
  'leadinglink': ('moulton-bike-key-feature-icon-leading-link-suspension.png', ('리딩 링크', 'Leading Link', 'リーディングリンク', 'Leading Link'), None),
  'monosphere': ('moulton-bike-key-feature-icon-monosphere-suspension.png', ('모노스피어', 'Monosphere', 'モノスフィア', 'Monosphere'), None),
  '20': ('moulton-bike-key-feature-icon-20-inch-wheel.png', ('20인치 휠', '20" Wheel', '20インチホイール', '20英寸车轮'), None),
  '17': ('moulton-bike-key-feature-icon-17-inch-wheel.png', ('17인치 휠', '17" Wheel', '17インチホイール', '17英寸车轮'), None),
  'separable': ('moulton-bike-key-feature-icon-separable-frame.png', ('분리형 프레임', 'Separable', '分割式フレーム', '可拆分车架'), None),
  'fixed': ('moulton-bike-key-feature-icon-fixed-frame.png', ('일체형 프레임', 'Fixed Frame', '一体型フレーム', '固定车架'), None),
}

SERIES_I18N = {
  'New Series': ('뉴 시리즈', 'New Series', 'ニューシリーズ', 'New Series'),
  'Moulton': ('몰튼', 'Moulton', 'モールトン', 'Moulton'),
  'AM Series': ('AM 시리즈', 'AM Series', 'AMシリーズ', 'AM 系列'),
  'Y-frame': ('Y-프레임', 'Y-frame', 'Yフレーム', 'Y 型车架'),
  'Special Edition': ('스페셜 에디션', 'Special Edition', 'スペシャルエディション', '特别版'),
}

def tr_val(v):
    """값 하나를 4개 언어 span 으로. 사전에 없으면 영문 그대로"""
    v = v.strip()
    if v in VALUES:
        ko, ja, zh = VALUES[v]
        return f'<span {t(ko, v, ja, zh)}>{html.escape(ko)}</span>'
    m = re.fullmatch(r'Up to (\d+)mm tyre section', v)
    if m:
        n = m.group(1)
        return f'<span {t(f"최대 {n}mm 타이어", v, f"最大{n}mmタイヤ", f"最大{n}mm轮胎")}>최대 {n}mm 타이어</span>'
    return html.escape(v)

def tr_cell(v):
    """'; ' 로 나뉜 복수 값(라이딩 카테고리) 처리"""
    parts = [p for p in v.split(';')]
    return '<br>'.join(tr_val(p) for p in parts) if len(parts) > 1 else tr_val(v)

def label(en):
    ko, ja, zh = LABELS[en]
    return f'<span {t(ko, en, ja, zh)}>{ko}</span>'

def parse_lines(block):
    out = []
    for line in block.strip().splitlines():
        k, v = line.split(':', 1)
        out.append((k.strip(), v.strip()))
    return out

def build_specs(m):
    rows = parse_lines(m['spec'])
    nb = len(m['builds'])
    per = [dict() for _ in range(nb)]
    for k, v in rows:
        cols = [c.strip() for c in v.split(' | ')]
        if len(cols) == 1:
            cols = cols * nb
        assert len(cols) == nb, (m['slug'], k, len(cols), nb)
        for i in range(nb):
            per[i][k] = cols[i]
    return per

def weight_kg(s):
    mm = re.match(r'([\d.]+)\s*kg', s)
    return float(mm.group(1)) if mm else None

def series_label(s):
    ko, en, ja, zh = SERIES_I18N[s]
    return f'<span {t(ko, en, ja, zh)}>{ko}</span>'

# ---------------------------------------------------------------- CSS
CSS = """
/* ===== Model page ===== */
.eyebrow{font-size:14px;letter-spacing:.18em;margin-bottom:14px}
.phero{position:relative;height:min(82vh,800px);min-height:480px;overflow:hidden;background:#161616}
.phero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.phero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.62) 0%,rgba(0,0,0,.28) 42%,rgba(0,0,0,0) 70%),linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.5) 100%)}
.phero__txt{position:absolute;left:0;right:0;bottom:clamp(40px,8vh,80px);z-index:2;color:#fff}
.phero__txt .eyebrow{color:#fff;opacity:.85}
.phero__txt h1{font-family:var(--en);font-weight:600;font-size:clamp(44px,7vw,104px);line-height:.95;letter-spacing:-.03em;text-transform:uppercase;text-shadow:0 2px 24px rgba(0,0,0,.35)}
.phero__txt p{color:rgba(255,255,255,.9);margin-top:18px;font-size:clamp(16px,1.4vw,20px);max-width:40ch}
.crumbs{font-family:var(--en);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);padding-top:22px}
.crumbs a:hover{color:var(--red)}
.crumbs span{margin:0 8px}

/* product block */
.pd{padding:clamp(28px,4vw,56px) 0 clamp(56px,7vw,100px)}
.pd__grid{display:grid;grid-template-columns:1.25fr 1fr;gap:clamp(32px,5vw,80px);align-items:start}
.gal__main{position:relative;aspect-ratio:4/3;background:var(--bg-soft);overflow:hidden}
.gal__main img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:4%;transition:opacity .3s}
.gal__thumbs{display:flex;gap:10px;margin-top:10px;flex-wrap:wrap}
.gal__thumbs button{width:92px;aspect-ratio:4/3;background:var(--bg-soft);border:1px solid transparent;padding:0;overflow:hidden;opacity:.6;transition:opacity .2s,border-color .2s}
.gal__thumbs button.on,.gal__thumbs button:hover{opacity:1;border-color:var(--ink)}
.gal__thumbs img{width:100%;height:100%;object-fit:contain;padding:6%}
.pd__info{position:sticky;top:100px}
.pd__info h2{font-family:var(--en);font-weight:600;font-size:clamp(32px,3.2vw,46px);letter-spacing:-.02em;text-transform:uppercase;line-height:1}
.pd__price{font-family:var(--en);font-size:20px;margin-top:14px;font-variant-numeric:tabular-nums}
.pd__price.ask{font-size:15px;color:var(--ink-3);letter-spacing:.04em}
.pd__desc{margin-top:24px;font-size:15.5px;line-height:1.75}
.icons{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:28px;padding:20px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.icons div{text-align:center}
.icons img{width:44px;height:44px;object-fit:contain;margin:0 auto 8px}
.icons span{display:block;font-family:var(--en);font-size:11.5px;letter-spacing:.06em;color:var(--ink-2);line-height:1.35}
.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:22px}
.facts b{display:block;font-family:var(--en);font-size:20px;font-weight:600;letter-spacing:-.01em}
.facts span{display:block;font-family:var(--en);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-top:4px}
.pd__cta{display:flex;gap:10px;flex-wrap:wrap;margin-top:28px}
.pd__cta .btn{flex:1 1 auto;justify-content:center}
.lead{margin-top:18px;font-size:13px;color:var(--ink-3);line-height:1.6}
.lead b{color:var(--ink-2);font-weight:600}

/* details */
.details{display:grid;gap:12px;padding-bottom:clamp(56px,7vw,100px)}
.details.n1{grid-template-columns:1fr}
.details.n1 figure{aspect-ratio:21/9}
.details.n5{grid-template-columns:repeat(5,1fr)}
.details figure{aspect-ratio:4/5;overflow:hidden;background:var(--bg-soft)}
.details img{width:100%;height:100%;object-fit:cover;transition:transform 1s cubic-bezier(.2,.7,.2,1)}
.details figure:hover img{transform:scale(1.05)}

/* spec */
.spec{border-top:1px solid var(--ink);padding:clamp(48px,6vw,88px) 0}
.spec__head{display:grid;grid-template-columns:1fr 2fr;gap:clamp(24px,5vw,96px);margin-bottom:clamp(24px,3vw,40px);align-items:end}
.spec__head h2{font-family:var(--en);font-weight:300}
html[lang="ko"] .spec__head h2,html[lang="ja"] .spec__head h2,html[lang="zh"] .spec__head h2{font-weight:300}
.spec__body{display:grid;grid-template-columns:1fr 2fr;gap:clamp(24px,5vw,96px)}
.spec__side .eyebrow{margin-bottom:8px}
.spec__side p{font-size:14px}
table.st{width:100%;border-collapse:collapse;font-size:14.5px}
table.st th,table.st td{text-align:left;vertical-align:top;padding:12px 0;border-bottom:1px solid var(--line)}
table.st th{width:38%;font-weight:400;color:var(--ink-3);padding-right:20px;font-size:13.5px}
table.st td{color:var(--ink)}
.tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:26px}
.tabs button{font-family:var(--en);font-size:12px;font-weight:600;letter-spacing:.08em;padding:10px 16px;border:1px solid var(--line);color:var(--ink-2);transition:.2s}
.tabs button:hover{border-color:var(--ink)}
.tabs button.on{background:var(--ink);border-color:var(--ink);color:#fff}
.bpanel{display:none}
.bpanel.on{display:block}
.bsec{display:grid;grid-template-columns:160px 1fr;gap:20px;padding:6px 0 22px}
.bsec h4{font-family:var(--en);font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--red);font-weight:600;padding-top:13px}
html[lang="ko"] .bsec h4,html[lang="ja"] .bsec h4,html[lang="zh"] .bsec h4{letter-spacing:.06em;font-size:13px}

/* lifestyle */
.life{display:grid;gap:12px}
.life.n1 figure{aspect-ratio:21/9}
.life.n2{grid-template-columns:1fr 1fr}
.life.n2 figure{aspect-ratio:4/3}
.life figure{overflow:hidden;background:var(--bg-soft)}
.life img{width:100%;height:100%;object-fit:cover}

.cta{background:var(--ink);color:#fff;padding:clamp(64px,8vw,110px) 0;text-align:center;margin-top:clamp(56px,7vw,100px)}
.cta h2{margin-bottom:16px}
.cta p{color:rgba(255,255,255,.75);margin:0 auto 32px}
.cta .btn{margin:6px}

.more{padding:clamp(64px,8vw,110px) 0}
.more__head{display:flex;justify-content:space-between;align-items:end;margin-bottom:clamp(24px,3vw,40px);gap:20px}
.more__grid{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.mcard .im{aspect-ratio:1/1;background:var(--bg-soft);overflow:hidden}
.mcard img{width:100%;height:100%;object-fit:contain;padding:8%;transition:transform .6s}
.mcard:hover img{transform:scale(1.04)}
.mcard b{display:block;font-family:var(--en);font-size:14px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin-top:14px}
.mcard span{display:block;font-family:var(--en);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-top:4px}

@media (max-width:1024px){
  .pd__grid{grid-template-columns:1fr}
  .pd__info{position:static}
  .details.n5{grid-template-columns:repeat(3,1fr)}
  .more__grid{grid-template-columns:repeat(2,1fr)}
}
@media (max-width:820px){
  .spec__head,.spec__body{grid-template-columns:1fr;gap:16px}
  .bsec{grid-template-columns:1fr;gap:0}
  .bsec h4{padding-top:4px}
  .life.n2{grid-template-columns:1fr}
  .life.n1 figure,.details.n1 figure{aspect-ratio:4/3}
  .more__head{flex-direction:column;align-items:flex-start}
}
@media (max-width:560px){
  .phero{height:72vh}
  .icons{grid-template-columns:repeat(2,1fr);row-gap:18px}
  .details.n5{grid-template-columns:repeat(2,1fr)}
  table.st th{width:42%}
  .gal__thumbs button{width:72px}
  .facts b{font-size:16px}
}
"""

# ---------------------------------------------------------------- page body
def render(m):
    by_slug = {x['slug']: x for x in MODELS}
    builds = build_specs(m)
    keyrows = parse_lines(m['key'])
    keymap = dict(keyrows)
    ws = [w for w in (weight_kg(b['Weight']) for b in builds) if w]
    if not ws:
        wtxt = '–'
    elif min(ws) == max(ws):
        wtxt = f'{min(ws):g} kg'
    else:
        wtxt = f'{min(ws):g}–{max(ws):g} kg'
    wheel = keymap['Wheel Size'].split(' (')[0].replace('" / 20"', '"')
    sep = keymap['Separability']

    # gallery
    g0 = m['gallery'][0]
    thumbs = ''.join(
        f'<button type="button" class="{"on" if i == 0 else ""}" aria-label="image {i+1}"><img data-src="{g}" alt="Moulton {m['name']} {i+1}" loading="lazy"></button>'
        for i, g in enumerate(m['gallery']))

    icons = ''.join(
        f'<div><img data-src="{ICONS[k][0]}" alt=""><span {t(*ICONS[k][1])}>{ICONS[k][1][0]}</span></div>'
        for k in m['icons'])

    if m['lead'] == 'stock':
        lead = (f'<b {t("즉시 생산 가능","In stock","即納可能","现货")}>즉시 생산 가능</b>',)
        lead_html = (f'<span {t("영국 공장 재고:","Factory stock:","英国工場在庫：","英国工厂库存：")}>영국 공장 재고:</span> {lead[0]}')
    else:
        L = m['lead']
        lead_html = (f'<span {t("영국 공장 생산 리드타임:","UK factory lead time:","英国工場の生産リードタイム：","英国工厂生产周期：")}>영국 공장 생산 리드타임:</span> '
                     f'<b {t(f"{L}개월", f"{L} months", f"{L}ヶ月", f"{L}个月")}>{L}개월</b>')
    lead_html += (f'<br><span {t("국내 인도 일정은 상담 시 안내해 드립니다.","Delivery to Korea is confirmed at consultation.","国内への納期はご相談時にご案内します。","在韩交付时间将于咨询时告知。")}>국내 인도 일정은 상담 시 안내해 드립니다.</span>')

    # details
    det = ''
    if m['details']:
        n = 'n5' if len(m['details']) >= 3 else 'n1'
        det = f'<section class="wrap details {n} rv">' + ''.join(
            f'<figure><img data-src="{d}" alt="Moulton {m["name"]} 디테일" loading="lazy"></figure>' for d in m['details']) + '</section>'

    # key features table
    key_tbl = ''.join(f'<tr><th>{label(k)}</th><td>{tr_cell(v)}</td></tr>' for k, v in keyrows)

    # builds
    tabs = ''
    if len(builds) > 1:
        tabs = '<div class="tabs" role="tablist">' + ''.join(
            f'<button type="button" class="{"on" if i == 0 else ""}" data-b="{i}">{html.escape(b)}</button>'
            for i, b in enumerate(m['builds'])) + '</div>'
    panels = ''
    for i, b in enumerate(builds):
        secs = ''
        for _, names, rows in SECTIONS:
            trs = ''.join(f'<tr><th>{label(r)}</th><td>{tr_cell(b[r])}</td></tr>' for r in rows if r in b)
            if trs:
                secs += f'<div class="bsec"><h4 {t(*names)}>{names[0]}</h4><table class="st">{trs}</table></div>'
        single = '' if len(builds) > 1 else f'<div class="eyebrow" style="margin-bottom:22px">{html.escape(m["builds"][0])}</div>'
        panels += f'<div class="bpanel{" on" if i == 0 else ""}" data-b="{i}">{single}{secs}</div>'

    # lifestyle
    life = ''
    if m['lifestyle']:
        n = 'n2' if len(m['lifestyle']) >= 2 else 'n1'
        life = f'<section class="wrap life {n} rv">' + ''.join(
            f'<figure><img data-src="{x}" alt="Moulton {m["name"]} 라이프스타일" loading="lazy"></figure>' for x in m['lifestyle'][:2]) + '</section>'

    # other models: next 4 in grid order
    idx = GRID_ORDER.index(m['slug'])
    others = [by_slug[GRID_ORDER[(idx + k) % len(GRID_ORDER)]] for k in range(1, 5)]
    more = ''.join(
        f'<a class="mcard" href="/{o["slug"]}/"><div class="im"><img data-src="{o["gallery"][0]}" alt="Moulton {o["name"]}" loading="lazy"></div>'
        f'<b>{o["name"]}</b><span>{o["series"]}</span></a>' for o in others)

    nb = len(builds)
    builds_txt = t(f'빌드 {nb}종', f'{nb} build{"s" if nb > 1 else ""}', f'{nb}種のビルド', f'{nb}种配置')

    return f"""
<main id="top">

<section class="phero">
  <img data-src="{m['hero']}" alt="Moulton {m['name']}" fetchpriority="high">
  <div class="wrap phero__txt">
    <div class="eyebrow">{series_label(m['series'])}</div>
    <h1>{m['name']}</h1>
    <p {t(*m['tag'])}>{m['tag'][0]}</p>
  </div>
</section>

<div class="wrap crumbs"><a href="/">Moulton</a><span>/</span><a href="/#bikes" {t('모델','Bikes','モデル','车型')}>모델</a><span>/</span>{m['name']}</div>

<section class="pd">
  <div class="wrap pd__grid">
    <div class="gal">
      <div class="gal__main"><img id="galMain" data-src="{g0}" alt="Moulton {m['name']}"></div>
      <div class="gal__thumbs">{thumbs if len(m['gallery']) > 1 else ''}</div>
    </div>
    <div class="pd__info">
      <div class="eyebrow">{series_label(m['series'])}</div>
      <h2>{m['name']}</h2>
      <div class="pd__price" id="pdPrice" data-slug="{m['slug']}"></div>
      <p class="pd__desc" {t(*m['desc'])}>{m['desc'][0]}</p>
      <div class="icons">{icons}</div>
      <div class="facts">
        <div><b>{html.escape(wheel)}</b><span {t('휠','Wheel','ホイール','车轮')}>휠</span></div>
        <div><b>{wtxt}</b><span {t('무게','Weight','重量','重量')}>무게</span></div>
        <div><b {t(*(VALUES[sep][0], sep, VALUES[sep][1], VALUES[sep][2]))}>{VALUES[sep][0]}</b><span {t('프레임','Frame','フレーム','车架')}>프레임</span></div>
      </div>
      <div class="pd__cta">
        <a class="btn red" href="https://rubiworkshop.com/models" target="_blank" rel="noopener" {t('상담 신청','Enquire','ご相談はこちら','预约咨询')}>상담 신청</a>
        <a class="btn" href="/authorized-dealer/" {t('공식 딜러','Find a dealer','正規ディーラー','授权经销商')}>공식 딜러</a>
      </div>
      <p class="lead">{lead_html}</p>
    </div>
  </div>
</section>

{det}

<section class="spec" id="frame">
  <div class="wrap">
    <div class="spec__head rv">
      <div><div class="eyebrow">Key Features</div><h2 {t('프레임','Frame','フレーム','车架')}>프레임</h2></div>
    </div>
    <div class="spec__body rv">
      <div class="spec__side"><p {t('모든 몰튼 프레임은 영국 브래드퍼드온에이번의 홀 에스테이트에서 손으로 만들어집니다.','Every Moulton frame is hand-built at the Hall Estate in Bradford-on-Avon, England.','すべてのモールトンのフレームは、英国ブラッドフォード・オン・エイヴォンのホール・エステートで手作業で製作されます。','每一副莫尔顿车架都在英国布拉德福德昂埃文的 Hall Estate 手工打造。')}>모든 몰튼 프레임은 영국 브래드퍼드온에이번의 홀 에스테이트에서 손으로 만들어집니다.</p></div>
      <table class="st">{key_tbl}</table>
    </div>
  </div>
</section>

<section class="spec" id="build">
  <div class="wrap">
    <div class="spec__head rv">
      <div><div class="eyebrow">Build Specifications</div><h2 {t('빌드 사양','Build Specifications','ビルド仕様','配置规格')}>빌드 사양</h2></div>
      <p style="font-size:14px" {t('표준 빌드 기준입니다. 루비워크샵에서 부품 구성을 바꾼 커스텀 빌드도 상담할 수 있습니다.','Standard factory builds. Custom builds with alternative components are available through Rubi Workshop.','標準ビルドの仕様です。Rubi Workshopではパーツ構成を変更したカスタムビルドもご相談いただけます。','以下为标准配置。亦可通过 Rubi Workshop 咨询更换零件的定制装配。')}>표준 빌드 기준입니다. 루비워크샵에서 부품 구성을 바꾼 커스텀 빌드도 상담할 수 있습니다.</p>
    </div>
    <div class="rv">
      {tabs}
      {panels}
    </div>
  </div>
</section>

{life}

<section class="cta">
  <div class="wrap rv">
    <div class="eyebrow" {t('시승 · 상담','Test ride · Consulting','試乗 · ご相談','试骑 · 咨询')}>시승 · 상담</div>
    <h2>{m['name']}</h2>
    <p {t('서울 반포 루비워크샵 몰튼 쇼룸에서 직접 보고 타 볼 수 있습니다. 사이즈와 빌드, 컬러를 함께 정해 드립니다.','See and ride it at the Moulton showroom, Rubi Workshop in Banpo, Seoul. We will help you choose size, build and colour.','ソウル・盤浦のRubi Workshopモールトンショールームで、実際にご覧いただき、試乗できます。サイズ、ビルド、カラーを一緒にお選びします。','欢迎到首尔盘浦 Rubi Workshop 莫尔顿展厅看车试骑，我们将协助您确定尺寸、配置与颜色。')}>서울 반포 루비워크샵 몰튼 쇼룸에서 직접 보고 타 볼 수 있습니다. 사이즈와 빌드, 컬러를 함께 정해 드립니다.</p>
    <a class="btn light" href="https://rubiworkshop.com/models" target="_blank" rel="noopener" {t('상담 신청','Enquire','ご相談はこちら','预约咨询')}>상담 신청</a>
    <a class="btn light" href="/sizing/" {t('사이징','Sizing','サイジング','尺寸')}>사이징</a>
    <a class="btn light" href="/colors/" {t('컬러','Colours','カラー','颜色')}>컬러</a>
  </div>
</section>

<section class="more">
  <div class="wrap">
    <div class="more__head rv">
      <div><div class="eyebrow">The Range</div><h2 {t('다른 모델','Other models','他のモデル','其他车型')}>다른 모델</h2></div>
      <a class="link" href="/#bikes" {t('전 모델 보기','View all bikes','全モデルを見る','查看全部车型')}>전 모델 보기</a>
    </div>
    <div class="more__grid rv">{more}</div>
  </div>
</section>

</main>

<script>
document.addEventListener('DOMContentLoaded',()=>{{
  /* gallery */
  const main=document.getElementById('galMain');
  document.querySelectorAll('.gal__thumbs button').forEach(b=>b.addEventListener('click',()=>{{
    main.style.opacity=0; const src=b.querySelector('img').src;
    setTimeout(()=>{{ main.src=src; main.style.opacity=1; }},150);
    document.querySelectorAll('.gal__thumbs button').forEach(x=>x.classList.toggle('on',x===b));
  }}));
  /* build tabs */
  document.querySelectorAll('.tabs button').forEach(b=>b.addEventListener('click',()=>{{
    document.querySelectorAll('.tabs button').forEach(x=>x.classList.toggle('on',x===b));
    document.querySelectorAll('.bpanel').forEach(p=>p.classList.toggle('on',p.dataset.b===b.dataset.b));
  }}));
  /* price from /models.js */
  const el=document.getElementById('pdPrice');
  const md=(window.MODELS||[]).find(x=>x.slug===el.dataset.slug)||{{}};
  const FROM={{ko:w=>w+' 부터',en:w=>'From '+w,ja:w=>w+'〜',zh:w=>w+' 起'}};
  const ASK={{ko:'가격 문의',en:'Price on request',ja:'価格はお問い合わせください',zh:'价格请咨询'}};
  const won=n=>'₩'+Number(n).toLocaleString('ko-KR');
  function price(){{ const L=document.documentElement.lang||'ko';
    el.textContent = md.price ? (md.from ? FROM[L](won(md.price)) : won(md.price)) : ASK[L];
    el.classList.toggle('ask',!md.price); }}
  price();
  document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setTimeout(price,0)));
}});
</script>
"""

# ---------------------------------------------------------------- page objects for build.py
def _page(m):
    n = m['name']
    return SimpleNamespace(
        SLUG=m['slug'],
        TITLE_KO=f'Moulton {n} | 몰튼 바이시클 코리아',
        TITLES_JS="{ko:'Moulton %s | 몰튼 바이시클 코리아', en:'Moulton %s | Moulton Bicycles Korea', ja:'Moulton %s | モールトン・バイシクル・コリア', zh:'Moulton %s | 莫尔顿自行车韩国'}" % (n, n, n, n),
        DESCRIPTION=html.escape(m['desc'][0][:150], quote=True),
        OG_TITLE=f'Moulton {n} | Moulton Bicycles Korea',
        OG_DESC=html.escape(m['tag'][0] + ' · ' + m['tag'][1], quote=True),
        OG_IMAGE='https://www.moultonbicycles.co.uk/cdn/shop/files/' + m['hero'],
        CSS=CSS,
        main=(lambda m=m: render(m)),
    )

PAGES = [_page(m) for m in MODELS]
