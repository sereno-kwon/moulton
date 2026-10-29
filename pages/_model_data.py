# -*- coding: utf-8 -*-
"""몰튼 모델 페이지 데이터 (UK 제품 페이지 기준, 2026-10).
   pages/models.py 가 읽어 /<slug>/index.html 을 생성.

   각 모델:
     slug, name, series(표시용), icons(기능 아이콘 키), lead(영국 공장 생산 리드타임)
     hero / gallery / details / lifestyle : UK CDN 파일명
     tag, desc : (ko, en, ja, zh)
     key   : 프레임 핵심 사양  "라벨: 값" 줄 단위
     builds: 빌드 이름 목록
     spec  : 빌드 사양 "라벨: 값1 | 값2 | ..." (빌드 순서, 값이 하나면 전 빌드 공통)
   가격은 /models.js 에서 관리."""

MODELS = [
# ------------------------------------------------------------------ NEW SERIES
dict(
  slug='ns-double-pylon', name='NS D-Pylon', series='New Series', lead='8–10',
  icons=['hydrolastic', 'flexitor', '20', 'separable'],
  hero='moulton-ns-double-pylon-stainless-hall-lawn-2.jpg',
  gallery=['moulton-ns-double-pylon-stainless.jpg', 'moulton-ns-double-pylon-stainless-angle-1.jpg', 'moulton-ns-double-pylon-stainless-angle-2.jpg'],
  details=['moulton-speed-polished-stainless-centre-frame-section-close-up.jpg'],
  lifestyle=['moulton-ns-double-pylon-stainless-hall-lawn.jpg'],
  tag=('뉴 시리즈의 정점', 'The pinnacle of the New Series', 'ニューシリーズの頂点', 'New Series 的巅峰之作'),
  desc=(
    "NS D-Pylon은 뉴 시리즈의 최상위 모델이자, 몰튼 스페이스프레임이 구조적으로 가장 응축된 형태입니다. 항공우주 등급 스테인리스 스틸로 만들고 손으로 연마해 거울 같은 광택을 냈습니다. 일반적인 시트 튜브와 헤드 튜브 자리에 스테인리스 '파일런'이 들어서고, 하중은 실버 브레이징으로 이은 가는 튜브들을 따라 흐릅니다. 일체형 리어 포크, 하이드로라스틱 리어 서스펜션, 플렉시터 프론트 서스펜션은 그대로 이어받았습니다.",
    "The NS D-Pylon is the flagship of the New Series and the most structurally concentrated form of the Moulton spaceframe. It is built from aerospace-grade stainless steel and hand-polished to a mirror finish. Stainless ‘pylons’ take the place of the conventional seat tube and head tube, and loads run through small-diameter tubes joined by silver brazing. The unified rear fork, Hydrolastic® rear suspension and Flexitor® front suspension are retained.",
    "NS D-Pylonはニューシリーズの最上位モデルであり、モールトンのスペースフレームが構造的に最も凝縮された形です。航空宇宙グレードのステンレススチールで作られ、手作業で鏡面に磨き上げられています。一般的なシートチューブとヘッドチューブの位置にはステンレスの「パイロン」が置かれ、荷重はシルバーブレージングで接合された細径チューブを通って流れます。一体型リアフォーク、ハイドロラスティック・リアサスペンション、フレキシター・フロントサスペンションはそのまま受け継いでいます。",
    "NS D-Pylon 是 New Series 的旗舰，也是莫尔顿空间桁架在结构上最为凝练的形态。车架采用航空级不锈钢打造，并经手工抛光至镜面效果。不锈钢“塔柱”取代了传统的座管与头管，载荷沿着以银焊连接的细径管件传递。一体式后叉、Hydrolastic® 后避震与 Flexitor® 前避震均予以保留。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Flexitor®
Rear Suspension: Hydrolastic®
Separability: Separable
Frame Coupling: Kingpin + stainless locknut
Frame Material: Aerospace stainless steel and Reynolds 931 stainless steel (forks)
Frame Construction: Silver fillet brazed. Twin tube 'pylon' seat mast and head tube. Tubular zig-zags.
Bottle Mounts: 2 sets: front and rear of 'Pylon' seat mast
Frame Finish: Polished Stainless''',
  builds=['Campagnolo Super Record 2x12'],
  spec='''
Ride Category: Road & Race
Brake Type: Caliper
Handlebar Type: Drop
Gear System: Derailleur
Front Mech: Campagnolo Super Record
Rear Mech: Campagnolo Super Record
Crankset: Campagnolo Super Record Carbon Ti 53/39
Cassette: Moulton CNC 10-30 12 speed CrMo/Ti/Al
Chain: Connex 12s0
Bottom Bracket: Campagnolo Ultra-Torque (ceramic)
Gear Range (inches): 26-99" (53/39t)
Brakes: TRP RG957 sidepull 57 caliper
Gear/Brake Levers: Campagnolo Super Record
Handlebar: Deda Speciale classic drop (44 or 42 o-o)
Tapes/Grips: Brooks Leather Antique Brown
Handlebar Stem: Moulton Wishbone Q (100, 150 or 170mm)
Headset: Moulton custom lightweight 1" sealed
Saddle: Brooks B17 Ti Leather Antique Brown
Seatpost: 2-bolt forged AL in-line, 27.2x350
Tyres: Schwalbe One (folding) 28-406
Rims: Moulton MT20 Black (CNC brake track)
Rear Hub: Moulton custom forged 28h silver
Front Hub: Moulton custom forged 28h silver 70mm
Spokes: Sapim Laser/Force butted (differential)
Mudguards: Available as accessory
Mudguard Clearance: Up to 28mm tyre section
Pedals: none supplied
Weight: 10.1 kg / 22.3 lb'''),

dict(
  slug='ns-speed', name='NS Speed', series='New Series', lead='8–10',
  icons=['hydrolastic', 'flexitor', '20', 'fixed'],
  hero='moulton-ns-speed-stainless-stone-pillars.jpg',
  gallery=['moulton-ns-speed-stainless.jpg', 'moulton-ns-speed-stainless-angle-1.jpg', 'moulton-ns-speed-stainless-angle-2.jpg'],
  details=['moulton-speed-polished-stainless-centre-frame-section-close-up.jpg'],
  lifestyle=['moulton-ns-speed-stainless-iron-grates.jpg'],
  tag=('가장 가벼운 일체형 뉴 시리즈', 'The lightest fixed-frame New Series', '最も軽い一体型ニューシリーズ', '最轻的固定车架 New Series'),
  desc=(
    "NS Speed는 뉴 시리즈에서 가장 가벼운 일체형 프레임 모델이자 파일런 설계 중 하나로, 몰튼 스페이스프레임의 가장 응축된 형태를 보여 줍니다. 항공우주 등급 스테인리스 스틸에 손으로 거울 광택을 냈고, 일반 시트 튜브 대신 제작된 싱글 파일런 기둥을 썼습니다. 구조적 연속성을 극대화하기 위해 분리되지 않는 프레임으로 만들었으며, 일체형 리어 포크와 하이드로라스틱 리어, 플렉시터 프론트 서스펜션을 갖췄습니다. 지속적인 속도를 위해 정밀하게 다듬은 로드 머신입니다.",
    "The NS Speed is the lightest fixed-frame model in the New Series and one of the pylon designs, the most structurally concentrated expression of the Moulton spaceframe. Built from aerospace-grade stainless steel and hand-polished to a mirror finish, it replaces the conventional seat tube with a fabricated single pylon column. The frame is non-separable to maximise structural continuity, and keeps the unified rear fork, Hydrolastic® rear and Flexitor® front suspension. A road machine, exacting in structure and refined in material, built for sustained speed.",
    "NS Speedはニューシリーズで最も軽い一体型フレームモデルで、パイロン設計の一つとして、モールトンのスペースフレームの最も凝縮された形を示します。航空宇宙グレードのステンレススチールを手作業で鏡面仕上げし、一般的なシートチューブの代わりに製作されたシングルパイロンの支柱を採用しました。構造の連続性を最大化するため非分割式とし、一体型リアフォーク、ハイドロラスティック・リア、フレキシター・フロントサスペンションを備えています。持続するスピードのために精密に仕上げられたロードマシンです。",
    "NS Speed 是 New Series 中最轻的固定车架车型，也是塔柱设计之一，体现了莫尔顿空间桁架最凝练的形态。车架以航空级不锈钢制造并手工抛光至镜面，以定制的单塔柱取代传统座管。为最大化结构连续性，车架不可拆分，并保留一体式后叉、Hydrolastic® 后避震与 Flexitor® 前避震。这是一台结构严谨、用料考究、为持续高速而生的公路机器。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Flexitor®
Rear Suspension: Hydrolastic®
Separability: Fixed
Frame Material: Aerospace stainless steel and Reynolds 931 stainless steel (forks)
Frame Construction: Silver fillet brazed. Twin tube 'pylon' seat mast. Tubular zig-zags.
Bottle Mounts: 2 sets: front and rear of 'Pylon' seat mast
Frame Finish: Polished Stainless''',
  builds=['Campagnolo Super Record 2x12'],
  spec='''
Ride Category: Road & Race
Brake Type: Caliper
Handlebar Type: Drop
Gear System: Derailleur
Front Mech: Campagnolo Super Record
Rear Mech: Campagnolo Super Record
Crankset: Campagnolo Super Record Carbon Ti 53/39
Cassette: Moulton CNC 10-30 12 speed CrMo/Ti/Al
Chain: Connex 12s0
Bottom Bracket: Campagnolo Ultra-Torque (ceramic)
Gear Range (inches): 26-99" (53/39t)
Brakes: TRP RG957 sidepull 57 caliper
Gear/Brake Levers: Campagnolo Super Record
Handlebar: Deda Zero100 RHM BoB (42 o-o)
Tapes/Grips: Brooks Cambium Rubber
Handlebar Stem: Custom Titanium (80, 100, 125 or 150mm)
Headset: Moulton custom lightweight 1" sealed
Saddle: Fizik Antares
Seatpost: 2-bolt forged AL in-line, 27.2x350
Tyres: Schwalbe One (folding) 28-406
Rims: Moulton MT20 Black (CNC brake track)
Rear Hub: Moulton custom forged 28h silver
Front Hub: Moulton custom forged 28h silver 70mm
Spokes: Sapim Laser/Force butted (differential)
Mudguards: Available as accessory
Mudguard Clearance: Up to 28mm tyre section
Pedals: none supplied
Weight: 9.5 kg / 20.9 lb'''),

dict(
  slug='ns-rapide', name='NS Rapide', series='New Series', lead='4–6',
  icons=['hydrolastic', 'flexitor', '20', 'separable'],
  hero='moulton-ns-rapide-stone-pillar-lane-trees.jpg',
  gallery=['moulton-ns-rapide-sunrise-orange.jpg', 'moulton-ns-rapide-sunrise-orange-angle-1.jpg', 'moulton-ns-rapide-sunrise-orange-angle-2.jpg'],
  details=['moulton-ns-rapide-centre-joint-frame-signature.jpg', 'moulton-ns-rapide-headbadge-close-up.jpg', 'moulton-ns-rapide-rear-suspension-valve.jpg', 'moulton-ns-rapide-superlight-seat-pillar.jpg', 'moulton-ns-rapide-rear-fork-details.jpg'],
  lifestyle=['moulton-ns-rapide-stone-wall-light-gravel-path.jpg'],
  tag=('가장 진보한 로드 몰튼', "Moulton's most advanced road bike", '最も先進的なロード・モールトン', '莫尔顿最先进的公路车'),
  desc=(
    "NS Rapide는 지금까지 나온 몰튼 중 가장 기술적으로 진보한 로드 지향 모델로, 퍼포먼스 로드와 올로드 주행을 위해 만들어졌습니다. 다듬어진 뉴 시리즈 분리형 스페이스프레임을 바탕으로 더 큰 451mm 휠을 쓰고, 에어로 카본 휠과 최신 12·13단 로드 구동계를 지원합니다. 고속 안정성과 정밀함, 효율이 한층 높아졌습니다. 여러 특수강을 조합한 프레임은 지금까지의 분리형 뉴 시리즈 중 가장 가볍습니다.",
    "The NS Rapide is the most technically advanced road-oriented Moulton to date, built for performance road and all-road riding. Based on a refined New Series separable spaceframe, it moves to a larger 451mm wheel, comes with aerodynamic carbon wheels and accepts the latest 12- and 13-speed road drivetrains, for greater stability, precision and efficiency at speed. Its blend of specialist steels makes it the lightest separable New Series model yet.",
    "NS Rapideは、これまでのモールトンの中で最も技術的に先進的なロード志向モデルで、パフォーマンスロードとオールロード走行のために作られました。改良されたニューシリーズの分割式スペースフレームをベースに、より大きな451mmホイールを採用し、エアロカーボンホイールと最新の12・13速ロードドライブトレインに対応。高速域での安定性、精度、効率が一段と高まりました。複数の特殊鋼を組み合わせたフレームは、分割式ニューシリーズ史上最軽量です。",
    "NS Rapide 是迄今技术最先进的公路取向莫尔顿，专为性能公路与全路况骑行打造。它基于改良的 New Series 可拆分空间桁架，采用更大的451mm车轮，配备空气动力学碳纤维轮组，并兼容最新的12速与13速公路传动系统，高速稳定性、精准度与效率更上一层楼。多种特种钢材组合的车架，使其成为迄今最轻的可拆分 New Series 车型。"),
  key='''
Wheel Size: 20" (451mm) / 20" (406mm)
Front Suspension: Flexitor®
Rear Suspension: Hydrolastic®
Separability: Separable
Frame Coupling: Kingpin + stainless locknut
Frame Material: Columbus Spirit, Kaisei NiCrMo and Reynolds 853 steels (stainless steel dropouts)
Frame Construction: Fillet-brazed with 'shot-in' tubes. Tubular zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Stove Enamel''',
  builds=['Campagnolo Super Record 2x13 WRL'],
  spec='''
Ride Category: Road & Race
Brake Type: Hydraulic Disc
Handlebar Type: Drop
Gear System: Wireless Derailleur
Front Mech: Campagnolo Super Record 13
Rear Mech: Campagnolo Super Record 13
Crankset: Campagnolo Super Record 13 Carbon Ti 55/39
Cassette: Campagnolo SR13 10-29
Chain: Campagnolo
Bottom Bracket: Campagnolo Qck-Tech
Gear Range (inches): 27-110" (55/39t)
Brakes: Campagnolo Super Record 13 Disc
Gear/Brake Levers: Campagnolo Super Record 13
Handlebar: Deda SuperZero RS or Deda Gravel 100 (40 o-o)
Tapes/Grips: Brooks Cambium Rubber
Handlebar Stem: Custom Titanium (80, 100, 125 or 150mm)
Headset: Tange Seiki RDC 1 1/8" sealed
Saddle: Fizik Antares
Seatpost: Moulton Superlight alloy 34.9 "M" seat pillar, in-line head
Tyres: Schwalbe SX-R 30-451 or Schwalbe G-One Speed 32-451
Rims: 'M' Deep Section Carbon (50mm)
Rear Hub: Miche RDX 28 N3W black
Front Hub: Miche RDX 28 black
Spokes: Sapim Laser/Force butted (differential)
Mudguards: Available as accessory
Mudguard Clearance: Up to 35mm tyre section
Pedals: none supplied
Weight: 9.9 kg / 21.8 lb'''),

dict(
  slug='ns-safari', name='NS Safari', series='New Series', lead='4–6',
  icons=['hydrolastic', 'flexitor', '20', 'separable'],
  hero='moulton-ns-safari-willow-green-green-wood-wall.jpg',
  gallery=['moulton-ns-safari-willow-green.jpg', 'moulton-ns-safari-willow-green-angle-1.jpg', 'moulton-ns-safari-willow-green-angle-2.jpg'],
  details=[],
  lifestyle=['moulton-ns-safari-willow-green-side-view-landscape.jpg', 'moulton-ns-safari-touring-bags-big-tyres-grey-bg.jpg'],
  tag=('뉴 시리즈의 그래블·탐험 모델', 'The New Series for gravel and expedition', 'グラベルと冒険のためのニューシリーズ', '为砂石与远征而生的 New Series'),
  desc=(
    "NS Safari는 뉴 시리즈의 오프로드·그래블 모델로, 포장도로를 넘어 자갈길과 거친 시골길, 탐험 지형까지 달리는 라이더를 위한 자전거입니다. 뉴 시리즈 스페이스프레임과 플렉시터 프론트, 하이드로라스틱 리어 서스펜션은 그대로 두고, 유압 디스크 브레이크와 넓어진 타이어 클리어런스, 최신 1x 구동계를 더했습니다. 새 지오메트리와 스루액슬, 넓어진 리어 허브 간격이 느슨하거나 고르지 않은 노면에서 제어력과 안정성, 제동 정밀도를 높여 바이크패킹과 장거리 투어링을 받쳐 줍니다.",
    "The NS Safari is the off-road and gravel member of the New Series, for riders whose routes run beyond tarmac onto gravel, rough lanes and expedition terrain. It keeps the New Series spaceframe with Flexitor® front and Hydrolastic® rear suspension, and adds hydraulic disc brakes, greater tyre clearance and a modern 1x drivetrain. Revised geometry, thru-axles and wider rear hub spacing bring more control, stability and braking precision on loose or uneven ground, ready for bikepacking and long-distance touring.",
    "NS Safariはニューシリーズのオフロード／グラベルモデルで、舗装路を越えて砂利道や荒れた田舎道、冒険の地形まで走るライダーのための一台です。ニューシリーズのスペースフレームとフレキシター・フロント、ハイドロラスティック・リアサスペンションはそのままに、油圧ディスクブレーキ、広いタイヤクリアランス、最新の1xドライブトレインを加えました。見直されたジオメトリー、スルーアクスル、広いリアハブ幅が、緩い路面や荒れた路面でのコントロール、安定性、制動精度を高め、バイクパッキングや長距離ツーリングを支えます。",
    "NS Safari 是 New Series 中的越野与砂石车型，专为骑出柏油路、驶向砂石路、崎岖小道乃至远征地形的骑行者打造。它保留 New Series 空间桁架以及 Flexitor® 前避震与 Hydrolastic® 后避震，并加入液压碟刹、更大的轮胎间隙与现代1x传动。改良的几何、桶轴与更宽的后花鼓间距，使其在松散或不平路面上拥有更好的操控、稳定与制动精度，胜任自行车露营与长途旅行。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Flexitor®
Rear Suspension: Hydrolastic®
Separability: Separable
Frame Coupling: Kingpin + stainless locknut
Frame Material: Columbus Spirit, Kaisei NiCrMo and Reynolds 853 steels (stainless steel dropouts)
Frame Construction: Fillet-brazed with 'shot-in' tubes. Tubular zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Hybrid (Powder/Enamel)''',
  builds=['Campagnolo Ekar 1x13'],
  spec='''
Ride Category: Gravel & Off-road; Touring & Adventure
Brake Type: Hydraulic Disc
Handlebar Type: Drop
Gear System: Derailleur
Front Mech: n/a
Rear Mech: Campagnolo Ekar
Crankset: Campagnolo Ekar 44t
Cassette: Campagnolo 13x 9-36
Chain: Campagnolo
Bottom Bracket: Campagnolo Pro-Tech
Gear Range (inches): 23-93" (44t)
Brakes: Campagnolo Ekar Disc
Gear/Brake Levers: Campagnolo Ekar
Handlebar: Deda Gravel 100 (40 o-o)
Tapes/Grips: Brooks Cambium Rubber
Handlebar Stem: Custom Titanium (80, 100, 125 or 150mm)
Headset: Tange Seiki RDC 1 1/8" sealed
Saddle: Selle San Marco Regal Evo
Seatpost: Moulton Titanium, 34.9 dia, layback head
Tyres: Schwalbe G-One Speed 40-406
Rims: Moulton DTR20 Black (tubeless ready)
Rear Hub: Miche RDX 28 N3W black
Front Hub: Miche RDX 28 black
Spokes: Sapim Laser/Force butted (differential)
Mudguards: Available as accessory
Mudguard Clearance: Up to 40mm tyre section
Pedals: none supplied
Weight: 10 kg / 22.1 lb'''),

dict(
  slug='ns-marathon', name='NS Marathon', series='New Series', lead='6–8',
  icons=['hydrolastic', 'flexitor', '20', 'separable'],
  hero='moulton-ns-marathon-willow-green-hl-metal-wall.jpg',
  gallery=['moulton-ns-marathon-stainless-blue-hl.jpg', 'moulton-ns-marathon-stainless-blue-hl-angle-1.jpg'],
  details=[],
  lifestyle=['moulton-ns-marathon-willow-green-hl-metal-wall-side.jpg'],
  tag=('장거리를 위한 뉴 시리즈', 'The long-distance New Series', '長距離のためのニューシリーズ', '为长距离而生的 New Series'),
  desc=(
    "NS Marathon은 뉴 시리즈의 장거리 모델입니다. 풀 스토브 에나멜 마감, 또는 에나멜 하이라이트를 더한 폴리시드 스테인리스 두 가지로 만들어집니다. 일체형 리어 포크와 하이드로라스틱 리어, 플렉시터 프론트 서스펜션을 갖췄고, 프레임은 특수강 또는 항공우주 등급 스테인리스 중에서 고를 수 있습니다. 최고 성능보다는 먼 거리를 꾸준히 달리는 안정감에 초점을 맞춘 자전거입니다.",
    "The NS Marathon is the long-distance model of the New Series, offered in full stove enamel or in polished stainless steel with enamel highlights. It keeps the unified rear fork, Hydrolastic® rear and Flexitor® front suspension, with frames in specialist steel or aerospace-grade stainless. Built for long, high-mileage road riding, it puts composure over distance ahead of outright performance.",
    "NS Marathonはニューシリーズの長距離モデルです。フル・ストーブエナメル仕上げ、またはエナメルのハイライトを加えたポリッシュドステンレスの2種類で製作されます。一体型リアフォーク、ハイドロラスティック・リア、フレキシター・フロントサスペンションを備え、フレームは特殊鋼または航空宇宙グレードのステンレスから選べます。最高性能よりも、長い距離を安定して走り続けることに焦点を当てた一台です。",
    "NS Marathon 是 New Series 的长距离车型，提供全烤漆涂装，或带烤漆点缀的抛光不锈钢两种版本。它保留一体式后叉、Hydrolastic® 后避震与 Flexitor® 前避震，车架可选特种钢或航空级不锈钢。专为高里程长途公路骑行打造，追求的是长距离下的从容稳定，而非极致性能。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Flexitor®
Rear Suspension: Hydrolastic®
Separability: Separable
Frame Coupling: Kingpin + stainless locknut
Frame Material: Reynolds 853 (forks) with Aerospace stainless steel or Columbus Spirit/Kaisei NiCrMo
Frame Construction: Fillet brazed (with silver for stainless frame) with 'shot-in' tubes. Tubular zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Polished Stainless w/ Enamel Highlights or Stove Enamel''',
  builds=['Campagnolo Chorus 2x12', 'Shimano Alfine 11'],
  spec='''
Ride Category: Road & Race; Touring & Adventure; City & Leisure
Brake Type: Caliper
Handlebar Type: Drop | Flat
Gear System: Derailleur | Hub
Front Mech: Campagnolo Chorus | n/a
Rear Mech: Campagnolo Chorus | n/a
Crankset: Campagnolo Chorus Carbon 52/36 | Shimano Alfine 45t w/chainguard
Cassette: Moulton CNC 10-30 12 speed CrMo/Ti/Al | 17t
Chain: Connex 12s0 | Connex 900 9 speed
Bottom Bracket: Campagnolo Ultra-Torque | Shimano Hollowtech II
Gear Range (inches): 24-97" (52/36t) | 26-106" (45t)
Brakes: TRP RG957 sidepull 57 caliper
Gear/Brake Levers: Campagnolo Chorus | Tektro FL750 / Shimano Alfine rapidfire
Handlebar: Deda Speciale classic drop (44 or 42 o-o) | M Special flat bar
Tapes/Grips: Brooks Leather Antique Brown | Brooks Cambium Ergonomic
Handlebar Stem: Moulton Wishbone Q (100, 150 or 170mm)
Headset: Moulton custom lightweight 1" sealed
Saddle: Brooks B17 Ti Leather Antique Brown | Selle San Marco Regal Short Dynamic 165
Seatpost: Moulton / Reynolds Titanium, layback
Tyres: Schwalbe One (folding) 28-406
Rims: Moulton MT20 Black (CNC brake track)
Rear Hub: Moulton custom forged 28h silver | Shimano Alfine 11 speed 32h silver
Front Hub: Moulton custom forged 28h silver 70mm
Spokes: Sapim Laser/Force butted (differential) | Sapim Laser butted front/PG rear
Mudguards: Available as accessory
Mudguard Clearance: Up to 28mm tyre section
Pedals: none supplied | MKS Promenade q/r
Weight: 10.1 kg / 22.3 lb | 11.1 kg / 24.5 lb'''),

# ------------------------------------------------------------------ MOULTON
dict(
  slug='speed', name='Speed', series='Moulton', lead='4–6',
  icons=['hydrolastic', 'leadinglink', '20', 'fixed'],
  hero='moulton-speed-stainless-stone-wall.jpg',
  gallery=['moulton-speed-stainless.jpg', 'moulton-speed-stainless-angle-1.jpg', 'moulton-bike-speed-stainless-campagnolo-super-record-22-back-angle.jpg'],
  details=['moulton-speed-polished-stainless-centre-frame-section-close-up.jpg'],
  lifestyle=['moulton-speed-stainless-wood-wall.jpg'],
  tag=('가장 가볍고 가장 로드에 집중한 몰튼', 'The lightest, most road-focused Moulton', '最も軽く、最もロードに特化したモールトン', '最轻、最专注公路的莫尔顿'),
  desc=(
    "SPEED는 몰튼에서 가장 가볍고 가장 로드에 집중한 모델입니다. 타협 없이 만든 일체형 올 스테인리스 스페이스프레임으로, 콜럼버스 XCr과 항공우주 스테인리스 스틸을 써서 손이 많이 가는 방식으로 제작합니다. 실버 브레이징 후 손으로 거울 광택을 냈고, 짧은 스트로크의 프론트 서스펜션과 하이드로라스틱 리어 서스펜션은 승차감을 무르게 만들지 않으면서도 제어력을 줍니다. 효율과 강성, 기계적 명료함을 응축한 진정한 스피드·레이스 모델입니다.",
    "The SPEED is Moulton's lightest and most road-focused model: a fixed-frame, all-stainless spaceframe built without compromise. Labour-intensive construction in Columbus XCr and aerospace stainless steels is silver-brazed and hand-polished to a mirror finish. Short-stroke front suspension and Hydrolastic® rear suspension provide control without softening the ride. A true speed and race model, distilled for efficiency, stiffness and mechanical clarity.",
    "SPEEDはモールトンで最も軽く、最もロードに特化したモデルです。妥協なく作られた一体型オールステンレスのスペースフレームで、コロンバスXCrと航空宇宙ステンレススチールを用い、手間のかかる工程で製作されます。シルバーブレージングの後、手作業で鏡面に磨き上げ、ショートストロークのフロントサスペンションとハイドロラスティック・リアサスペンションが、乗り味を柔らかくしすぎることなく確かなコントロールをもたらします。効率、剛性、機械としての明快さを凝縮した真のスピード／レースモデルです。",
    "SPEED 是莫尔顿最轻、最专注公路的车型：一款毫不妥协的固定式全不锈钢空间桁架。车架采用 Columbus XCr 与航空级不锈钢，以费时费工的方式制造，经银焊后手工抛光至镜面。短行程前避震与 Hydrolastic® 后避震在不使骑行变软的前提下提供精准控制。这是一款将效率、刚性与机械纯粹性凝聚于一身的真正竞速车型。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Leading Link (crown)
Rear Suspension: Hydrolastic®
Separability: Fixed
Frame Material: Columbus XCr, Reynolds 921 (fork), and Aerospace stainless steels
Frame Construction: Silver fillet brazed with 'shot-in' tubes. Tubular zig-zags.
Bottle Mounts: 1 set: seat tube
Frame Finish: Polished Stainless''',
  builds=['Campagnolo Super Record 2x12'],
  spec='''
Ride Category: Road & Race
Brake Type: Caliper
Handlebar Type: Drop
Gear System: Derailleur
Front Mech: Campagnolo Super Record
Rear Mech: Campagnolo Super Record
Crankset: Campagnolo Super Record Carbon Ti 53/39
Cassette: Moulton CNC 10-30 12 speed CrMo/Ti/Al
Chain: Connex 12s0
Bottom Bracket: Campagnolo Ultra-Torque (ceramic)
Gear Range (inches): 26-99" (53/39t)
Brakes: Campagnolo Super Record
Gear/Brake Levers: Campagnolo Super Record
Handlebar: Deda Zero100 RHM BoB (42 o-o)
Tapes/Grips: Brooks Cambium Rubber
Handlebar Stem: Custom Titanium (80, 100, 125 or 150mm)
Headset: Moulton custom lightweight 1" sealed
Saddle: Fizik Antares
Seatpost: Moulton 953, in-line head
Tyres: Schwalbe One (folding) 28-406
Rear Hub: Moulton custom forged 28h silver
Front Hub: Moulton custom forged 28h silver
Spokes: Sapim Laser/Force butted (differential)
Mudguards: n/a
Mudguard Clearance: n/a
Pedals: none supplied
Weight: 9 kg / 19.8 lb'''),

# ------------------------------------------------------------------ AM SERIES
dict(
  slug='am-gt', name='AM GT', series='AM Series', lead='6–8',
  icons=['hydrolastic', 'leadinglink', '17', 'separable'],
  hero='moulton-am-gt-stainless-lane-grass-lawn.jpg',
  gallery=['moulton-gt-mk3-stainless.jpg', 'moulton-gt-mk3-stainless-angle-1.jpg'],
  details=[],
  lifestyle=['moulton-am-gt-bike-polished-stainless-with-cyclist-woods.jpg'],
  tag=('올 스테인리스 그랜드 투어러', 'The all-stainless Grand Tourer', 'オールステンレスのグランドツアラー', '全不锈钢长途旅行车'),
  desc=(
    "AM GT는 오리지널 AM(Advanced Engineering) 자전거의 올 스테인리스 버전입니다. 17인치 휠과 클래식 스페이스프레임, 비일체형 리어 포크 구성은 그대로 두고, 전체를 스테인리스로 제작하고 하이드로라스틱 리어 서스펜션을 더했습니다. 실버 브레이징 후 손으로 연마한 프레임은 구조적 정밀함과 장거리 고속 주행의 안정적인 핸들링을 함께 갖췄습니다. 많은 오너들이 이 자전거로 세계를 여행했습니다.",
    "The AM GT is the all-stainless version of the original AM (Advanced Engineering) bicycle. It keeps the 17-inch wheel format, the classic spaceframe and the non-unified rear fork, and adds all-stainless fabrication and Hydrolastic® rear suspension. Silver-brazed and hand-polished, it balances structural precision with stable high-speed handling over long distances: a material refinement of the AM, tuned for sustained high-mileage road riding. Many owners have travelled the world on one.",
    "AM GTは、オリジナルAM（Advanced Engineering）自転車のオールステンレス版です。17インチホイール、クラシックなスペースフレーム、非一体型リアフォークという構成はそのままに、全体をステンレスで製作し、ハイドロラスティック・リアサスペンションを加えました。シルバーブレージング後に手作業で磨き上げたフレームは、構造の精密さと長距離高速走行での安定したハンドリングを両立しています。多くのオーナーがこの一台で世界を旅してきました。",
    "AM GT 是原版 AM（Advanced Engineering）自行车的全不锈钢版本。它保留17英寸车轮、经典空间桁架与非一体式后叉的配置，并以全不锈钢制造，加入 Hydrolastic® 后避震。车架经银焊并手工抛光，兼具结构上的精密与长途高速下的稳定操控。许多车主骑着它环游了世界。"),
  key='''
Wheel Size: 17"
Front Suspension: Leading Link (crown)
Rear Suspension: Hydrolastic®
Separability: Separable
Frame Coupling: Kingpin + stainless locknut
Frame Material: Columbus XCr, Reynolds 921 (fork), and Aerospace stainless steels
Frame Construction: Silver fillet brazed with 'shot-in' tubes. Tubular zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Polished Stainless''',
  builds=['Campagnolo Centaur 2x11', 'Shimano Alfine 11'],
  spec='''
Ride Category: Road & Race; Touring & Adventure | City & Leisure
Brake Type: Caliper
Handlebar Type: Drop | Flat
Gear System: Derailleur | Hub
Front Mech: Campagnolo Centaur Black | n/a
Rear Mech: Campagnolo Centaur Black | n/a
Crankset: Campagnolo Centaur Black 52/36 or 58/44 | Shimano Alfine 45t w/chainguard
Cassette: Moulton 9-32 | 16t
Chain: Connex 11sX | Connex 900 9 speed
Bottom Bracket: Campagnolo Ultra-Torque | Shimano Hollowtech II
Gear Range (inches): 19-99" (52/36t) or 23-109" (58/44t) | 23-103" (45t)
Brakes: Tektro R539 DP 57 caliper
Gear/Brake Levers: Campagnolo Centaur Black | Tektro FL750 / Shimano Alfine rapidfire
Handlebar: Deda Speciale classic drop (44 or 42 o-o) | M Special flat bar
Tapes/Grips: Brooks Leather Antique Brown | Brooks Cambium Ergonomic
Handlebar Stem: Moulton Wishbone Q (100, 150 or 170mm)
Headset: Moulton custom lightweight 1" sealed
Saddle: Brooks B17 Ti Leather Antique Brown | Selle San Marco Regal Short Dynamic 165
Seatpost: Moulton / Reynolds Titanium, layback
Tyres: Schwalbe Kojak (Kevlar) 32-369
Rims: Moulton M17 Silver (CNC brake track)
Rear Hub: Moulton custom forged 28h silver | Shimano Alfine 11 speed 32h silver
Front Hub: Moulton custom forged 28h silver
Spokes: Sapim Laser/Force butted (differential) | Sapim Laser butted front/PG rear
Mudguards: Available as accessory
Mudguard Clearance: Up to 32mm tyre section
Pedals: none supplied | MKS Promenade q/r
Weight: 10.2 kg / 22.5 lb | 11.2 kg / 24.7 lb'''),

dict(
  slug='jubilee', name='Jubilee', series='AM Series', lead='2–4',
  icons=['monosphere', 'leadinglink', '20', 'separable'],
  hero='moulton-jubilee-special-blue-stone-wall.jpg',
  gallery=['moulton-jubilee-ferrari-red.jpg', 'moulton-jubilee-ferrari-red-angle-1.jpg', 'moulton-jubilee-special-blue-frame-close-up.jpg'],
  details=[],
  lifestyle=[],
  tag=('몰튼 50주년 기념 모델', "Born for Moulton's 50th anniversary", 'モールトン50周年記念モデル', '为莫尔顿50周年而生'),
  desc=(
    "주빌리는 몰튼 자전거 50주년을 기념해 출시되었고, 지금은 라인업을 대표하는 모델이 되었습니다. 더 가벼운 특수 튜브와 구조적 개선을 더한 상위 스페이스프레임으로, 장거리에서 흔들림 없는 핸들링을 보여 줍니다. 1986년 오리지널 AM 스페이스프레임을 닮은 프레임 구성을 20인치 휠에 맞게 다시 설계하고 지오메트리를 다듬었습니다. 로드와 장거리 주행은 물론 투어링까지 소화하며, AM 시리즈의 엔지니어링 계보를 잇습니다.",
    "The Jubilee was launched to mark fifty years of the Moulton bicycle and has become a defining model of the range. A higher-tier version of the spaceframe, it uses lighter specialist tubing and structural refinements for steady handling over long distances. Its frame layout recalls the original 1986 AM spaceframe, redesigned for 20-inch wheels with refined geometry. Built for road and long-distance riding with real touring ability, it continues the engineering line of the AM series.",
    "ジュビリーはモールトン自転車の50周年を記念して発売され、今ではラインナップを代表するモデルとなりました。より軽い特殊チューブと構造的な改良を加えた上位のスペースフレームで、長距離でも揺るぎないハンドリングを見せます。1986年のオリジナルAMスペースフレームを思わせるフレーム構成を20インチホイール用に再設計し、ジオメトリーを洗練させました。ロードや長距離はもちろんツーリングもこなし、AMシリーズのエンジニアリングの系譜を受け継いでいます。",
    "Jubilee 为纪念莫尔顿自行车诞生五十周年而推出，如今已成为产品线的代表车型。它是空间桁架的高阶版本，采用更轻的特种管材与结构改良，长途骑行时操控稳健。车架布局令人想起1986年的原版 AM 空间桁架，并针对20英寸车轮重新设计、优化几何。它胜任公路与长途骑行，也具备真正的旅行能力，延续了 AM 系列的工程血脉。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Leading Link (crown)
Rear Suspension: Monosphere
Separability: Separable
Frame Coupling: Kingpin + stainless locknut
Frame Material: Columbus Spirit and Kaisei NiCroMo steels (stainless steel dropouts)
Frame Construction: Fillet-brazed with 'shot-in' tubes. Tubular zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Stove Enamel''',
  builds=['Campagnolo Centaur 2x11', 'Shimano Alfine 11', 'Shimano 105 2x11'],
  spec='''
Ride Category: Road & Race; Touring & Adventure | City & Leisure | Touring & Adventure; Road & Race
Brake Type: Caliper
Handlebar Type: Drop | Flat | Flat or Drop
Gear System: Derailleur | Hub | Derailleur
Front Mech: Campagnolo Centaur Black | n/a | Shimano 105
Rear Mech: Campagnolo Centaur Black | n/a | Shimano 105
Crankset: Campagnolo Centaur Black 52/36 or 58/44 | Shimano Alfine 45t w/chainguard | Shimano 105 53/39
Cassette: Moulton 10-32 | 17t | Moulton 10-32
Chain: Connex 11sX | Connex 900 9 speed | Connex 11sX
Bottom Bracket: Campagnolo Ultra-Torque | Shimano Hollowtech II | Shimano Hollowtech II
Gear Range (inches): 21-96" (52/36t) or 26-107" (58/44t) | 26-106" (45t) | 23-99" (53/39t)
Brakes: Tektro R539 DP 57 caliper
Gear/Brake Levers: Campagnolo Centaur Black | Tektro FL750 / Shimano Alfine rapidfire | Shimano 105
Handlebar: Deda Speciale classic drop (44 or 42 o-o) | M Special flat bar | GB Carter drop Bar (42 c-c)
Tapes/Grips: Brooks Cambium Rubber
Handlebar Stem: AL ahead stem (90, 110 or 135mm) | AL ahead stem (90, 110 or 135mm) | AL adjustable stem 110 / 31.8
Headset: Moulton custom lightweight 1" sealed
Saddle: Fizik Antares | Selle San Marco Regal Short Dynamic 165 | Selle San Marco Regal Short Dynamic 140
Seatpost: Moulton / Reynolds Titanium, layback
Tyres: Schwalbe One (folding) 28-406
Rims: Moulton MT20 Black (CNC brake track)
Rear Hub: Moulton custom forged 28h silver | Shimano Alfine 11 speed 32h silver | Moulton custom forged 28h silver
Front Hub: Moulton custom forged 28h silver | Moulton custom forged 28h silver 70mm | Moulton custom forged 28h silver
Spokes: Sapim Laser/Force butted (differential) | Sapim Laser butted front/PG rear | Sapim Laser/Force butted (differential)
Mudguards: Available as accessory
Mudguard Clearance: Up to 28mm tyre section
Pedals: none supplied | MKS Promenade q/r | none supplied
Weight: 10.2 kg / 22.5 lb | 11.2 kg / 24.7 lb | 10.3 kg / 22.7 lb'''),

dict(
  slug='am-speed', name='AM Speed', series='AM Series', lead='2–4',
  icons=['monosphere', 'leadinglink', '17', 'fixed'],
  hero='zeb-kyffin-riding-moulton-speed-monaco.jpg',
  gallery=['moulton-am-speed-white.jpg', 'moulton-am-speed-white-angle-1.jpg'],
  details=[],
  lifestyle=['moulton-am-speed-riden-by-richard-grigsby-1991.jpg'],
  tag=('레이스 어크로스 아메리카에서 태어난 몰튼', 'Born from Race Across America', 'レース・アクロス・アメリカから生まれたモールトン', '诞生于横越美国赛'),
  desc=(
    "AM SPEED는 오리지널 AM 몰튼의 일체형 레이싱 버전으로, 레이스 어크로스 아메리카를 염두에 두고 개발되었습니다. 17인치 휠과 클래식 AM 스페이스프레임 구성은 그대로 두면서 더 가볍고 날카로운 성능을 냈습니다. 레이놀즈 725와 카이세이 NiCrMo 스틸, 스테인리스 드롭아웃, 레이스용으로 조율한 서스펜션으로 장시간 고속 내구 주행을 위해 만들어졌습니다. 가장 직선적이고, 집중되고, 역사로 검증된 스피드 몰튼입니다.",
    "The AM SPEED is the fixed-frame racing version of the original AM Moulton, developed with Race Across America in mind. It keeps the 17-inch wheels and the classic AM spaceframe layout while being lighter and sharper. Reynolds 725 and Kaisei NiCrMo steels, stainless steel dropouts and race-tuned suspension make it a machine for sustained high-speed endurance riding: the most direct, focused and historically proven speed Moulton.",
    "AM SPEEDはオリジナルAMモールトンの一体型レーシングバージョンで、レース・アクロス・アメリカを念頭に開発されました。17インチホイールとクラシックなAMスペースフレームの構成はそのままに、より軽く、より鋭い性能を実現。レイノルズ725とカイセイNiCrMoスチール、ステンレスドロップアウト、レース向けに調整されたサスペンションにより、長時間の高速耐久走行のために作られています。最も直截で、研ぎ澄まされ、歴史に裏打ちされたスピード・モールトンです。",
    "AM SPEED 是原版 AM 莫尔顿的固定车架竞速版本，为横越美国赛（Race Across America）而开发。它保留17英寸车轮与经典 AM 空间桁架布局，同时更轻、更锐利。Reynolds 725 与 Kaisei NiCrMo 钢材、不锈钢勾爪与竞速调校的避震，使其专为持续高速耐力骑行而生：最直接、最专注、也最经历史验证的速度型莫尔顿。"),
  key='''
Wheel Size: 17"
Front Suspension: Leading Link (crown)
Rear Suspension: Monosphere
Separability: Fixed
Frame Material: Reynolds 725 and Kaisei NiCroMo steels (stainless steel dropouts)
Frame Construction: Fillet-brazed with 'shot-in' tubes. Tubular zig-zags.
Bottle Mounts: 1 set: seat tube
Frame Finish: Stove Enamel''',
  builds=['Campagnolo Centaur 2x11'],
  spec='''
Ride Category: Road & Race
Brake Type: Caliper
Handlebar Type: Drop
Gear System: Derailleur
Front Mech: Campagnolo Centaur Black
Rear Mech: Campagnolo Centaur Black
Crankset: Campagnolo Centaur Black 52/36 or 58/44
Cassette: Moulton 9-32
Chain: Connex 11sX
Bottom Bracket: Campagnolo Ultra-Torque
Gear Range (inches): 19-99" (52/36t) or 23-109" (58/44t)
Brakes: Tektro R539 DP 57 caliper
Gear/Brake Levers: Campagnolo Centaur Black
Handlebar: Deda Speciale classic drop (44 or 42 o-o)
Tapes/Grips: Brooks Cambium Rubber
Handlebar Stem: AL ahead stem (90, 110 or 135mm)
Headset: Moulton custom lightweight 1" sealed
Saddle: Fizik Antares
Seatpost: 2-bolt forged AL in-line, 27.2x350
Tyres: Schwalbe Kojak (Kevlar) 32-369
Rims: Moulton M17 Silver (CNC brake track)
Rear Hub: Moulton custom forged 28h silver
Front Hub: Moulton custom forged 28h silver
Spokes: Sapim Laser/Force butted (differential)
Mudguards: Available as accessory
Mudguard Clearance: Up to 32mm tyre section
Pedals: none supplied
Weight: 9.7 kg / 21.4 lb'''),

dict(
  slug='am-22', name='AM 22', series='AM Series', lead='2–4',
  icons=['monosphere', 'leadinglink', '17', 'separable'],
  hero='moulton-am-22-steely-grey-stone-pillars.jpg',
  gallery=['moulton-am-22-steely-grey.jpg', 'moulton-am-22-steely-grey-angle-1.jpg'],
  details=[],
  lifestyle=['moulton-am-22-bike-steely-grey-next-to-mossy-iron-grates.jpg'],
  tag=('1983년 AM 설계의 결정판', 'The definitive form of the 1983 AM', '1983年AM設計の決定版', '1983年 AM 设计的定型之作'),
  desc=(
    "AM 22는 1983년 오리지널 AM(Advanced Engineering) 설계를 분리형으로 이어 가는 모델입니다. 17인치 휠 플랫폼 위에 지은 스페이스프레임으로, 비일체형 리어 포크와 클래식 십자형 격자 구성을 유지해 높은 비틀림 강성과 장거리에서의 안정적인 핸들링을 냅니다. 특수 튜브와 마이터 조인트, 듀얼 리어 포크 업라이트로 만든 프레임은 로드와 내구 주행을 위한 것입니다. 오리지널 AM 설계의 결정판입니다.",
    "The AM 22 carries the original 1983 AM (Advanced Engineering) design forward in separable form. A spaceframe built around the 17-inch wheel platform, it retains the non-unified rear fork and the classic cruciform lattice for high torsional stiffness and stable handling over distance. Specialist tubing, mitred joints and dual rear fork uprights make it a machine for road and endurance riding: the definitive form of the original AM.",
    "AM 22は、1983年のオリジナルAM（Advanced Engineering）設計を分割式で受け継ぐモデルです。17インチホイールのプラットフォームの上に築かれたスペースフレームで、非一体型リアフォークとクラシックな十字格子構成を保ち、高いねじり剛性と長距離での安定したハンドリングを生みます。特殊チューブ、マイタージョイント、デュアルリアフォークアップライトで作られたフレームは、ロードと耐久走行のためのもの。オリジナルAM設計の決定版です。",
    "AM 22 以可拆分的形式延续了1983年原版 AM（Advanced Engineering）设计。这款空间桁架以17英寸车轮平台为基础，保留非一体式后叉与经典十字格构布局，带来出色的抗扭刚性与长途稳定操控。特种管材、斜接接头与双后叉立管构成的车架，专为公路与耐力骑行打造：原版 AM 的定型之作。"),
  key='''
Wheel Size: 17"
Front Suspension: Leading Link (crown)
Rear Suspension: Monosphere
Separability: Separable
Frame Coupling: Kingpin + stainless locknut
Frame Material: Columbus Spirit and Kaisei NiCroMo steels (stainless steel dropouts)
Frame Construction: Fillet-brazed with 'shot-in' tubes. Tubular zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Stove Enamel''',
  builds=['Campagnolo Centaur 2x11'],
  spec='''
Ride Category: Road & Race; Touring & Adventure
Brake Type: Caliper
Handlebar Type: Drop
Gear System: Derailleur
Front Mech: Campagnolo Centaur Black
Rear Mech: Campagnolo Centaur Black
Crankset: Campagnolo Centaur Black 52/36 or 58/44
Cassette: Moulton 9-32
Chain: Connex 11sX
Bottom Bracket: Campagnolo Ultra-Torque
Gear Range (inches): 19-99" (52/36t) or 23-109" (58/44t)
Brakes: Tektro R539 DP 57 caliper
Gear/Brake Levers: Campagnolo Centaur Black
Handlebar: Deda Speciale classic drop (44 or 42 o-o)
Tapes/Grips: Brooks Cambium Rubber
Handlebar Stem: AL ahead stem (90, 110 or 135mm)
Headset: Moulton custom lightweight 1" sealed
Saddle: Selle San Marco Regal Short Dynamic 140
Seatpost: Moulton / Reynolds Titanium, layback
Tyres: Schwalbe Kojak (Kevlar) 32-369
Rims: Moulton M17 Silver (CNC brake track)
Rear Hub: Moulton custom forged 28h silver
Front Hub: Moulton custom forged 28h silver
Spokes: Sapim Laser/Force butted (differential)
Mudguards: Available as accessory
Mudguard Clearance: Up to 32mm tyre section
Pedals: none supplied
Weight: 10 kg / 22.1 lb'''),

# ------------------------------------------------------------------ Y-FRAME / HAIRPIN
dict(
  slug='xtb', name='XTB', series='Y-frame', lead='2–4',
  icons=['monosphere', 'leadinglink', '20', 'separable'],
  hero='moulton-xtb-camel-yellow-yew-trees.jpg',
  gallery=['moulton-xtb-steely-grey.jpg', 'moulton-xtb-steely-grey-angle-1.jpg'],
  details=[],
  lifestyle=['moulton-xtb-bike-camel-yellow-beneath-yew-trees-2.jpg'],
  tag=('AM-ATB의 현대적 후계자', 'The modern successor to the AM-ATB', 'AM-ATBの現代的な後継', 'AM-ATB 的现代传人'),
  desc=(
    "XTB는 세계 최초의 양산형 풀 서스펜션 마운틴바이크였던 AM-ATB의 현대적 크로스 터레인 후계자입니다. 자갈길, 숲길, 혼합 노면을 위해 만들어졌습니다. 헤어핀 스페이스프레임을 바탕으로 보강 브레이싱과 듀얼 리어 포크 업라이트, 강화된 서스펜션을 더해 AM-ATB보다 더 튼튼하고 가볍고 목적에 충실해졌습니다. 분리 기능과 짐 싣는 능력, 몰튼다운 침착한 승차감은 그대로입니다.",
    "The XTB is the modern cross-terrain successor to the AM-ATB, the world's first production full-suspension mountain bike. Made for gravel, forest tracks and mixed surfaces, it builds on the hairpin spaceframe with reinforced bracing, dual rear fork uprights and uprated suspension: stronger, lighter and more purpose-built than the AM-ATB, while keeping separability, load-carrying ability and the composure of a Moulton.",
    "XTBは、世界初の量産フルサスペンション・マウンテンバイクであったAM-ATBの現代的なクロステレイン後継モデルです。砂利道、林道、混合路面のために作られました。ヘアピン・スペースフレームをベースに、補強ブレーシング、デュアルリアフォークアップライト、強化されたサスペンションを加え、AM-ATBより強く、軽く、目的に忠実になりました。分割機能、積載能力、モールトンらしい落ち着いた乗り味はそのままです。",
    "XTB 是 AM-ATB（全球首款量产全避震山地车）的现代跨地形传人。它专为砂石路、林道与混合路面打造，在发夹式空间桁架的基础上加入强化支撑、双后叉立管与升级避震，比 AM-ATB 更坚固、更轻、更具针对性，同时保留可拆分、载物能力与莫尔顿特有的从容骑感。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Leading Link (unicrown)
Rear Suspension: Monosphere
Separability: Separable
Frame Coupling: Centre bolt + alloy locknut
Frame Material: Columbus Spirit and Reynolds 525 CrMo steels (stainless steel dropouts)
Frame Construction: Fillet brazed, hairpin construction. Tubular zig-zags.
Bottle Mounts: 4 sets: seat tube, lower rail, 2x head tube
Frame Finish: Powder Coat''',
  builds=['Shimano Alfine 11', 'SRAM Rival 11'],
  spec='''
Ride Category: City & Leisure; Gravel & Off-road | City & Leisure (flat bar); Gravel & Off-road; Touring & Adventure
Brake Type: Front V-brake + Rear Mech. Disc
Handlebar Type: Flat | Flat or Drop
Gear System: Hub | Derailleur
Front Mech: n/a
Rear Mech: n/a | SRAM Rival 1
Crankset: Shimano Alfine 45t w/chainguard | SRAM Rival 1, 42t
Cassette: 20t | Custom 9-36t
Chain: Connex 900 9 speed | Connex 11sX
Bottom Bracket: Shimano Hollowtech II | SRAM GXP
Gear Range (inches): 24-97" (45t) | 23-93" (42t)
Brakes: Front Shimano V + Rear TRP Spyre disc
Gear/Brake Levers: Shimano Alfine (flat) or Shimano Hollowtech (drop) | SRAM Apex Trigger (flat) or SRAM Rival 1 (drop)
Handlebar: M Special flat bar | M Special flat bar or Deda Speciale classic drop (44 o-o)
Tapes/Grips: Triple-density with bar end hooks | Triple-density with bar end hooks (flat) or Brooks Cambium rubber tape (drop)
Handlebar Stem: AL ahead stem (90, 110 or 135mm)
Headset: Tange Seiki RDC 1" sealed
Saddle: Selle San Marco Regal Short Dynamic 165
Seatpost: 31.6 CNC Aluminium, in-line (lightweight)
Tyres: Schwalbe Billy Bonkers 50-406
Rims: Double Wall Black (CNC brake track)
Rear Hub: Shimano Alfine 11 speed 32h silver | Moulton custom forged 28h silver
Front Hub: Moulton custom forged 28h silver
Spokes: Sapim Laser/Force butted (differential)
Mudguards: Available as accessory
Mudguard Clearance: Up to 50mm tyre section
Pedals: MKS Promenade q/r | none supplied
Weight: 12 kg / 26.4 lb | 11.3 kg / 24.9 lb'''),

dict(
  slug='sst', name='SST', series='Y-frame', lead='1–2',
  icons=['monosphere', 'leadinglink', '20', 'separable'],
  hero='moulton-sst-airforce-blue-stone-trees.jpg',
  gallery=['moulton-sst-airforce-blue-side.jpg', 'moulton-sst-airforce-blue-angle-1.jpg', 'moulton-sst-sage-grey.jpg', 'moulton-sst-sage-grey-angle-1.jpg'],
  details=[],
  lifestyle=['moulton-sst-bike-airforce-blue-by-wooden-gate-at-the-hall.jpg'],
  tag=('더 정교해진 TSR의 후계자', 'The refined successor to the TSR', 'より洗練されたTSRの後継', '更精致的 TSR 继任者'),
  desc=(
    "SST는 TSR을 더 정교하게 다듬은 후속 모델입니다. 실용성은 그대로 두고 더 가볍고, 더 단단하고, 더 섬세해졌습니다. 헤어핀 스페이스프레임에 스테인리스 드롭아웃과 더 큰 피벗 베어링, 테이퍼드 원형 리어 스테이를 더해 정확하고 내구성 있는 주행감을 냅니다. 분리형의 다재다능함으로 도심과 레저, 장거리 로드, 짐을 실은 투어링까지 아우릅니다.",
    "The SST is a more refined successor to the TSR: lighter, stiffer and more detailed, while staying practical. It keeps the hairpin spaceframe and adds stainless steel dropouts, larger pivot bearings and tapered round rear stays for a more precise, durable ride. Separable and versatile, it covers city and leisure riding, endurance road riding and loaded touring, for riders who want more refinement and responsiveness without the labour-intensive spaceframes.",
    "SSTはTSRをより洗練させた後継モデルです。実用性はそのままに、より軽く、より剛く、より繊細になりました。ヘアピン・スペースフレームにステンレスドロップアウト、大型のピボットベアリング、テーパー付きの丸断面リアステーを加え、正確で耐久性のある乗り味を実現。分割式の汎用性で、街乗りやレジャー、長距離ロード、荷物を積んだツーリングまでこなします。",
    "SST 是 TSR 更精致的继任者：更轻、更刚、更细腻，同时保持实用。它沿用发夹式空间桁架，并加入不锈钢勾爪、更大的枢轴轴承与锥形圆管后下叉，骑行更精准、更耐用。可拆分、多用途，从城市休闲、长途公路到载重旅行皆可胜任。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Leading Link (unicrown)
Rear Suspension: Monosphere
Separability: Separable
Frame Coupling: Centre bolt + alloy locknut
Frame Material: Columbus Spirit and Reynolds 525 CrMo steels (stainless steel dropouts)
Frame Construction: Fillet brazed, hairpin construction. Solid zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Powder Coat''',
  builds=['Campagnolo Centaur 2x11', 'Shimano Alfine 11', 'Shimano 105 2x11', 'SRAM X5 9'],
  spec='''
Ride Category: Road & Race; Touring & Adventure | City & Leisure | City & Leisure (flat bar); Touring & Adventure; Road & Race | City & Leisure
Brake Type: Caliper | Front Caliper or V-brake + Rear Mech. Disc | Caliper or V-brake | Caliper or V-brake
Handlebar Type: Drop | Flat | Flat or Drop | Flat
Gear System: Derailleur | Hub | Derailleur | Derailleur
Front Mech: Campagnolo Centaur Black | n/a | Shimano 105 | n/a
Rear Mech: Campagnolo Centaur Black | n/a | Shimano 105 | SRAM X5
Crankset: Campagnolo Centaur Black 52/36 or 58/44 | Shimano Alfine 45t w/chainguard | Shimano 105 53/39 | Sturmey Archer 54t w/chainguard
Cassette: Moulton 10-32 | 17t | Moulton 10-32 | Sturmey Archer 11-34
Chain: Connex 11sX | Connex 900 9 speed | Connex 11sX | Connex 900 9 speed
Bottom Bracket: Campagnolo Ultra-Torque | Shimano Hollowtech II | Shimano Hollowtech II | Sturmey Archer
Gear Range (inches): 21-96" (52/36t) or 26-107" (58/44t) | 25-105" (45t) (caliper) | 23-98" (53/39t) (caliper) | 29-91" (54t) (caliper)
Brakes: Tektro R539 DP 57 caliper | Front Tektro R539 DP 57 caliper or Shimano v-brake / Rear TRP Spyre disc | Tektro R539 DP 57 caliper or Tektro RX6 v-brake | Tektro R539 DP 57 caliper or Shimano v-brake
Gear/Brake Levers: Campagnolo Centaur Black | Tektro FL750 / Shimano Alfine rapidfire | Shimano 105 | SRAM X-5 black (caliper) or Avid (v-brakes)
Handlebar: Deda Speciale classic drop (44 or 42 o-o) | M Special flat bar | GB Carter drop Bar (42 c-c) or M Special flat bar | M Special flat bar
Tapes/Grips: Brooks Cambium Rubber | Brooks Cambium Ergonomic | Brooks Cambium Rubber | Diamond knurl lock-on grips
Handlebar Stem: AL ahead stem (90, 110 or 135mm) | AL ahead stem (90, 110 or 135mm) | AL adjustable stem 110 / 31.8 | Kalloy AL adjustable stem 110 / 26
Headset: Tange Seiki RDC 1" sealed
Saddle: Fizik Antares | Selle San Marco Regal Short Dynamic 165 | Selle San Marco Regal Short Dynamic 140 | Selle Royal Viper
Seatpost: 31.6 CNC Aluminium, in-line (lightweight) | 31.6 forged Aluminium, layback head | 31.6 forged Aluminium, layback head | 31.6 forged Aluminium, layback head
Tyres: Schwalbe One (folding) 28-406 | Schwalbe One (folding) 28-406 (caliper) or 40-406 Marathon Racer tyres (v-brake) | Schwalbe One (folding) 28-406 | Schwalbe One (folding) 28-406 (caliper) or 40-406 Marathon Racer tyres (v-brake)
Rims: Moulton MT20 Black (CNC brake track) | Moulton MT20 Black (CNC brake track) | Moulton MT20 Black (CNC brake track) | ER-10 Black (CNC brake track)
Rear Hub: Moulton custom forged 28h silver | Shimano Alfine 11 speed 32h silver | Moulton custom forged 28h silver | Alloy forged q/r 28h silver (HG for 10/11s)
Front Hub: Moulton custom forged 28h silver | Moulton custom forged 28h silver 70mm | Moulton custom forged 28h silver | Alloy forged q/r 28h silver
Spokes: Sapim Laser/Force butted (differential) | Sapim Laser butted front/PG rear | Sapim Laser/Force butted (differential) | Sapim Leader stainless 14g
Mudguards: Available as accessory
Mudguard Clearance: Up to 28mm tyre section | Up to 28mm (Caliper) or 40mm (V-brakes) tyre section | Up to 28mm (Caliper) or 40mm (V-brakes) tyre section | Up to 28mm (Caliper) or 40mm (V-brakes) tyre section
Pedals: none supplied | MKS Promenade q/r | none supplied | VP607 alloy with rubber inserts
Weight: 10.5 kg / 23 lb | 11.8 kg / 26 lb | 10.8 kg / 23.7 lb | 11.1 kg / 24.5 lb'''),

dict(
  slug='tsr', name='TSR', series='Y-frame', lead='1–2',
  icons=['monosphere', 'leadinglink', '20', 'separable'],
  hero='moulton-tsr-powder-pink-wooden-wall.jpg',
  gallery=['moulton-tsr-powder-pink.jpg', 'moulton-tsr-powder-pink-angle-1.jpg'],
  details=['moulton-tsr-powder-pink-frame-close-up-foliage.jpg'],
  lifestyle=[],
  tag=('몰튼의 세계로 들어가는 첫 관문', 'The gateway to Moulton engineering', 'モールトンの世界への入口', '通往莫尔顿工程的入门之选'),
  desc=(
    "TSR은 오리지널 APB의 현대적 후계자로, 몰튼 엔지니어링을 가장 실용적이고 부담 없이 시작할 수 있는 모델입니다. 몰튼의 헤어핀 스페이스프레임으로 출퇴근과 레저, 가벼운 투어링을 위해 만들어졌습니다. 일상의 쓰임새와 내구성, 이동을 위한 분리 기능 사이의 균형을 갖췄고, 효율과 편안함, 오래가는 신뢰성에 집중한 가장 솔직한 몰튼입니다.",
    "The TSR is the modern successor to the original APB: a practical, accessible and capable way into Moulton engineering. Built on the hairpin spaceframe for commuting, leisure and light touring, it balances everyday usability, durability and separability for transport. The most straightforward and attainable expression of the Moulton approach, focused on efficiency, comfort and long-term reliability.",
    "TSRはオリジナルAPBの現代的な後継モデルで、モールトンのエンジニアリングを最も実用的に、気軽に始められる一台です。モールトンのヘアピン・スペースフレームで、通勤、レジャー、軽いツーリングのために作られました。日常での使いやすさ、耐久性、移動のための分割機能のバランスを備え、効率、快適性、長期的な信頼性に焦点を当てた、最も率直なモールトンです。",
    "TSR 是原版 APB 的现代传人：一款实用、亲民且能力出众的莫尔顿入门车型。它基于发夹式空间桁架，专为通勤、休闲与轻度旅行打造，在日常实用、耐用性与便于运输的可拆分设计之间取得平衡。这是莫尔顿理念最直接、最易拥有的表达，专注于效率、舒适与长久可靠。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Leading Link (unicrown)
Rear Suspension: Monosphere
Separability: Separable
Frame Coupling: Centre bolt + alloy locknut
Frame Material: Columbus Spirit and Reynolds 525 CrMo steels
Frame Construction: Fillet brazed, hairpin construction. Solid zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Powder Coat''',
  builds=['Shimano Nexus 8', 'SRAM X5 9'],
  spec='''
Ride Category: City & Leisure
Brake Type: V-brake | Caliper or V-brake
Handlebar Type: Flat
Gear System: Hub | Derailleur
Front Mech: n/a
Rear Mech: n/a | SRAM X5
Crankset: Sturmey Archer 54t w/chainguard
Cassette: 18t | SRAM PG950 11-32
Chain: Connex 900 9 speed
Bottom Bracket: Sealed Cartridge
Gear Range (inches): 30-96" (54t) | 32-94" (54t)
Brakes: Shimano v-brake | Tektro R539 DP 57 caliper or Shimano v-brake
Gear/Brake Levers: Avid | SRAM X-5 black (caliper) or Avid (v-brakes)
Handlebar: M Special flat bar
Tapes/Grips: Rubber moulded grips
Handlebar Stem: Kalloy AL adjustable stem 110 / 26
Headset: Tange Seiki RDC 1" sealed
Saddle: Selle Royal Viper
Seatpost: 31.6 forged Aluminium, layback head
Tyres: Schwalbe 40-406 Marathon Racer | Schwalbe One (folding) 28-406 (caliper) or 40-406 Marathon Racer tyres (v-brake)
Rims: Double Wall Black (CNC brake track)
Rear Hub: Shimano Nexus 8 speed 32h silver | Alloy forged q/r 28h silver (HG for 10/11s)
Front Hub: Alloy forged q/r 28h silver
Spokes: Sapim Leader stainless 14g
Mudguards: Available as accessory
Mudguard Clearance: Up to 40mm tyre section (V-brakes) | Up to 28mm (Caliper) or 40mm (V-brakes) tyre section
Pedals: VP607 alloy with rubber inserts
Weight: 12.6 kg / 27.8 lb | 11.5 kg / 25.4 lb'''),

# ------------------------------------------------------------------ SPECIAL EDITION
dict(
  slug='the-hall-se', name='The Hall SE', series='Special Edition', lead='stock',
  icons=['monosphere', 'leadinglink', '20', 'separable'],
  hero='moulton-hall-se-green-wooden-front-door.jpg',
  gallery=['moulton-the-hall-se-hall-green.jpg', 'moulton-the-hall-se-hall-green-angle-1.jpg'],
  details=[],
  lifestyle=['moulton-hall-se-green-wooden-garden-gate.jpg'],
  tag=('홀 에스테이트에 바치는 스페셜 에디션', 'A special edition in tribute to The Hall', 'ザ・ホールに捧げるスペシャルエディション', '致敬 The Hall 的特别版'),
  desc=(
    "더 홀 스페셜 에디션은 몰튼이 태어난 장소와 그 기원, 그리고 이어져 온 엔지니어링에 바치는 모델입니다. 전용 홀 그린 컬러와 각인된 스테인리스 배지를 달았고, 알렉스 몰튼 박사가 자전거를 설계한 브래드퍼드온에이번의 제임스 1세 양식 저택 '더 홀'을 기립니다. 프론트와 리어 서스펜션을 통합한 클래식 헤어핀 스페이스프레임으로, 매일 타기 좋은 실용적인 분리형 미니벨로입니다. 이 자전거의 매력은 구조의 복잡함이 아니라 그 출신에 있습니다.",
    "The Hall Special Edition is a tribute to place, origin and the continuity of Moulton engineering. Finished in an exclusive Hall Green with an engraved stainless steel badge, it honours the Jacobean Hall in Bradford-on-Avon where Dr Alex Moulton developed his bicycles. Built on the classic hairpin spaceframe with integrated front and rear suspension, it remains a practical, separable small-wheeler for everyday riding. Its appeal is provenance rather than structural complexity.",
    "ザ・ホール・スペシャルエディションは、モールトンが生まれた場所とその起源、そして受け継がれてきたエンジニアリングに捧げるモデルです。専用のホールグリーンと刻印入りのステンレスバッジをまとい、アレックス・モールトン博士が自転車を設計したブラッドフォード・オン・エイヴォンのジャコビアン様式の邸宅「ザ・ホール」を讃えます。前後サスペンションを統合したクラシックなヘアピン・スペースフレームで、毎日乗りやすい実用的な分割式ミニベロです。その魅力は構造の複雑さではなく、出自にあります。",
    "The Hall 特别版是对莫尔顿诞生之地、其起源以及工程传承的致敬。它采用专属的 Hall Green 涂装与刻印不锈钢车标，纪念亚历克斯·莫尔顿博士在布拉德福德昂埃文的詹姆斯一世时期宅邸 The Hall 中设计自行车的岁月。它基于前后避震一体化的经典发夹式空间桁架，是一台适合日常骑行的实用可拆分小轮车。它的魅力在于出身，而非结构的复杂。"),
  key='''
Wheel Size: 20" (406mm)
Front Suspension: Leading Link (unicrown)
Rear Suspension: Monosphere
Separability: Separable
Frame Coupling: Centre bolt + alloy locknut
Frame Material: Columbus Spirit and Reynolds 525 CrMo steels
Frame Construction: Fillet brazed, hairpin construction. Solid zig-zags.
Bottle Mounts: 2 sets: seat tube & lower rail
Frame Finish: Powder Coat''',
  builds=['Shimano Nexus 8'],
  spec='''
Ride Category: City & Leisure
Brake Type: V-brake
Handlebar Type: Flat
Gear System: Hub
Front Mech: n/a
Rear Mech: n/a
Crankset: Sturmey Archer 54t w/chainguard
Cassette: 18t
Chain: Connex 900 9 speed
Bottom Bracket: Sealed Cartridge
Gear Range (inches): 30-96" (54t)
Brakes: Shimano v-brake
Gear/Brake Levers: Avid
Handlebar: M Special flat bar
Tapes/Grips: OXO-PRO Lockable Comfort Grip
Handlebar Stem: Kalloy AL adjustable stem 110 / 26
Headset: Tange Seiki RDC 1" sealed
Saddle: Brooks B17 or B17s Leather Honey Brown
Seatpost: 31.6 forged Aluminium, layback head
Tyres: Schwalbe 40-406 Marathon Racer
Rims: Double Wall Black (CNC brake track)
Rear Hub: Shimano Nexus 8 speed 32h silver
Front Hub: Alloy forged q/r 28h silver
Spokes: Sapim Leader stainless 14g
Mudguards: 20" Alloy Gloss Black (medium)
Mudguard Clearance: Up to 40mm tyre section (V-brakes)
Pedals: VP607 alloy with rubber inserts
Weight: 12.8 kg / 28.2 lb'''),
]
