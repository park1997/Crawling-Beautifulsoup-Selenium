import requests
res = requests.get("http://naver.com")
res1 = requests.get("http://nadocoding.tistory.com")
res2 = requests.get("http://google.com")
print("응답 코드 : ",res.status_code) #200이면 정상 작동된것
print("응답 코드 2: ",res1.status_code)

if res.status_code==200:
    print("정상입니다.")
else:
    print("문제가 생겼스비다 . 에러코드 [",res1.status_code,"]")

#if 문을 쓰지 않고도 raise_for_status로 에러인지 확인가능 하다.
res.raise_for_status()
print("웹스크래핑을 진행합니다.")

print(len(res2.text))
with open("mygoogle.html","w",encoding="UTF-8") as f:
    f.write(res2.text)