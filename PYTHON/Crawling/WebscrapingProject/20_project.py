# 프로젝트) 웹 스크래핑을 이용하여 나만의 비서를 만들어보자 

# [조건]

# 1. 네이버에서 오늘 서울의 날씨 정보를 가져온다
# 2. 헤드라인 뉴스 3건을 가져온다
# 3. IT뉴스 3건을 가져온다
# 4. 해커스 어학원 홈페이지에서 오늘의 영어회화 지문을 가져온다

# [출력 예시]

# [오늘의 날씨]
# 흐림,어제보다 xx도 높아요
# 현재 xx도 (최저 xx도 / 최고 xx도)
# 오전 강수확률 xx도 / 오후 강수확률 xx도

# 미세먼지 xxxxx 좋음
# 초미세먼지 xxx 좋음

# [헤드라인 뉴스]
# 1. 무슨 무슨일이...
#     (링크 :  https:// .... )
# 2. 어떤 어떤 일이...
#     (링크 : https://....)
# 3. 이런 저런 일이...
#     (링크 : https://....)

# [IT 뉴스]
# 1. 무슨 무슨 일이...
#     (링크 : https://....)
# 2. 어떤 어떤 일이...
#     (링크 : https://....)
# 3. 이런 저런 일이...
#     (링크 : https://....)

# [오늘의 영어 회화]
# (영어 지문)
# json : how do you think bla bla??
# kim : well, i think blabla ... 

# (한글 지문)
# json : 어쩌구 저쩌구 어떻게 생각행?
# kim :  음 내생각엔 어쩌구 어쩌꾸 
from bs4 import BeautifulSoup
import lxml
import requests
import re
from selenium import webdriver

def create_soup(url):
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Accept-Language":"ko-KR,ko"}
    res =  requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def print_news(index,title,link):
    print("{}. {}".format(index+1,title))
    print(" (링크 : {})".format(link))



def scrape_weather():
    print("[오늘의 날씨]")
    url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    # 흐림,어제보다 xx도 높아요
    cast = soup.find("p",attrs={"class":"cast_txt"}).get_text()
    # 현재 xx도 (최저 xx도 / 최고 xx도)
    curr_temp = soup.find("p",attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span",attrs={"class":"min"}).get_text() # 최저 온도
    max_temp = soup.find("span",attrs={"class":"max"}).get_text() # 최고 온도
    # 오전 강수확률 xx도 / 오후 강수확률 xx도
    morning_rain_rate = soup.find("span",attrs={"class":"point_time morning"}).get_text().strip() # 오전 강수확률
    afternoon_rain_rate = soup.find("span",attrs={"class":"point_time afternoon"}).get_text().strip() # 오후 강수확률

    # 미세먼지 xxxxx 좋음
    # 초미세먼지 xxx 좋음
    
    # dust = soup.find("dl",attrs={"class":"indicator","id":"dust"},text=["미세먼지","초미세먼지"]) # 이런 문법 잘 알기 !!

    dust = soup.find("dl",attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text() # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지

    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp,min_temp,max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate,afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초 미세먼지 {}".format(pm25))
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li",limit=3) # li tag 를 모두 찾는데 3개까지만 가져와라!! 할수 있음 !! 개꿀팁!!
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        # [헤드라인 뉴스]
        # 1. 무슨 무슨일이...
        #     (링크 :  https:// .... )
        # 2. 어떤 어떤 일이...
        #     (링크 : https://....)
        # 3. 이런 저런 일이...
        #     (링크 : https://....)
        print_news(index,title,link)
    print()
    
def scrape_it_news():
    url="https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3) # 3개 까지만 가져오기 
    for index, news in enumerate(news_list):
        a_index=0
        img = news.find("img")
        if img:
            a_index=1 # 이미지 태그가 있으면 1번쨰 a 태그의 정보를 사용
        title = news.find_all("a")[a_index].get_text().strip()
        link = news.find_all("a")[a_index]["href"]
        print_news(index,title,link)

def scrape_english():
    print("[오늘의 영어 회화]")
    url="https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")}) # conv_kor_t 로 시작하는 id 에 해당하는 div tag를 가져옴
    print("(영어지문)")
    for sentence in sentences[len(sentences)//2:]: # 8 문장이 있다고 가정할 때 4~7 까지(인덱스 기준) 잘라서 가져옴
        print(sentence.get_text().strip())
    print()
    print("(한글지문)")
    for sentence in sentences[:len(sentences)//2]: # 8 문장이 있다고 가정할 때 0~3 까지(인덱스 기준) 잘라서 가져옴
        print(sentence.get_text().strip())


if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기 
    scrape_headline_news() # 헤드라인 뉴스 가져오기
    scrape_it_news() # IT뉴스 정보 가져오기 
    scrape_english() # 오늘의 영어회화 가져오기


