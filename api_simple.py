# ไฟล์: api_simple.py
from fastapi import FastAPI
import sqlite3

app = FastAPI(title="🏪 ร้านค้า API", version="1.0.0")

@app.get("/")
def home():
    return {"message": "✅ API ทำงานปกติ", "status": "online"}

@app.get("/test")
def test():
    return {"test": "สวัสดี", "number": 123}

@app.get("/products")
def get_products():
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, retail_price FROM products LIMIT 10')
        products = cursor.fetchall()
        conn.close()
        
        result = [{"id": p[0], "name": p[1], "price": p[2]} for p in products]
        return {"success": True, "total": len(result), "products": result}
    except Exception as e:
        return {"success": False, "error": str(e)}