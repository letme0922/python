# demoFile.py
#파일에 쓰기
with open("demofile.txt", "wt", encoding="utf-8") as file:
    file.write("안녕하세요!\n")
    file.write("파일에 저장.\n")

# 파일 읽기
with open("demofile.txt", "rt", encoding="utf-8") as file:
    content = file.read()
    print(content)
