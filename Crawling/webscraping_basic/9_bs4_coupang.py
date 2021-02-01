import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
# 서버가 나를 막음 그래서 headers를 이용하여 진짜 사용자가 이용하는 것처럼 만듬
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res= requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")
# search-product 로 시작하는 클래스 가져오는 방법!! re 쓰기 !!
items= soup.find_all("li",attrs={"class":re.compile("^search-product")})

# print(items[0].find("div",attrs={"class":"name"}).get_text())
for item in items:
    # 광고 상품 제외하고 구하기 
    if item.find("span",attrs={"class":"ad-badge-text"}):
        print("광고 상품 제외합니다.")
        continue
    name=item.find("div",attrs={"class":"name"}).get_text() # 제품명
    price= item.find("strong",attrs={"class":"price-value"}).get_text() # 가격
    # 평점 수
    # 리뷰 100개 이상 평점 4.5 이상 되는 것만 조회 하기!
    rate=item.find("em",attrs={"class":"rating"}) # 평점
    if rate:
        if float(rate.get_text())>=4.5:
            rate=rate.get_text()
        else:
            print("평점이 4.5 이상이 아님")
            continue
    else:
        rate="평점 없음"
    # 리뷰 수 
    rate_count = item.find("span",attrs={"class":"rating-total-count"})
    if rate_count:
        if float(rate_count.get_text()[1:-1])>=100:
            rate_count=rate_count.get_text()[1:-1]
        else:
            print("리뷰가 100개 이상이 아님")
            continue
    else:
        rate_count="평점 수 없음"



    print(name,price,rate,rate_count)




