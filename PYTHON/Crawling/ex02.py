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

url="http://json.parser.online.fr/"

# 실제 접속하는 것 처럼 보이는 headers
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Accept-Language":"ko-KR,ko"}

# 크롬 웹드라이버 백그라운드X
browser = webdriver.Chrome("./chromedriver")

elem = browser.find_element_by_xpath("//*[@id=\"eT\"]")
elem.send_keys("")