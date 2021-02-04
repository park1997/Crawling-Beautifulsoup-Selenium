import re
from bs4 import BeautifulSoup
import lxml
import requests

#다음 영화순위 2011~2019 까지 앞 5개만 추출

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
for i in range(9,0,-1):
    url="https://search.daum.net/search?w=tot&q=201{}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(i)
    res= requests.get(url,headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    images = soup.find_all("img",attrs={"class":"thumb_img"})
    for idx,image in enumerate(images):
        
        # 상위 5개 이미지만 다운로드 받겠음!
        if idx>=4:
            break
        #print(image["src"])
        image_url=image["src"]
        if image_url.startswith("//"):
            image_url="https:"+image_url
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # wb => write binary
        with open("movie{}_{}.jpg".format(i,idx+1),"wb") as f:
            # 이 리소스가 가지고있는 컨텐트 정보(이미지)를 파일로 씀
            f.write(image_res.content)
        