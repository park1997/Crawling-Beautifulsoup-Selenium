import requests
from bs4 import BeautifulSoup
import re

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}


for i in range(1,6):
    print("현재 페이지 :{}".format(i))
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(str(i))
    res= requests.get(url,headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")

    # search-product 로 시작하는 클래스 가져오는 방법!! re 쓰기 !!
    items= soup.find_all("li",attrs={"class":re.compile("^search-product")})
    for item in items:
        name= item.find("div",attrs={"class":"name"}).get_text()
        
        # 평점이 4.5 이상
        if (item.find("em",attrs={"class":"rating"})):
            if (float(item.find("em",attrs={"class":"rating"}).get_text())>=4.5):
                rate=float(item.find("em",attrs={"class":"rating"}).get_text())
            else:
                continue
        else:
            continue
        
        # 리뷰수가 100 이상
        if item.find("span",attrs={"class":"rating-total-count"}):
            if float(item.find("span",attrs={"class":"rating-total-count"}).get_text()[1:-1])>=100:
                review=item.find("span",attrs={"class":"rating-total-count"}).get_text()[1:-1]
            else:
                continue
        else:
            continue

        price=item.find("strong",attrs={"class":"price-value"}).get_text()
        print("제품명 : {}\n가격 : {}\n리뷰수 : {}\n평점 : {}".format(name,price,review,rate))


