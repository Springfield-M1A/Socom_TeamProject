let symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB'];
let chart;
let isNormalized = false;
let chartType = 'line'; // 기본 차트 타입

window.onload = function() {
    symbols.forEach(symbol => {
        getStockData(symbol, updateBanner);
    });

    let ctx = document.getElementById('stock-chart').getContext('2d');
    chart = new Chart(ctx, {
        type: chartType,
        data: {},
        options: {} // 필요한 옵션을 설정합니다.
    });

    document.getElementById('toggle-normalization').addEventListener('click', toggleNormalization);
    document.getElementById('toggle-chart-type').addEventListener('click', toggleChartType);

    Array.from(document.getElementsByName('symbol')).forEach(checkbox => {
        checkbox.addEventListener('change', updateChart);
    });

    document.getElementById('search-input').addEventListener('keyup', function() {
        let input = this.value.toUpperCase();
        let rows = document.getElementById('stock-table').getElementsByTagName('tr');
        for (let i = 0; i < rows.length; i++) {
            let cells = rows[i].getElementsByTagName('td');
            let match = Array.from(cells).some(cell => cell.innerText.toUpperCase().includes(input));
            rows[i].style.display = match ? '' : 'none';
        }
    });
};

function toggleNormalization() {
    isNormalized = !isNormalized;
    updateChart();
}

function toggleChartType() {
    chartType = chartType === 'line' ? 'candlestick' : 'line';
    updateChart();
}

window.onload = function() {
    symbols.forEach(symbol => {
        getStockData(symbol, updateBanner); // 각 종목에 대해 정보를 가져옵니다.
    });
    // 다른 초기화 작업들...
}

function getStockData(symbol, callback) {
    fetch(`/get_stock_data?symbol=${symbol}`)
        .then(response => response.json())
        .then(data => {
            callback(symbol, data); // 가져온 데이터를 이용해 해당 종목의 배너를 업데이트합니다.
        })
        .catch(error => console.error('Error:', error));
}

function updateBanner(symbol, data) {
    // 가져온 데이터를 이용해 배너를 업데이트합니다.
    // 이 부분은 실제 데이터의 형태에 따라 작성해야 합니다.
}


window.onload = function() {
    // 차트를 초기화합니다.
    let ctx = document.getElementById('stock-chart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'line', // 기본 차트 타입
        data: {},
        options: {} // 필요한 옵션을 설정합니다.
    });

    symbols.forEach(symbol => {
        getStockData(symbol, updateChart); // 각 종목에 대해 정보를 가져와 차트를 업데이트합니다.
    });
}

function updateChart(symbol, data) {
    // 가져온 데이터를 이용해 차트를 업데이트합니다.
    // 이 부분은 실제 데이터의 형태에 따라 작성해야 합니다.
}
// static/js/stock.js
window.onload = function() {
    // 초기화 작업들...

    document.getElementById('change-chart-type').addEventListener('click', function() {
        // 차트 타입을 바꿉니다. 'line'과 'candlestick' 사이에서 바꿉니다.
        chart.config.type = chart.config.type === 'line' ? 'candlestick' : 'line';
        chart.update(); // 차트를 업데이트합니다.
    });
}
// static/js/stock.js
window.onload = function() {
    // 초기화 작업들...

    document.getElementById('search-input').addEventListener('keyup', function() {
        let input = this.value.toUpperCase(); // 검색어
        let rows = document.getElementById('table').getElementsByTagName('tr');
        for (let i = 0; i < rows.length; i++) {
            let cells = rows[i].getElementsByTagName('td');
            let match = Array.from(cells).some(cell => cell.innerText.toUpperCase().includes(input));
            rows[i].style.display = match ? '' : 'none'; // 일치하는 행만 보여줍니다.
        }
    });
}
// stock.js
let chart = new Chart(ctx, {
    type: 'candlestick', // 새로운 차트 타입을 사용합니다.
    data: {
        datasets: [{
            data: [], // 데이터는 [시작 가격, 종가, 최고가, 최저가]의 배열들을 포함하는 배열이어야 합니다.
            // ...
        }],
    },
    // ...
});
