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

interval = 1

# 백그라운드에서 실행 (메모리 효율을 늘릴 수 있음)
# options = webdriver.ChromeOptions()
# options.headless = True

# 나의 컴퓨터 전체화면 크기로 실행
# options.add_argument("window-size=3072x1920") 

# 모든 내용이 담긴 Json형태의 데이터
info={}

# 네이버 부동산 URL
url="https://new.land.naver.com/complexes/"

# 실제 접속하는 것 처럼 보이는 headers
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Accept-Language":"ko-KR,ko"}

# 크롬 웹드라이버 백그라운드X
browser = webdriver.Chrome("./chromedriver")
# 크롬 웹드라이버 백그라운드에서 실행 O
# browser = webdriver.Chrome("./chromedriver",options=options)




# 검색할 아파트의 고유 번호 입력
# num = input("아파트의 고유 번호 입력 >")

# URL + 고유번호
# url = url + num
url += "1525"
# 페이지 이동
browser.get(url)
# 창 최대화
browser.maximize_window()
# 동일 매물 묶기
browser.find_element_by_class_name("address_filter").click()



# 반복 수행
try:
    prev = len(browser.find_elements_by_class_name("item.false"))
    print(prev)
    # 반복 수행
    while True:
        # 현재 보이는 매물의 elements
        elem=browser.find_elements_by_class_name("item.false")
        # 맨밑 요소 클릭하면 매물이 업데이트됨
        elem[prev-1].click()
        if len(browser.window_handles)!=1:
            browser.close()
        # 로딩으로인한 오류 제거를위해 1초간 쉬어줌
        time.sleep(interval)
        # 현재 매물 개수 업데이트
        curr = len(elem)
        # 이전 매물개수와 현재매물 개수가 같다는건 더이상 업데이트 할매물이 없다는 뜻
        if prev==curr:
            break
        
        # 매물 개수 업데이트 
        prev = curr
except :
    pass

scrollWrap = browser.execute_script("document.querySelector('.item_list_list--article')")





time.sleep(2)
browser.quit()