/* 몰튼 모델 목록. 가격은 여기서만 수정하면 메인과 모델 페이지에 모두 반영됩니다. */
/* ============================================================
   MODELS
   price: 원화 숫자 (예: 38500000). 비워 두면 "가격 문의"로 표시됩니다.
   from: true 이면 "~부터" 표기. tag: 카드 좌상단 뱃지.
   series: ns | moulton | am | y | se  (필터용)
   slug: 모델 페이지 주소 (moultonbicycles.co.kr/<slug>/)
   이 파일 하나를 메인 그리드와 각 모델 페이지가 함께 사용합니다.
   ============================================================ */
var MODELS = [
  {slug:'ns-double-pylon', name:'NS D-Pylon',  series:'ns',      label:'New Series',       img:'moulton-ns-double-pylon-stainless.jpg', alt:'moulton-ns-double-pylon-stainless-angle-1.jpg', price:'', from:false, tag:''},
  {slug:'ns-speed', name:'NS Speed',    series:'ns',      label:'New Series',       img:'moulton-ns-speed-stainless.jpg',        alt:'moulton-ns-speed-stainless-angle-1.jpg',        price:'', from:false, tag:''},
  {slug:'ns-rapide', name:'NS Rapide',   series:'ns',      label:'New Series',       img:'moulton-ns-rapide-sunrise-orange.jpg',  alt:'moulton-ns-rapide-sunrise-orange-angle-1.jpg',  price:'', from:false, tag:{ko:'신모델',en:'New Model',ja:'新モデル',zh:'新车型'}},
  {slug:'speed', name:'Speed',       series:'moulton', label:'Moulton',          img:'moulton-speed-stainless.jpg',           alt:'moulton-speed-stainless-angle-1.jpg',           price:'', from:false, tag:''},
  {slug:'ns-safari', name:'NS Safari',   series:'ns',      label:'New Series',       img:'moulton-ns-safari-willow-green.jpg',    alt:'moulton-ns-safari-willow-green-angle-1.jpg',    price:'', from:false, tag:''},
  {slug:'ns-marathon', name:'NS Marathon', series:'ns',      label:'New Series',       img:'moulton-ns-marathon-stainless-blue-hl.jpg', alt:'moulton-ns-marathon-stainless-blue-hl-angle-1.jpg', price:'', from:true, tag:''},
  {slug:'am-gt', name:'AM GT',       series:'am',      label:'AM Series',        img:'moulton-gt-mk3-stainless.jpg',          alt:'moulton-gt-mk3-stainless-angle-1.jpg',          price:'', from:true, tag:''},
  {slug:'jubilee', name:'Jubilee',     series:'am',      label:'AM Series',        img:'moulton-jubilee-ferrari-red.jpg',       alt:'moulton-jubilee-ferrari-red-angle-1.jpg',       price:'', from:false, tag:''},
  {slug:'am-speed', name:'AM Speed',    series:'am',      label:'AM Series',        img:'moulton-am-speed-white.jpg',            alt:'moulton-am-speed-white-angle-1.jpg',            price:'', from:false, tag:''},
  {slug:'am-22', name:'AM 22',       series:'am',      label:'AM Series',        img:'moulton-am-22-steely-grey.jpg',         alt:'moulton-am-22-steely-grey-angle-1.jpg',         price:'', from:false, tag:''},
  {slug:'xtb', name:'XTB',         series:'y',       label:'Y-frame',          img:'moulton-xtb-steely-grey.jpg',           alt:'moulton-xtb-steely-grey-angle-1.jpg',           price:'', from:false, tag:''},
  {slug:'sst', name:'SST',         series:'y',       label:'Y-frame',          img:'moulton-sst-airforce-blue-side.jpg',    alt:'moulton-sst-airforce-blue-angle-1.jpg',         price:'', from:true, tag:''},
  {slug:'the-hall-se', name:'The Hall SE', series:'se',      label:'Special Edition',  img:'moulton-the-hall-se-hall-green.jpg',    alt:'moulton-the-hall-se-hall-green-angle-1.jpg',    price:'', from:false, tag:{ko:'스페셜 에디션',en:'Special Edition',ja:'スペシャルエディション',zh:'特别版'}},
  {slug:'tsr', name:'TSR',         series:'y',       label:'Y-frame',          img:'moulton-tsr-powder-pink.jpg',           alt:'moulton-tsr-powder-pink-angle-1.jpg',           price:'', from:false, tag:''},
];
