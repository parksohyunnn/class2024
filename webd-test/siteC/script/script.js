$(function () {
    // 이미지 슬라이드
    let currentIndex = 0;   //현재 이미지 설정
    $(".sliderWrap").append($(".slider").first().clone(true)); //첫번째 이미지를 복사해서 마지막에 추가

    setInterval(function () {     //3초에 한번씩 실행
        currentIndex++;     //현재 이미지를 1씩 증가
        $(".sliderWrap").animate({ marginTop: -350 * currentIndex + "px" }, 600);

        if (currentIndex == 3) {  //마지막 이미지가 됐을 때
            setTimeout(function () {  //한번만 실행
                $(".sliderWrap").animate({ marginTop: 0 }, 0); //애니메이션을 정지
                currentIndex = 0;   //현재 이미지를 초기화
            }, 700);
        }
    }, 3000);
});

$(".nav > ul > li").mouseover(function () {
    $(this).find(".submenu").stop().slideDown();
});
$(".nav > ul > li").mouseout(function () {
    $(this).find(".submenu").stop().slideUp();
});

// 팝업
$(".popup-btn").click(function () {   //팝업 버튼 클릭
    $(".popup-view").show();    //팝업 나타나기
});
$(".popup-close").click(function () {     //팝업 닫기 버튼 클릭
    $(".popup-view").hide();   //팝업 숨기기
});