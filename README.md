# Moulton Bicycles Korea · moultonbicycles.co.kr

몰튼 UK(moultonbicycles.co.uk) 홈페이지 구조를 따른 정적 사이트.

- `index.html` 메인 원페이지
- `suspension/index.html` 서스펜션 페이지 (/suspension). `build_suspension.py`가 메인의 헤더·푸터·스타일을 가져와 생성하므로, 본문은 스크립트의 CONTENT 영역을 고친 뒤 `python3 build_suspension.py`로 재생성.

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
