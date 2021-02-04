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

def create_soup(url):
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    res= requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup



# 백그라운드에서 실행 (메모리 효율을 늘릴 수 있음)
# options = webdriver.ChromeOptions()
# options.headless = True

# 나의 컴퓨터 전체화면 크기로 실행
# options.add_argument("window-size=3072x1920") 

# 모든 내용이 담긴 Json형태의 데이터
info={}

# 네이버 부동산 URL
url="https://new.land.naver.com/complexes/"

# 실제 접속하는 것 처럼 보이는 headers
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Accept-Language":"ko-KR,ko"}

# 크롬 웹드라이버 백그라운드X
browser = webdriver.Chrome("./chromedriver")
# 크롬 웹드라이버 백그라운드에서 실행 O
# browser = webdriver.Chrome("./chromedriver",options=options)


# 검색할 아파트의 고유 번호 입력
# num = input("아파트의 고유 번호 입력 >")

# URL + 고유번호
# url = url + num
url += "1525"
# 페이지 이동
browser.get(url)

# 창 최대화
browser.maximize_window()

# 문서의 높이만큼 스크롤을 내림
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# window.scrollTo(0,document.querySelector(".scrollingContainer").scrollHeight)

# 1초에 1번 스크롤 내림
interval = 1

# 동일 매물 묶기
browser.find_element_by_class_name("address_filter").click()



prev = len(browser.find_elements_by_class_name("item_link"))

# # 반복 수행
# while True:
#     # 현재 보이는 매물의 elements
#     elem=browser.find_elements_by_class_name("item_link")
#     # 맨밑 요소 클릭하면 매물이 업데이트됨
#     elem[prev-1].click()
#     # 로딩으로인한 오류 제거를위해 1초간 쉬어줌
#     time.sleep(interval)
#     # 현재 매물 개수 업데이트
#     curr = len(elem)
#     # 이전 매물개수와 현재매물 개수가 같다는건 더이상 업데이트 할매물이 없다는 뜻
#     if prev==curr:
#         break
    
#     # 매물 개수 업데이트 
#     prev = curr

print("스크롤 완료!")

# 현재 페이지 소스를 lxml 로 parsing 함
soup = BeautifulSoup(browser.page_source,"lxml")

# 단지 명 
complex_title = soup.find("h3",attrs={"class":"title","id":"complexTitle"}).get_text()
info["단지 명"]=complex_title

# 단지 종류(오피스텔,아파트 ...)
complex_type = soup.find("span",attrs={"class":"label--category"}).get_text()
info["단지 종류"]=complex_type

# 단지정보 클릭
browser.find_element_by_xpath("//*[@id=\"summaryInfo\"]/div[2]/div[2]/button[1]").click()

# 로딩으로 인해 크롤링이 안될 수 있으므로 1초 쉬어줌
time.sleep(interval)

# soup 객체 다시 받아옴
soup = BeautifulSoup(browser.page_source,"lxml")

# 데이터가 들어갈 임시 저장소 
temp = []
items = soup.find("div",attrs={"class":"infinite_scroll "})

# 단지 정보 테이블 소스코드
complex_infos = soup.find("table",attrs={"class":"info_table_wrap"}).find_all("tr",attrs={"class":"info_table_item"})

# 딕셔너리를 만들기위해 key, value 값을 리스트에 저장
detail_infos_key = []
detail_infos_value = []

# for문을 이용하여 단지정보 추출
for complex_info in complex_infos:
    for details in complex_info.find_all("th",attrs={"class":"table_th"}):
        detail_infos_key.append(details.get_text())
    for details in complex_info.find_all("td",attrs={"class":"table_td"}):
        detail_infos_value.append(details.get_text())

# 단지정보 key,value 값을 대응시켜 딕셔너리에 데이터 저장
for i in range(len(detail_infos_key)):
    info[detail_infos_key[i]] = detail_infos_value[i]

# 단지 내 면적별 정보 테이블
size_infos = soup.find("div",attrs = {"class":"detail_box--floor_plan"})

