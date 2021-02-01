# 동적인 웹사이트를 스크롤링을 조절하여 영화의 목록 가져 오기 !!
from selenium import webdriver
import requests
import lxml
from bs4 import BeautifulSoup
import time

url="https://play.google.com/store/movies/top"
browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

# 페이지 이동
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터의 높이인 1920 으로 스크롤 내리기 
# browser.execute_script("window.scrollTo(0,1920)") # 3072 x 1920

# 화면 가장 아래로 스크롤 내리기 
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") # 문서의 높이만큼 스크롤을 내림

interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩 대기 
    time.sleep(interval)

    #현재 높이를 가져와서 저장
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height==prev_height:
        break

    # 높이를 업데이트 함
    prev_height = current_height
print("스크롤 완료")

# 구글무비에 할인하는 영화 정보 가져오기 
# 스크롤을 내릴때마다 더 정보가 보이는 동적인 웹싸이트 경우

#헤더 설정하고 서버에 한국문자로된거 가져와 달라 함
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Accept-Language":"ko-KR,ko"}

soup = BeautifulSoup(browser.page_source,"lxml")

# 모든영화에 대한 정보 가져옴
# 클래스명이 리스트안에 있는 것들이랑 같은 경우들 
# movies = soup.find_all("div",attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]})
movies = soup.find_all("div",attrs={"class":"Vpfmgd"})
print(len(movies))


for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    # 할인된 컨텐츠만 찾기!!
    if movie.find("span",attrs={"class":"SUZt4c djCuy"}):
        # 할인 전 가격
        prev_price=movie.find("span",attrs={"class":"SUZt4c djCuy"}).get_text()
        print("할인된 영화 : {}\t할인전 가격 : {}\t할인후 가격 : {}".format(title,prev_price,price))
    else:  
        print("할인되지 않은 영화 : {}\t가격 : {}".format(title,price))

browser.quit()