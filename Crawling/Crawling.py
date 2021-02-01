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

info={}

# 네이버 부동산 URL
url="https://new.land.naver.com/complexes/"

# 실제 접속하는 것 처럼 보이는 headers
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Accept-Language":"ko-KR,ko"}

# 크롬 웹드라이버
browser = webdriver.Chrome("./chromedriver")

#창 최대화
# browser.maximize_window()

# 검색할 아파트의 고유 번호 입력
# num = input("아파트의 고유 번호 입력 >")

# URL + 고유번호
# url = url + num
url += "1525"
# 페이지 이동
browser.get(url)

# 문서의 높이만큼 스크롤을 내림
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 1초에 1번 스크롤 내림
interval = 1

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩이있을수 있기때문에 1초간 쉬어줌
    time.sleep(interval)

    # 현재 높이를 가져와서 저장
    current_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height==current_height:
        break

    # 높이를 업데이트 함
    prev_height = current_height
print("스크롤 완료!")

# 현재 페이지 소스를 lxml 로 parsing 함
soup = BeautifulSoup(browser.page_source,"lxml")

# 단지 명 
complex_title = soup.find("h3",attrs={"class":"title","id":"complexTitle"}).get_text()
info["단지 명"]=complex_title

# 단지 종류(오피스텔,아파트 ...)
complex_type = soup.find("span",attrs={"class":"label--category"}).get_text()
info["단지 종류"]=complex_type

# 단지정보 클릭
browser.find_element_by_xpath("//*[@id=\"summaryInfo\"]/div[2]/div[2]/button[1]").click()

# 로딩으로 인해 크롤링이 안될 수 있으므로 1초 쉬어줌
time.sleep(interval)

# soup 객체 다시 받아옴
soup = BeautifulSoup(browser.page_source,"lxml")

# 단지 정보 테이블 소스코드
complex_infos = soup.find("table",attrs={"class":"info_table_wrap"}).find_all("tr",attrs={"class":"info_table_item"})

# 딕셔너리를 만들기위해 key, value 값을 리스트에 저장
detail_infos_key=[]
detail_infos_value=[]

# for문을 이용하여 단지정보 추출
for complex_info in complex_infos:
    for details in complex_info.find_all("th",attrs={"class":"table_th"}):
        detail_infos_key.append(details.get_text())
    for details in complex_info.find_all("td",attrs={"class":"table_td"}):
        detail_infos_value.append(details.get_text())

# 단지정보 key,value 값을 대응시켜 딕셔너리에 데이터 저장
for i in range(len(detail_infos_key)):
    info[detail_infos_key[i]]=detail_infos_value[i]

# 단지 내 면적별 정보 테이블
size_infos=soup.find("div",attrs={"class":"detail_box--floor_plan"})

# "단지 내 면적별 정보"
width_info_name=size_infos.find("h5",attrs={"class":"heading_text"}).get_text()

# soup 객체 정보 업데이트
soup = BeautifulSoup(browser.page_source,"lxml")

# 면적 종류 정보 
width_info_num=len(soup.find("span",attrs={"class":"detail_sorting_width"}).find_all("a",attrs={"class":"detail_sorting_tab"}))

size_info_key=[]
size_info_value=[]

# 단지 면적별로 클릭하여 각 면적에 해당하는 정보 가져오기 !
for num in range(width_info_num):
    temp=[]
    #각 면적 클릭을위한 xpath
    xpath="//*[@id=\"tab{}\"]".format(num)
    
    # 첫번째 해당하는 평수 클릭
    browser.find_element_by_xpath(xpath).click()
    
    # 로딩시간 고려하여 2초 동안 쉼
    time.sleep(interval)
    
    # soup 객체 정보 업데이트 
    soup = BeautifulSoup(browser.page_source,"lxml")

    # 현재 Loop에 해당하는 평수 
    size=soup.find("div",attrs={"class":"detail_sorting_inner"}).find("span",attrs={"class":"text"}).get_text()
    
    size_infos_table = soup.find("div",attrs={"class":"detail_box--floor_plan"}).find("table",attrs={"class":"info_table_wrap"}).find_all("tr",attrs={"class":"info_table_item"})
    temp=[]
    for size_info in size_infos_table:
        if len(size_info)==2:
            print(len(size_info))
            temp=[]
        for i in size_info:
            print(i.get_text())
            temp.append(i.get_text())
        
    print("*"*100)
        # for details in size_info.find_all("th",attrs={"class":"table_th"}):
        #     size_info_key.append(details.get_text())
        # for details in size_info.find_all("td",attrs={"class":"table_td"}):
        #     size_info_value.append(details.get_text())
    # print(len(size_info_key),len(size_info_value))
    # print(size_info_key)
    # print(size_info_value)

    # print()
    # print("*"*50)

# 단지 내 면적별 정보 딕셔너리로 만드는 것부터 다시 !!




time.sleep(2)
browser.quit()