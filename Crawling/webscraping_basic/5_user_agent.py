import requests
url="http://nadocoding.tistory.com"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res=requests.get(url,headers=headers)
# res.raise_for_status()
with open("nadocodig.html","w",encoding="UTF-8") as f:
    f.write(res.text)


# USERAGENT

# 스마트폰으로 접속하는지 웹으로 접속하는지 보여줌
# 일반적인 경로로 들어가지 않을때는 경로를 막거나 권한을 ㅜ찌 않을 수도있음
# 그럴떄 useragent를 줘서 사람 맞아요! 라고 할 수있음





