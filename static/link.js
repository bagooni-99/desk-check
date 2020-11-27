var abc = document.getElementById("link");

function link_change() {
    var date_1 = new Date();
    // date Object를 받아오고 
    var month_1 = date_1.getMonth() + 1;
    // 달을 받아옵니다 
    var clockDate_1 = date_1.getDate();
    // 몇일인지 받아옵니다 
    abc.innerHTML = month_1 + "월 " + clockDate_1 + "일 예약 현황";
}
link_change();
