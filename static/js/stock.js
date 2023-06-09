document.addEventListener("DOMContentLoaded", function() {
    // 상위 5개 종목 정보 가져오기
    fetchTopStocks();

    // 그래프 초기화
    initGraph();

    // 종목 목록 테이블 초기화
    initStockTable();

    // 검색 기능
    document.querySelector("#search-input").addEventListener("input", function() {
        searchStocks(this.value);
    });
});

function fetchTopStocks() {
    // API 요청을 통해 상위 5개 종목 정보 가져오기
    // 가져온 데이터를 배너에 출력
}

function initGraph() {
    // 그래프 초기화 및 첫 번째 종목의 그래프 출력
    // 다른 종목 선택 기능 및 그래프 타입 변경 기능 구현
}

function initStockTable() {
    // API 요청을 통해 종목 목록 정보 가져오기
    // 가져온 데이터를 테이블에 출력
}

function searchStocks(keyword) {
    // 종목 목록에서 키워드를 포함하는 종목 필터링
    // 필터된 결과를 테이블에 출력
}
