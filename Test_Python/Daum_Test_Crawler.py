import io
import sys
import json
import urllib.request as req
# pip install fake-useragent 설치 후 실행 가능
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Fake Header 정보
fuser = UserAgent()

# 헤더 선언
headers = {
    'User-Agent': fuser.ie,
    'referer': 'https://finance.daum.net/'
}

# 다음 주식 요청 URL
Toplist_URL = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
respone = req.urlopen(req.Request(Toplist_URL, headers=headers)).read().decode('utf-8')

# 응답 데이터 확인(JSON Data)
# print('response URL: ',respone)

# 응답 데이터 str -> json 변환 및 data 값 저장
rank_json = json.loads(respone)['data']

# 중간 요청 데이터 확인
# print('중간 확인 : ', rank_json, '\n')

for tier_market in rank_json:
    # print(type(elm)) #Type 확인
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(tier_market['rank'], tier_market['tradePrice'], tier_market['name']), )