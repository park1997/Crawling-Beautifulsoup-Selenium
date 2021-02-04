from bs4 import BeautifulSoup
import lxml
import requests

url = "https://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")
cartoons=soup.find_all("td",attrs={"class":"title"})
# # 제목 정보 출력
# for i in cartoons:
#     # print(i.a.get_text())
# print()

# # 링크 정보 출력
# for j in cartoons:
#     # print("https://comic.naver.com"+j.a["href"]) # 태그내의 속성을 가져오려면 대괄호를 쓰면됨!!
# print()

# #각각의 대응하는 json형태로 바꾸기
# dic={}
# for i in cartoons:
#     dic[i.a.get_text()]="https://comic.naver.com"+j.a["href"]
# # print(dic)

# 평점 정보 뺴오기 
total_rate=0
cartoons = soup.find_all("div",attrs={"class":"rating_type"})
# print(cartoons)
for i in cartoons:
    print(i.strong.get_text(),i.find("strong").get_text())
    total_rate+=float(i.strong.get_text())
print("총 점수 : ",total_rate)
print("평균 점수 : ",total_rate/len(cartoons))
