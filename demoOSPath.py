# demoOSPath.py 
import random
from os.path import * 

print("---랜덤모듈---")
print(random.random()) # 0.0 ~ 1.0 사이의 실수
print(random.randint(1, 10)) # 1 ~ 10 사이의 정수
print([random.randrange(20) for i in range(10)]) # 0 ~ 19 사이의 정수 5개
print([random.randrange(20) for i in range(10)]) # 0 ~ 19 사이의 정수 5개
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

#파이썬 파일의 경로 
#raw string notation 
filePath = r"c:\python310\python.exe"
if exists(filePath):
    print("파일이 존재합니다.")
    print("파일명:", basename(filePath))
    print("디렉토리명:", dirname(filePath))
    print("파일 크기:", getsize(filePath))
else:
    print("파일이 존재하지 않습니다.")

import glob 
#특정 폴더의 파일 리스트 
print(glob.glob(r"c:\work\*.py"))

import os 
print(os.getcwd()) #현재 작업 디렉토리
print("운영체제명:", os.name) #운영체제명
print("환경변수:", os.environ) #환경변수
os.system("notepad.exe") #메모장 실행

