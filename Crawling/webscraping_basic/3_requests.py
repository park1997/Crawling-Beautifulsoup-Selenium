import requests
res = requests.get("http://naver.com")
res1 = requests.get("http://nadocoding.tistory.com")
res2 = requests.get("http://google.com")
print("응답 코드 : ",res.status_code) #200이면 정상 작동된것
print("응답 코드 2: ",res1.status_code)

if res.status_code==200:
    print("정상입니다.")
else:
    print("문제가 생겼습니다 . 에러코드 [",res1.status_code,"]")

#if 문을 쓰지 않고도 raise_for_status로 에러인지 확인가능 하다.
res.raise_for_status()
print("웹스크래핑을 진행합니다.")

print(len(res2.text))
with open("mygoogle.html","w",encoding="UTF-8") as f:
    f.write(res2.text)

# requests

# 웹페이지를 읽어올때 쓰임

# 하지만 동적인 웹페이지를 읽을떄 안됨
# 셀레늄은 느리지만 동적인 웹페이지를 읽을떄 가능

# res.raise_for_status() 는 접속에 문제가 있는지 없는지 확인하는 역할
