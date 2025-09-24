# web1.py
# 웹 크롤링 연습

from bs4 import BeautifulSoup

#웹페이지 로딩
page=open("test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup=BeautifulSoup(page, "html.parser")

# plist=soup.find_all("p")
# print(plist)

# p1=soup.find("p")
# print(p1)

# p2=soup.find_all("p", class_="outer-text")
# print(p2)

p3=soup.find_all("p", attrs={"class":"outer-text"})

for item in p3:
    title = item.text.strip()
    print(title)