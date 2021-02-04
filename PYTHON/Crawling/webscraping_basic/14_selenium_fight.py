from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome("여기에 경로를 넣어야함") 근데 우린 같은 폴더안에 있으니까 경로를 넣을 필요가 없음
browser = webdriver.Chrome("./chromedriver")
url="https://flight.naver.com/flights/"
browser.get(url)# url 로 이동
browser.find_element_by_link_text("가는날 선택").click()

# 달력에서 날짜 선택
# element 가 아니라 elements 로 해서 여러개 있는것들을 리스트로 받아옴
# browser.find_elements_by_link_text("31")[0].click() # 이번달 달력에서 선택됨
browser.find_elements_by_link_text("1")[1].click() # 다음달 달력에서 선택됨(다음달 1일 클릭됨)
browser.find_elements_by_link_text("5")[1].click() # 다음달 달력에서 ㄴ선택됨(디음달 5일 클릭됨)


# xpath 를 이용하여 목적지 제주도로 하기 
time.sleep(2)
# xpath를 가져올때 클릭이 안되는 경우가 있음 그럴떈 상위 태그로 xpath설정하거나 다른 태그를 이용해보자!
browser.find_element_by_xpath("//*[@id=\"recommendationList\"]/ul/li[1]").click()


# 항공권 검색 클릭하기
browser.find_element_by_link_text("항공권 검색").click()

# 어떤 element가 나올떄 까지 20 초 까진 기다려달라 !
# WebDriverWait를 통해서 browser를 20초동안 기다림
# 20초 안에 뭔가 나오면은 어떤 조건(xpath에 해당하는 element가 위치할때 까지 기다려 달라!) 에 해당하는 떄 까지 기다려 달라
# x 초 안에 안뜨면 에러가 남 따라서 try except 를 활용하자!
try:
    # 성공했을떄 동작 수행
    elem=WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"content\"]/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text) # 첫번쨰 결과 출력
finally:
    browser.quit()

