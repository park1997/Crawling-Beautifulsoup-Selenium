from bs4 import BeautifulSoup
import lxml
import requests

url = "https://comic.naver.com/webtoon/weekday.nhn"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")
# 네이버 웹툰 전체목록 가져오기
cartoons=soup.find_all("a",attrs={"class":"title"}) # class=title 인 a element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())





