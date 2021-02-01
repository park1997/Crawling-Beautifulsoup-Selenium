from bs4 import BeautifulSoup
import lxml
import re
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 네이버 부동산 URL
url="https://land.naver.com/"

# 실제 접속하는 것 처럼 보이는 headers
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Accept-Language":"ko-KR,ko"}

# 크롬 웹드라이버
browser = webdriver.Chrome("./chromedriver")

#창 최대화
# browser.maximize_window()

# 페이지 이동
browser.get(url)

# 검색할 내용 입력
# thing=input("검색할 내용 입력>")
thing = "분당구 풍림아파트"

# 검색할 내용이 화면 입력창에 입력 됨
browser.find_element_by_id("queryInputHeader").send_keys(thing)

# 입력이된 검색물을 검색 시작
# browser.find_element_by_class_name("search_button type_inside NPI=a:search").click()
browser.find_element_by_id("queryInputHeader").send_keys(Keys.ENTER)

elements = browser.find_elements_by_class_name("item")

# 첫번째 요소 삭제 (쓸모없는 데이터)
del elements[0]

for element in elements:
    element.click()
    time.sleep(4)



