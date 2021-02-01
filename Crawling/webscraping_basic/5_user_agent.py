import requests
url="http://nadocoding.tistory.com"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res=requests.get(url,headers=headers)
# res.raise_for_status()
with open("nadocodig.html","w",encoding="UTF-8") as f:
    f.write(res.text)






