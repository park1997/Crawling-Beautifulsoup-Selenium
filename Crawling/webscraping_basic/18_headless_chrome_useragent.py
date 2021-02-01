# 동적인 웹사이트를 스크롤링을 조절하여 영화의 목록 가져 오기 !!
from selenium import webdriver
import requests
import lxml
from bs4 import BeautifulSoup
import time

# 이렇게 두줄만 넣어준다면 누넹보이진 않지만 백그라운드에서 실행한다!!
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=3072x1920") # 이러한 사이즈(나의 컴퓨터 디스플레이 사이즈)로 브라우저 크기를 늘린상태로 실행하지만 우리 사용자에게는 안보임

# user agent 값을 이렇게 바꿔줄 필요가 있음
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36")

url="https://www.whatismybrowser.com/detect/what-is-my-user-agent"
# 이곳에 options = options 넣어주면 이제 실행되는 창이 안보임
browser = webdriver.Chrome("./chromedriver",options=options)
browser.maximize_window()

browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()
