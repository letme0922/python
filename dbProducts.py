import sqlite3
import random
import string

class ProductDB:
    def __init__(self, db_name="MyProduct.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS Products (
                    productID INTEGER PRIMARY KEY,
                    productName TEXT NOT NULL,
                    productPrice INTEGER NOT NULL
                )
            """)

    def insert_product(self, productID, productName, productPrice):
        with self.conn:
            self.conn.execute(
                "INSERT INTO Products (productID, productName, productPrice) VALUES (?, ?, ?)",
                (productID, productName, productPrice)
            )

    def update_product(self, productID, productName=None, productPrice=None):
        with self.conn:
            if productName is not None and productPrice is not None:
                self.conn.execute(
                    "UPDATE Products SET productName=?, productPrice=? WHERE productID=?",
                    (productName, productPrice, productID)
                )
            elif productName is not None:
                self.conn.execute(
                    "UPDATE Products SET productName=? WHERE productID=?",
                    (productName, productID)
                )
            elif productPrice is not None:
                self.conn.execute(
                    "UPDATE Products SET productPrice=? WHERE productID=?",
                    (productPrice, productID)
                )

    def delete_product(self, productID):
        with self.conn:
            self.conn.execute(
                "DELETE FROM Products WHERE productID=?",
                (productID,)
            )

    def select_product(self, productID):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM Products WHERE productID=?",
            (productID,)
        )
        return cur.fetchone()

    def select_all(self, limit=10):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Products LIMIT ?", (limit,))
        return cur.fetchall()

    def close(self):
        self.conn.close()

    def insert_sample_data(self, count=100000):
        with self.conn:
            for i in range(1, count + 1):
                name = "Product_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
                price = random.randint(10000, 1000000)
                self.conn.execute(
                    "INSERT INTO Products (productID, productName, productPrice) VALUES (?, ?, ?)",
                    (i, name, price)
                )

if __name__ == "__main__":
    db = ProductDB()
    # 샘플 데이터 10만개 삽입 (이미 데이터가 있으면 중복 에러 발생 가능)
    db.insert_sample_data(100000)

    # 예시: 제품 1개 조회
    print(db.select_product(1))

    # 예시: 제품 10개 조회
    print(db.select_all(10))

    db.close()