# "단지 내 면적별 정보"
width_info_name = size_infos.find("h5",attrs = {"class":"heading_text"}).get_text()
info[width_info_name] = {}

# soup 객체 정보 업데이트
soup = BeautifulSoup(browser.page_source,"lxml")


# 면적 종류 정보 
width_info = soup.find("span",attrs = {"class":"detail_sorting_width"}).find_all("a",attrs = {"class":"detail_sorting_tab"})

# 더보기 탭이 있을 경우 탭을 누른다 !
if soup.find("div",attrs = {"class":"btn_moretab_box"}):
    browser.find_element_by_xpath("//*[@id=\"detailContents1\"]/div[2]/div[2]/div/div[2]/button").click()
temp={}
# 단지 면적별로 클릭하여 각 면적에 해당하는 정보 가져오기 !
for num in range(len(width_info)):
    #각 면적 클릭을위한 xpath
    xpath="//*[@id=\"tab{}\"]".format(num)

    # for loop 에 따라 해당하는 평수 클릭
    browser.find_element_by_xpath(xpath).click()
    
    # 로딩시간 고려하여 1초 동안 쉼
    # time.sleep(interval)
    
    # soup 객체 정보 업데이트 
    soup = BeautifulSoup(browser.page_source,"lxml")
    

    # 현재 Loop에 해당하는 평수 
    size = soup.find("div",attrs = {"class":"detail_sorting_inner"}).find("span",attrs = {"class":"text"}).get_text()
    
    size_infos_table = soup.find("div",attrs = {"class":"detail_box--floor_plan"}).find("table",attrs = {"class":"info_table_wrap"}).find_all("tr",attrs = {"class":"info_table_item"})
    # rowspan 이 2 인경우를 탐지하기 위한 변수 
    checking_boolean = True
    title_for_rowspan = ""
    for details_table in size_infos_table:
        title = ""
        detail = ""
        temp_list=[]
        try: 
            # 공급/전용 , 방수/욕실수 , 해당면적 세대수 , 현관구조 , 공시가격
            if details_table.find("th",attrs = {"class":"table_th"}) and details_table.find("td",attrs = {"class":"table_td"}) and checking_boolean and (not details_table.find("th",attrs = {"rowspan":"2"})):
                title = details_table.find("th",attrs = {"class":"table_th"}).get_text()
                if details_table.find("strong"):
                    detail = details_table.find("strong").get_text()
                else:
                    detail = details_table.find("td",attrs = {"class":"table_td"}).get_text()
                info[width_info_name][title]=detail
            # 해당면적 매물, 관리비 , 보유세
            elif details_table.find("th",attrs={"rowspan":"2"}) and checking_boolean and details_table.find("a"):
                # 소 분류 이름
                title = details_table.find("th", attrs={"rowspan":"2"}).get_text()
                # rowspan 으로 인해 다음 태그에서 title 값 못가져오므로 다른 변수에 타이틀값 저장
                title_for_rowspan = title
                detail_infos = details_table.find_all("a",attrs={"class":"data"})
                for detail_info in detail_infos:
                    detail_info_name = detail_info.get_text()
                    detail_info_num = detail_info.find("span").get_text()
                    temp_list.append(detail_info_name+" : "+detail_info_num)
                info[width_info_name][title]=temp_list
                checking_boolean = False
            # rowspan = 2 다음 태그 , 해당면적 매물, 관리비, 보유세
            elif (not checking_boolean) and details_table.find("ul"):
                detail_infos = details_table.find_all("li",attrs={"class":"info_list_item"})
                for detail_info in detail_infos:
                    detail = detail_info.get_text().strip()
                    info[width_info_name][title_for_rowspan].append(detail)
                checking_boolean = True
                title_for_rowspan = ""
            # 
            elif checking_boolean and details_table.find("th",attrs={"class":"table_th","rowspan":"2"}):
                title = details_table.find("th",attrs={"class":"table_th"}).get_text()
                title_for_rowspan = title
                detail = details_table.find("strong").get_text()
                temp_list.append(detail)
                info[width_info_name][title]=temp_list
                checking_boolean = False
        except :
            # 예외처리
            pass
    # 면적별로 묶어서 Json형태로 
    temp[width_info[num].get_text()]=info[width_info_name]
