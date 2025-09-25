# db1.py 
import sqlite3

#연결객체를 생성(일단 메모리에서 작업)
con = sqlite3.connect(":memory:")
#커서객체를 리턴 
cur = con.cursor()
#테이블 생성(SQL구문은 대소문자를 구분하지 않음)
cur.execute(
"create table PhoneBook (name text, phoneNum text);")
#데이터 삽입
cur.execute(
    "insert into PhoneBook (name, phoneNum) values (?, ?);",
    ("Alice", "123-456-7890"))

#파라메터를 입력 
name = "전우치"
phoneNum = "010-1234-5678"
cur.execute(
    "insert into PhoneBook (name, phoneNum) values (?, ?);",
    (name, phoneNum))

#다중의 행을 입력 
datalist = (("박문수","010-222-3333"), ("이순신","010-333-1234"))
cur.executemany(
    "insert into PhoneBook (name, phoneNum) values (?, ?);",
    datalist)

#검색 
for row in cur.execute("select * from PhoneBook;"):
    print(row)

