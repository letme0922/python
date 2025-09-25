#라이브러리를 사용하면 선언부가 늘어난다! 
import sqlite3
import random

class ProductDatabase:
    def __init__(self, db_name="MyProduct.db"):
        self.db_name = db_name
        self.create_table()
    
    def create_table(self):
        """테이블 생성"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                productID INTEGER PRIMARY KEY,
                productName TEXT NOT NULL,
                productPrice INTEGER NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def insert_product(self, name, price):
        """제품 추가"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Products (productName, productPrice)
            VALUES (?, ?)
        ''', (name, price))
        
        conn.commit()
        conn.close()
    
    def update_product(self, product_id, name=None, price=None):
        """제품 정보 수정"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        if name and price:
            cursor.execute('''
                UPDATE Products 
                SET productName = ?, productPrice = ?
                WHERE productID = ?
            ''', (name, price, product_id))
        elif name:
            cursor.execute('''
                UPDATE Products 
                SET productName = ?
                WHERE productID = ?
            ''', (name, product_id))
        elif price:
            cursor.execute('''
                UPDATE Products 
                SET productPrice = ?
                WHERE productID = ?
            ''', (price, product_id))
            
        conn.commit()
        conn.close()
    
    def delete_product(self, product_id):
        """제품 삭제"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            DELETE FROM Products 
            WHERE productID = ?
        ''', (product_id,))
        
        conn.commit()
        conn.close()
    
    def select_all_products(self):
        """모든 제품 조회"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM Products')
        products = cursor.fetchall()
        
        conn.close()
        return products
    
    def generate_sample_data(self, count=100000):
        """샘플 데이터 생성"""
        product_types = ['스마트폰', '노트북', '태블릿', 'TV', '모니터', '이어폰', '스피커', '키보드', '마우스', '프린터']
        brands = ['삼성', 'LG', '애플', '소니', '레노버', '에이서', '아수스', '델', 'HP', '필립스']
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        for _ in range(count):
            name = f"{random.choice(brands)} {random.choice(product_types)} {random.randint(1, 9)}세대"
            price = random.randint(50000, 2000000)
            
            cursor.execute('''
                INSERT INTO Products (productName, productPrice)
                VALUES (?, ?)
            ''', (name, price))
            
        conn.commit()
        conn.close()

# 사용 예시
def main():
    # 데이터베이스 인스턴스 생성
    db = ProductDatabase()
    
    # 샘플 데이터 생성
    print("샘플 데이터 생성 중...")
    db.generate_sample_data()
    print("샘플 데이터 생성 완료!")
    
    # 데이터 조회 예시
    products = db.select_all_products()
    print(f"\n전체 제품 수: {len(products)}")
    print("\n처음 5개 제품:")
    for product in products[:5]:
        print(f"ID: {product[0]}, 이름: {product[1]}, 가격: {product[2]:,}원")
    
    # 데이터 수정 예시
    db.update_product(1, price=999000)
    
    # 데이터 삭제 예시
    db.delete_product(2)

if __name__ == "__main__":
    main()