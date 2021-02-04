# 동적페이지 다루는법
import requests
import lxml
from bs4 import BeautifulSoup




# 구글무비에 할인하는 영화 정보 가져오기 
# 스크롤을 내릴때마다 더 정보가 보이는 동적인 웹싸이트 경우

#헤더 설정하고 서버에 한국문자로된거 가져와 달라 함
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Accept-Language":"ko-KR,ko"}

url="https://play.google.com/store/movies"
res=requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 모든영화에 대한 정보 가져옴
movies = soup.find_all("div",attrs={"class":"WHE7ib mpg5gc"})
# print(len(movies))

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
