# DemoFile.py 

#파일에 쓰기(wt - write text) 
#wite라는 키워드는 file.close() 를 자동으로 해줌
with open("DemoFile.txt", "wt", encoding="utf-8") as file:
    file.write("안녕하세요!\n")
    file.write("파일에 저장.\n")    


#파일 읽기(rt - read text)
with open("DemoFile.txt", "rt", encoding="utf-8") as file:
    content = file.read()
    print(content)  




