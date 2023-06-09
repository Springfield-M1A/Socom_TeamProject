// 종목 정보 데이터
const stockData = [
    { code: "AAPL", name: "Apple Inc.", price: 150.50, low: 148.80, high: 152.20 },
    { code: "GOOGL", name: "Alphabet Inc.", price: 2500.00, low: 2475.50, high: 2530.00 },
    // ... 추가 종목 데이터
];

// 상위 차트 데이터
const topChart1 = { title: "Chart 1", data: "..." };
const topChart2 = { title: "Chart 2", data: "..." };
const topChart3 = { title: "Chart 3", data: "..." };
const topChart4 = { title: "Chart 4", data: "..." };
const topChart5 = { title: "Chart 5", data: "..." };
const topCharts = [topChart1, topChart2, topChart3, topChart4, topChart5];

// 초기화 함수
function init() {
    displayTopCharts();
    displayStockTable();
}

// 상위 차트 표시
function displayTopCharts() {
    const chartContainer = document.querySelector(".top-charts");

    // 상위 차트 데이터를 반복하여 표시
    topCharts.forEach((chartData) => {
        const chartDiv = document.createElement("div");
        chartDiv.classList.add("chart");

        const title = document.createElement("h4");
        title.textContent = chartData.title;
        chartDiv.appendChild(title);

        const data = document.createElement("p");
        data.textContent = chartData.data;
        chartDiv.appendChild(data);

        chartContainer.appendChild(chartDiv);
    });
}

// 종목 표 표시
function displayStockTable() {
    const tableBody = document.querySelector(".stock-table tbody");

    // 종목 데이터를 반복하여 표시
    stockData.forEach((stock) => {
        const row = document.createElement("tr");

        const codeCell = document.createElement("td");
        codeCell.textContent = stock.code;
        row.appendChild(codeCell);

        const nameCell = document.createElement("td");
        nameCell.textContent = stock.name;
        row.appendChild(nameCell);

        const priceCell = document.createElement("td");
        priceCell.textContent = stock.price;
        row.appendChild(priceCell);

        const lowCell = document.createElement("td");
        lowCell.textContent = stock.low;
        row.appendChild(lowCell);

        const highCell = document.createElement("td");
        highCell.textContent = stock.high;
        row.appendChild(highCell);

        tableBody.appendChild(row);
    });
}

// 그래프 종류 변경
function changeChartType(type) {
    // TODO: 그래프 종류 변경 로직 구현
}

// 데이터 가져오기
function fetchData() {
    // API 호출 및 데이터 처리 로직 구현
}

// 그래프 그리기
function drawGraph() {
    // 그래프 그리기 로직 구현 (D3.js, Chart.js 등 활용)
}

// 종목 표 업데이트
function updateStockTable() {
    const tableBody = document.querySelector(".stock-table tbody");

    // 검색어 가져오기
    const searchKeyword = document.querySelector("#search-input").value.toLowerCase();

    // 종목 표 초기화
    tableBody.innerHTML = "";

    // 종목 데이터 반복하여 표시
    stockData.forEach((stock) => {
        // 종목명과 검색어 비교
        if (stock.name.toLowerCase().includes(searchKeyword)) {
            const row = document.createElement("tr");

            const codeCell = document.createElement("td");
            codeCell.textContent = stock.code;
            row.appendChild(codeCell);

            const nameCell = document.createElement("td");
            nameCell.textContent = stock.name;
            row.appendChild(nameCell);

            const priceCell = document.createElement("td");
            priceCell.textContent = stock.price;
            row.appendChild(priceCell);

            const lowCell = document.createElement("td");
            lowCell.textContent = stock.low;
            row.appendChild(lowCell);

            const highCell = document.createElement("td");
            highCell.textContent = stock.high;
            row.appendChild(highCell);

            tableBody.appendChild(row);
        }
    });
}

// 이벤트 리스너 등록
document.querySelector("#search-input").addEventListener("input", updateStockTable);

// 초기화 실행
fetchData();
drawGraph();
updateStockTable();

// 초기화 실행
init();
