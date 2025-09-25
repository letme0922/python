# web2.py
#클리앙 웹사이트 중고장터 
from bs4 import BeautifulSoup
import urllib.request
import re 



#파일에 저장
f = open("clien.txt", "wt", encoding="utf-8")

#페이징처리 
for i in range(0,10):
    #웹서버에 데이터 전달: QueryString방식 
    url = "https://www.clien.net/service/board/" \
        + "sold?&od=T31&category=0&po=" + str(i)
    print(url)
    #페이지 실행 결과 문자열 
    data = urllib.request.urlopen(url)
    #스프 객체 생성
    soup = BeautifulSoup(data, 'html.parser')
    #중고장터매물 제목
    list = soup.find_all("span", 
        attrs={"data-role":"list-title-text"})
    for item in list:
        #문자열 가공 
        title = item.text.strip()
        print(title)
        f.write(title + "\n")

#1열에서 코딩 
f.close()

#선택한 블럭 주석: ctrl + /
# <span class="subject_fixed" data-role="list-title-text" title="아이폰15프로 화이트 256GB팝니다(애캐플26.04.24까지)">
# 			아이폰15프로 화이트 256GB팝니다(애캐플26.04.24까지)
# </span>