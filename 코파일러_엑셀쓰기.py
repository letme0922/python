# products.xlsx 파일로 전자제품 판매 데이터 100개 생성 및 저장
import random
from openpyxl import Workbook

# 샘플 제품명 리스트
product_names = [
    "스마트폰", "노트북", "태블릿", "스마트워치", "이어폰", "헤드폰", "모니터", "키보드", "마우스", "프린터",
    "카메라", "스피커", "TV", "프로젝터", "게임기", "공기청정기", "로봇청소기", "냉장고", "세탁기", "전자레인지"
]

wb = Workbook()
ws = wb.active
ws.title = "Products"

# 헤더 작성
ws.append(["제품ID", "제품명", "수량", "가격"])

for i in range(1, 101):
    product_id = f"P{i:04d}"
    product_name = random.choice(product_names)
    quantity = random.randint(1, 50)
    price = random.randint(50000, 2000000)
    ws.append([product_id, product_name, quantity, price])

wb.save("products.xlsx")