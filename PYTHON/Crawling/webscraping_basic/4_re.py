import re #정규식 라이브러리

# ca?e
# care, cafe ...
# caae, cabe, ...
p = re.compile("ca.e") 
# .(ca,e) : 하나의 문자를 의미 > care, cafe case (o) | caffe(x)
# ^(^de) : 문자열의 시작 >  desk, destination (o)| fade(x)
# $ (se$) : 문자열의 끝 > case, base (o) | face(x)


def print_match(m):
    #매칭되지않으면 에러 발생
    if m :
        print("m.group() : ",m.group()) #일치하는 문자열 반환
        print("m.string() : ",m.string) # 입력받은 문자열(함수가 아니라 변수라 괄호 없음)
        print("m.start() : ",m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : ",m.end()) # 일치하는 문자열의 끝 index
        print("m.span() : ",m.span()) # 일치하는 문자여릐 시작 / 끝 index
    else:
        print("매칭x")

m= p.match("careless") #match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
print()
m=p.search("good care") # 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)
print()
lst=p.findall("careless") # 일치하는 모든것을 리스트 형태로 반환
print(lst,"\n")
lst1=p.findall("good care cafe")
print(lst1)


# 1. p= re.compile("원하는 형태")
# 2. m=p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m=p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. 1st = p.findall("비교할 문자열") : 일치하는 모든것을 "리스트" 형태로 반환
