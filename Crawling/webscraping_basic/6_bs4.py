import requests
from bs4 import BeautifulSoup
import lxml

url="https://comic.naver.com/index.nhn"

res= requests.get(url)
#혹시나 문제 있으면 프로그램을 종료하도록 함
res.raise_for_status()
# html 문서값을 첫번쨰 인자로 넣음
# lxml parser를 통해서 객체를 만든것임
#soup 이 모든 정보를 가지고 있음
soup=BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)  #처음 발견되는 a element를 출력하라는 뜻
# print(soup.a.attrs) #속성 값들을 출력함
# print(soup.a["href"]) # a element를 href 속성값 정보를 출력가능

# print(soup.find("a",attrs={"class":"Nbtn_upload"})) # a element 에서 class="Nbtn_upload" 인것중 첫 번째 항목 출력
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element를 찾는 것

rank1=soup.find("li",attrs={"class":"rank01"})
print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)

rank2= rank1.next_sibling.next_sibling # 형제 등급으로 이동하는 방법 next_sibling
rank3=rank2.next_sibling.next_sibling
# print(rank2.a.get_text())
# print(rank3.a.get_text())
rank2=rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# 조건을 기준으로 next_sibling 하는 방법!
rank2=rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank3=rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2=rank3.find_previous_sibling("li")
print(rank2.a.get_text())

#부모로 이동하기(parent)
# print(rank1.parent)

#next_sibling 한번에 하는법
all_rank=rank1.find_next_siblings("li") #list 형태로 나옴
#print(all_rank)
for i in all_rank:
    print(i.a.get_text())

#find로  태그를 찾아오는 방법도 있음!!
webtoon= soup.find("a",text="데드퀸-21화") # 텍스트가 ("우리가 찾는 텍스트") 인걸 찾아 올 수 있음
print(webtoon)


