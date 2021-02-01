from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chrome("여기에 경로를 넣어야함") 근데 우린 같은 폴더안에 있으니까 경로를 넣을 필요가 없음
browser = webdriver.Chrome("./chromedriver")
browser.get("http://naver.com")
elem= browser.find_element_by_class_name("link_login")
# elem.click() # 로그인 버튼 클릭 하기 
# browser.back() # 이전 페이지로 이동하기 
# browser.forward() # 앞 페이지로 이동 하기
elem = browser.find_element_by_id("query")
elem.send_keys("네이버부동산")
elem.send_keys(Keys.ENTER)
elem = browser.find_elements_by_tag_name("a")
print(type(elem))
# for e in elem:
#     print(e.get_attribute("href"))

# x path 를 활용한 브라우저 클릭
elem = browser.find_element_by_xpath("//*[@id=\"main_pack\"]/section[1]/div/div/div[1]/div/div[2]/a")
elem.click()
time.sleep(2)
browser.close() #현재 열려있는 탭만 닫음
time.sleep(2)
browser.quit() # 현재 열려있는 브라우저전체를 닫음


# Selenuim 

# 로그인, 어떤 결과에 대한 필터링 등 어떤 동작을 해야하는 경우
# (크롬 버전에 맞는 chromedriver 가 반드시 있어야함)

# 셀레늄 할떄는 떄로는 기다려랴할 필요가 있음
# 항공권 검색과같이 로딩이있을경우
# 그럴때 필요한 문법 : WebDriver.Wait(browser,10).until(EC.presence_of_element_located((By.XPATH,"엑스패스")))

# 스크롤 내리는것도 가능 





