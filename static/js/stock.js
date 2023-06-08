$(document).ready(function() {
    let myChart;
    let stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']; // 상위 종목들

    // 첫 번째 종목을 그래프로 보여줍니다.
    getStockData(stocks[0]);

    // 종목 리스트를 만듭니다.
    for (let stock of stocks) {
        $("#stock-list").append(`<button class="stock-button" value="${stock}">${stock}</button>`);
    }

    // 종목 버튼을 클릭했을 때, 해당 종목의 그래프를 보여줍니다.
    $(".stock-button").click(function() {
        let stock = $(this).val();
        getStockData(stock);
    });

    // 검색 버튼을 클릭했을 때, 검색한 종목의 그래프를 보여줍니다.
    $("#search-button").click(function() {
        let stock = $("#search-input").val();
        getStockData(stock);
    });

    // 시간 간격 버튼을 클릭했을 때, 해당 시간 간격으로 그래프를 업데이트합니다.
    $(".interval").click(function() {
        let interval = $(this).val();
        updateChart(interval);
    });

    // 정규화 버튼을 클릭했을 때, 그래프를 정규화합니다.
    $("#normalize").click(function() {
        // 정규화 로직을 추가합니다.
    });

    // 주식 데이터를 가져와 그래프를 그립니다.
    function getStockData(stock) {
        $.ajax({
            url: '/get_stock_data/',
            data: {
                'symbol': stock,
                'interval': 'daily'
            },
            dataType: 'json',
            success: function(data) {
                let dates = Object.keys(data['Time Series (Daily)']).reverse();
                let prices = dates.map(date => data['Time Series (Daily)'][date]['4. close']);
                drawChart(stock, dates, prices);
            }
        });
    }

    // 그래프를 그립니다.
    function drawChart(stock, dates, prices) {
        if (myChart) {
            myChart.destroy(); // 이전 그래프를 제거합니다.
        }
        let ctx = document.getElementById('myChart').getContext('2d');
        myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: stock,
                    data: prices,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            }
        });
    }

    // 그래프를 업데이트합니다.
    function updateChart(interval) {
        // 시간 간격에 따른 그래프 업데이트 로직을 추가합니다.
    }
});
