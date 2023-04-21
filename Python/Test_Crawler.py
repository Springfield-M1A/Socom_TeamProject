market='KOSPI'
pageSize = 50
page = 1

url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize={pageSize}&page={page}"
print(url)