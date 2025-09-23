# demoOSPath.py
import random
from os.path import *

print("---랜덤 모듈---")
print(random.random())  # 0.0 ~ 1.0 미만의 임의의 값
print(random.randint(1, 10))  # 1 ~ 10 사이의 임의의 정수 값
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20),10))
print(random.sample(range(20),10))



filePath = r"C:\python310\python.exe"
if exists(filePath):
    print("---os.path 모듈---")
    print("파일명:", basename(filePath))
    print("디렉터리명:", dirname(filePath))
    print("확장자명:", splitext(filePath)[1])
    print("파일크기:", getsize(filePath), "bytes")
    print("최종수정일:", getmtime(filePath))
    print("생성일:", getctime(filePath))
else:
    print(filePath, "파일이 없습니다.")

import glob
#특정 폴더의 파일 리스트
print(glob.glob(r"c:\work\*.py"))
