# 다음 부동산에 송파 헬리오시티 를 검색하여 매물 정보 스크래핑 하기

# [출력 결과]
# ======매물 1=======
# 거래 : 매매
# 면적 : 84/59
# 가격 : 165,000(만원)
# 동 : 214동
# 층 : 고/23
# ======매물 2=======
# ...

import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml

url="https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res= requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# with open("puiz.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

data_rows = soup.find("table",attrs={"class":"tbl"}).find("tbody").find_all("tr")

for index,row in enumerate(data_rows):
    colums = row.find_all("td")
    print("=============매물 {}=============".format(index+1))
    print("거래 : ",colums[0].get_text().strip())
    print("면적 : ",colums[1].get_text().strip(),"(공급/전용)")
    print("가격 : ",colums[2].get_text().strip(),"(만원)")
    print("동 : ",colums[3].get_text().strip())
    print("층 : ",colums[4].get_text().strip())




