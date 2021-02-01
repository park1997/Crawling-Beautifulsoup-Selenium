from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#네이버 로그인 연습하기!

# chrome("여기에 경로를 넣어야함") 근데 우린 같은 폴더안에 있으니까 경로를 넣을 필요가 없음
browser = webdriver.Chrome("./chromedriver")

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. 아이디와 패스워드를 입력한다
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(2)
# 5. id 를 새로 입력
browser.find_element_by_id("id").send_keys("my_id") # "naver_idmy_id" 로 써짐
time.sleep(1)
browser.find_element_by_id("id").clear() # 원래 있던거 지움
time.sleep(1)
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source) # 지금 페이지에 있는 htmlt소스 코드를 출력 해줌

# 7. 브라우저 정료
browser.quit() # 전체 브라우저 정료
# browser.close() # 현재 탭만 종료


