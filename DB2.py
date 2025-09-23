# db1.py 
import sqlite3

#연결객체를 생성:파일에 영구적으로 저장(sample.db) 
#raw string 사용
con = sqlite3.connect(r"c:\work\sample.db")
#커서객체를 리턴 
cur = con.cursor()
#테이블 생성(SQL구문은 대소문자를 구분하지 않음)
#테이블이 이미 존재하면 무시
cur.execute(
"create table if not exists PhoneBook (name text, phoneNum text);")
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


print("---fetchall()---") 
cur.execute("select * from PhoneBook;") 
print(cur.fetchall()) #나머지 행 리턴

#쓰기작업 
con.commit()