# info에 저장
info[width_info_name]=temp
# print(info)

# 재사용을 위한 temp 초기화
temp={}

# 로딩으로 인한 오류 방지를위한 interval
time.sleep(interval)

# "시세/실거래가"
actual_transaction = soup.find("button",attrs={"class":"complex_link","data-nclk":"CID.sise"}).get_text()

# {"시세/실거래가" : {}}
info[actual_transaction]={}

# 시세 실거래가 클릭
browser.find_element_by_xpath("//*[@id=\"summaryInfo\"]/div[2]/div[2]/button[2]").click()

# soup 객체 업데이트
soup = BeautifulSoup(browser.page_source,"lxml")


# 시세/실거래가 면적 정보[x,x,x,x,x]
width_info = soup.find("div",attrs={"class":"detail_tabpanel"}).find_all("a",attrs={"class":"detail_sorting_tab"})


for num in range(len(width_info)):
    # 시세/실거래가 면적 for loop 를 통해 클릭
    browser.find_element_by_link_text(width_info[num].get_text()).click()
    
    # {"시세/실거래가" : {"76m": {}}}
    info[actual_transaction][width_info[num].get_text()] = {}

    # soup 객체 업데이트
    soup = BeautifulSoup(browser.page_source,"lxml")
    
    # 매매, 전세, 월세 
    selling_type = soup.find_all("a",attrs={"id":re.compile("^marketPriceTab")})

    # 월세는 구하지 않는 걸로 하므로 for loop 의 횟수를 1회 줄임
    for i in range(len(selling_type)-1):
        id = "marketPriceTab{}".format(i+1)

        # 매매, 전세 클릭
        browser.find_element_by_id(id).click()
        
        # soup 객체 업데이트
        soup = BeautifulSoup(browser.page_source,"lxml")
        

        # {"시세/실거래가" : {"76m": {"매매": {}}}}
        info[actual_transaction][width_info[num].get_text()][selling_type[i].get_text()] = {}
        
        if soup.find("div",attrs={"class":"detail_asking_price"}):
            # 상한가 하한가 정보가 들은 테이블 소스
            min_max_table = soup.find_all("div",attrs={"class":"detail_table_cell"})

            # "하한가", 하한가의 가격을 가져오기
            min_name = min_max_table[0].find("span").get_text()
            min_price = min_max_table[0].find("strong").get_text()

            # "상한가", 상한가의 가격을 가져오기 
            max_name = min_max_table[1].find("span").get_text()
            max_price = min_max_table[1].find("strong").get_text()

            # 매매가 대비 전세가, 그 에 해당하는 퍼센트를 가져옴
            rent_fee_name = min_max_table[2].find("span").get_text()
            rent_fee_price = min_max_table[2].find("strong").get_text()

            # 크롤링한 데이터를 Json형태로 저장
            info[actual_transaction][width_info[num].get_text()][selling_type[i].get_text()][min_name] = min_price
            info[actual_transaction][width_info[num].get_text()][selling_type[i].get_text()][max_name] = max_price
            info[actual_transaction][width_info[num].get_text()][selling_type[i].get_text()][rent_fee_name] = rent_fee_price            
        else:
            # 그에 해당하는 데이터가 없을 경우 "해당 기간 내 시세 및 실거래 정보가 없습니다." 출력
            info[actual_transaction][width_info[num].get_text()][selling_type[i].get_text()] = "해당 기간 내 시세 및 실거래가 정보가 없습니다"
        
print(info)

# 브라우저 종료전 1초 쉬기
time.sleep(interval)
# 브라우저 종료
browser.quit()
