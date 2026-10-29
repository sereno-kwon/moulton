# Moulton Bicycles Korea · moultonbicycles.co.kr

몰튼 UK(moultonbicycles.co.uk) 홈페이지 구조를 따른 정적 사이트.

- `index.html` 메인 원페이지
- `suspension/index.html` 서스펜션 (/suspension)
- `design/index.html` 디자인의 진화 (/design)
- `colors/index.html` 컬러 & 피니시 (/colors). UK 'Colours' 페이지 번역. 파우더 코트 15색·스토브 에나멜 15색은 `pages/colors.py`의 `POWDER`/`ENAMEL` 목록, 스와치 이미지는 UK CDN `moulton-bike-colour-<slug>.jpg`
- `sizing/index.html` 사이징 가이드 (/sizing). UK 'Sizing' 페이지 번역. 모델별 인사이드 레그는 `pages/sizing.py`의 `SIZES`(인치, cm 자동 환산)
- `faq/index.html` 자주 묻는 질문 (/faq). UK FAQ 중 영국 전용 항목(영국 배송·VAT·반품·Cycle to Work·쿠키) 제외, 구매·납기·보증은 루비컴퍼니 기준으로 재작성. 질문은 `pages/faq.py`의 `FAQ` 목록(카테고리 3개)
- `about-moulton/index.html` 몰튼 자전거 (/about-moulton). UK 'The Moulton Bike' 번역. 핵심 특징 5개는 `pages/about_moulton.py`의 `FEATURES`
- `alex-moulton/index.html` 알렉스 몰튼 박사 (/alex-moulton). UK 'Dr Alex Moulton' 번역. 갤러리 14장 `GALLERY`, 연표 `TIMELINE` (자선 신탁 설립은 UK 페이지의 1997 대신 moultontrust.org 기준 1977)
- `the-hall/index.html` 홀 에스테이트 (/the-hall). UK 'The Hall Estate' 번역. 투어·숙박 링크는 moultontrust.org
- `racing/index.html` 레이싱 & 기록 (/racing). UK 'Records & Racing' 번역. F-프레임 5건·스페이스프레임 6건은 `pages/racing.py`의 `F_FRAME`/`SPACEFRAME`
- `authorized-dealer/index.html` 공식 딜러 (/authorized-dealer). 딜러 정보는 `pages/authorized_dealer.py`의 `DEALERS` 목록(상호·지역·주소·전화·스토어 링크·서비스 태그). 쇼룸(루비워크샵) → 프라임 딜러 → 인증 딜러 → 안내 → 딜러 문의(루비서플라이) 순. 재생성: `python3 build.py authorized_dealer`

서브페이지는 `build.py`가 메인의 헤더·푸터·스타일·언어 전환을 그대로 가져와 생성. 본문은 `pages/<slug>.py`에 있고, 고친 뒤 `python3 build.py`로 재생성. 새 페이지는 `pages/`에 같은 형식으로 추가.

## 구조
1. 상단 티커 (Made in England · Since 1962)
2. 헤더 · KO/EN/JA/ZH 전환
3. 히어로
4. More than an artform (브랜드 소개)
5. NS Rapide 신모델 배너
6. 특징 4개 섹션 (Engineered Elegance / Made in England / Design Heritage / Racing Pedigree)
7. Epic Adventures 배너
8. One Bike, Many Possibilities (비포·애프터 슬라이더)
9. 전 모델 그리드 (14종, 시리즈 필터)
10. 구매 안내 (쇼룸 · 공식 딜러 · 전화 · 온라인 상담)
11. Stories (룩북 · 몰튼 뉴스)
12. In the press
13. 푸터

## 수정할 곳 (index.html 하단 `<script>`)
- `IMG_BASE`: 현재 UK Shopify CDN 링크. `assets/`에 같은 파일명으로 저장한 뒤 `'assets/'`로 변경.
- `MODELS`: `price`에 원화 숫자 입력 (예: `price:38500000`). 비우면 "가격 문의" 표시. `from:true`면 "부터".
- `PRESS`: 언론 인용 문구.

## 텍스트 수정
모든 문구는 `data-ko` / `data-en` / `data-ja` / `data-zh` 속성에 있음. 네 속성만 고치면 됨. 중국어는 간체(简体) 기준.

## 서체
영문 Pretendard, 한글 S-Core Dream, 일본어 Noto Sans JP, 중국어 Noto Sans SC (CDN). 모두 `<head>`에서 로드.

## 모델 페이지 (/<slug>/)
- 14종: ns-double-pylon, ns-speed, ns-rapide, speed, ns-safari, ns-marathon, am-gt, jubilee, am-speed, am-22, xtb, sst, the-hall-se, tsr
- 내용·사양: `pages/_model_data.py` (UK 제품 페이지 기준), 템플릿: `pages/models.py`
- **가격은 `models.js` 한 곳에서만 수정** → 메인 그리드와 모델 페이지에 바로 반영 (재빌드 불필요)
- 내용 수정 후에는 `python3 build.py models`

## SEO
- `sitemap.xml`: `python3 build.py` 실행 시 자동 생성 (루트 + 모든 하위 페이지)
- `robots.txt`: 전체 허용, 빌드용 파일(`/pages/`, `build.py`, `README.md`) 제외, sitemap 위치 안내
