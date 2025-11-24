# ไฟล์: db_functions.py
# ฟังก์ชันสำหรับจัดการ Database

import sqlite3

# ฟังก์ชันที่ 1: ดึงสินค้าทั้งหมด
def get_all_products():
    """ดึงข้อมูลสินค้าทั้งหมด"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, name, retail_price, current_stock, unit
        FROM products
        ORDER BY name
    ''')
    
    products = cursor.fetchall()
    conn.close()
    
    return products


# ฟังก์ชันที่ 2: ค้นหาสินค้าตามชื่อ
def search_product_by_name(keyword):
    """ค้นหาสินค้าด้วยชื่อ"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, name, retail_price, current_stock, unit
        FROM products
        WHERE name LIKE ?
        ORDER BY name
    ''', (f'%{keyword}%',))
    
    products = cursor.fetchall()
    conn.close()
    
    return products


# ฟังก์ชันที่ 3: ดึงสินค้าตาม ID
def get_product_by_id(product_id):
    """ดึงข้อมูลสินค้า 1 รายการ"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, name, retail_price, current_stock, unit, cost_price
        FROM products
        WHERE id = ?
    ''', (product_id,))
    
    product = cursor.fetchone()
    conn.close()
    
    return product


# ฟังก์ชันที่ 4: ดึงสินค้าที่มีสต็อก
def get_products_in_stock():
    """ดึงสินค้าที่มีสต็อก"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, name, retail_price, current_stock, unit
        FROM products
        WHERE current_stock > 0
        ORDER BY current_stock DESC
    ''')
    
    products = cursor.fetchall()
    conn.close()
    
    return products


# ฟังก์ชันที่ 5: คำนวณมูลค่าสต็อกทั้งหมด
def get_total_stock_value():
    """คำนวณมูลค่าสต็อก"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            SUM(cost_price * current_stock) as total_cost,
            SUM(retail_price * current_stock) as total_retail,
            SUM((retail_price - cost_price) * current_stock) as profit
        FROM products
        WHERE current_stock > 0
    ''')
    
    result = cursor.fetchone()
    conn.close()
    
    return {
        'total_cost': result[0] or 0,
        'total_retail': result[1] or 0,
        'profit': result[2] or 0
    }


# ฟังก์ชันที่ 6: ดึงหมวดหมู่ทั้งหมด
def get_all_categories():
    """ดึงหมวดหมู่ทั้งหมด"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, name, description FROM categories ORDER BY name')
    
    categories = cursor.fetchall()
    conn.close()
    
    return categories


# ฟังก์ชันที่ 7: ดึงสินค้าตามหมวดหมู่
def get_products_by_category(category_id):
    """ดึงสินค้าตามหมวดหมู่"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.id, p.name, p.retail_price, p.current_stock, p.unit
        FROM products p
        WHERE p.category_id = ?
        ORDER BY p.name
    ''', (category_id,))
    
    products = cursor.fetchall()
    conn.close()
    
    return products


# ทดสอบฟังก์ชัน (ถ้ารันไฟล์นี้โดยตรง)
if __name__ == "__main__":
    print("🧪 ทดสอบฟังก์ชัน")
    print("=" * 50)
    
    # ทดสอบ 1: ดูสินค้าทั้งหมด
    print("\n1 สินค้าทั้งหมด:")
    all_products = get_all_products()
    print(f"   มีสินค้า {len(all_products)} รายการ")
    
    # ทดสอบ 2: ค้นหาสินค้า
    print("\n2 ค้นหาสินค้าที่มีคำว่า 'Milk':")
    search_results = search_product_by_name("Milk")
    for product in search_results:
        print(f"   - {product[1]}: {product[2]} บาท")
    
    # ทดสอบ 3: ดูสินค้าที่มีสต็อก
    print("\n3 สินค้าที่มีสต็อก:")
    in_stock = get_products_in_stock()
    print(f"   มี {len(in_stock)} รายการ")
    
    # ทดสอบ 4: คำนวณมูลค่า
    print("\n4 มูลค่าสต็อกทั้งหมด:")
    stock_value = get_total_stock_value()
    print(f"   ลงทุน: {stock_value['total_cost']:.2f} บาท")
    print(f"   มูลค่า: {stock_value['total_retail']:.2f} บาท")
    print(f"   กำไร: {stock_value['profit']:.2f} บาท")
    
    # ทดสอบ 5: ดูหมวดหมู่
    print("\n5 หมวดหมู่ทั้งหมด:")
    categories = get_all_categories()
    for cat in categories:
        print(f"   - {cat[1]}")

# ========================================
# ฟังก์ชันสำหรับเขียนข้อมูล (CREATE)
# ========================================

def add_product(name, category_id, unit, cost_price, retail_price, 
                name_th=None, wholesale_price=None, barcode=None, 
                min_wholesale_qty=10, min_stock_level=10, has_expiry_date=0):
    """เพิ่มสินค้าใหม่
    
    Args:
        name (str): ชื่อภาษาอังกฤษ (บังคับ)
        name_th (str): ชื่อภาษาไทย (ไม่บังคับ)
        category_id (int): รหัสหมวดหมู่
        unit (str): หน่วย
        cost_price (float): ราคาทุน
        retail_price (float): ราคาขาย
        ...
    """
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO products 
            (barcode, name, name_th, category_id, unit, cost_price, retail_price, 
             wholesale_price, min_wholesale_qty, min_stock_level, has_expiry_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (barcode, name, name_th, category_id, unit, cost_price, retail_price,
              wholesale_price, min_wholesale_qty, min_stock_level, has_expiry_date))
        
        conn.commit()
        product_id = cursor.lastrowid
        conn.close()
        
        return {"success": True, "product_id": product_id, "message": "เพิ่มสินค้าสำเร็จ"}
    
    except sqlite3.IntegrityError as e:
        return {"success": False, "message": f"Error: {str(e)}"}
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}


def add_category(name, name_th=None, description=None):
    """เพิ่มหมวดหมู่ใหม่
    
    Args:
        name (str): ชื่อภาษาอังกฤษ
        name_th (str): ชื่อภาษาไทย
        description (str): คำอธิบาย
    """
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO categories (name, name_th, description)
            VALUES (?, ?, ?)
        ''', (name, name_th, description))
        
        conn.commit()
        category_id = cursor.lastrowid
        conn.close()
        
        return {"success": True, "category_id": category_id, "message": "เพิ่มหมวดหมู่สำเร็จ"}
    
    except sqlite3.IntegrityError:
        return {"success": False, "message": "หมวดหมู่นี้มีอยู่แล้ว"}
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}
    
# ========================================
# ฟังก์ชันสำหรับแก้ไขข้อมูล (UPDATE)
# ========================================

def update_product_price(product_id, cost_price=None, retail_price=None, wholesale_price=None):
    """แก้ไขราคาสินค้า"""
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        # สร้าง SQL แบบ dynamic
        updates = []
        params = []
        
        if cost_price is not None:
            updates.append("cost_price = ?")
            params.append(cost_price)
        
        if retail_price is not None:
            updates.append("retail_price = ?")
            params.append(retail_price)
        
        if wholesale_price is not None:
            updates.append("wholesale_price = ?")
            params.append(wholesale_price)
        
        if not updates:
            return {"success": False, "message": "ไม่มีข้อมูลที่ต้องแก้ไข"}
        
        params.append(product_id)
        sql = f"UPDATE products SET {', '.join(updates)} WHERE id = ?"
        
        cursor.execute(sql, params)
        conn.commit()
        
        if cursor.rowcount == 0:
            conn.close()
            return {"success": False, "message": "ไม่พบสินค้า"}
        
        conn.close()
        return {"success": True, "message": "แก้ไขราคาสำเร็จ"}
    
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}


def update_product_stock(product_id, quantity, operation='set'):
    """อัพเดทสต็อกสินค้า
    
    operation:
    - 'set': ตั้งค่าเป็น quantity
    - 'add': เพิ่ม quantity
    - 'subtract': ลด quantity
    """
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        if operation == 'set':
            sql = "UPDATE products SET current_stock = ? WHERE id = ?"
            cursor.execute(sql, (quantity, product_id))
        
        elif operation == 'add':
            sql = "UPDATE products SET current_stock = current_stock + ? WHERE id = ?"
            cursor.execute(sql, (quantity, product_id))
        
        elif operation == 'subtract':
            # ตรวจสอบว่าสต็อกพอหรือไม่
            cursor.execute("SELECT current_stock FROM products WHERE id = ?", (product_id,))
            result = cursor.fetchone()
            
            if not result:
                conn.close()
                return {"success": False, "message": "ไม่พบสินค้า"}
            
            current = result[0]
            if current < quantity:
                conn.close()
                return {"success": False, "message": f"สต็อกไม่พอ (มีอยู่ {current})"}
            
            sql = "UPDATE products SET current_stock = current_stock - ? WHERE id = ?"
            cursor.execute(sql, (quantity, product_id))
        
        conn.commit()
        conn.close()
        
        return {"success": True, "message": "อัพเดทสต็อกสำเร็จ"}
    
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}
    
# ========================================
# ฟังก์ชันสำหรับลบข้อมูล (DELETE)
# ========================================

def delete_product(product_id):
    """ลบสินค้า"""
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        # ตรวจสอบว่ามีสินค้าหรือไม่
        cursor.execute("SELECT name FROM products WHERE id = ?", (product_id,))
        result = cursor.fetchone()
        
        if not result:
            conn.close()
            return {"success": False, "message": "ไม่พบสินค้า"}
        
        product_name = result[0]
        
        # ลบสินค้า
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        conn.close()
        
        return {"success": True, "message": f"ลบสินค้า '{product_name}' สำเร็จ"}
    
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}


def deactivate_product(product_id):
    """ปิดการขายสินค้า (แทนการลบ - แนะนำ)"""
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute("UPDATE products SET is_active = 0 WHERE id = ?", (product_id,))
        
        if cursor.rowcount == 0:
            conn.close()
            return {"success": False, "message": "ไม่พบสินค้า"}
        
        conn.commit()
        conn.close()
        
        return {"success": True, "message": "ปิดการขายสินค้าสำเร็จ"}
    
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}
    
# ========================================
# ฟังก์ชันสำหรับจัดการ 2 ภาษา
# ========================================

def get_all_products_bilingual():
    """ดึงสินค้าทั้งหมด (2 ภาษา)"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, name, name_th, retail_price, current_stock, unit
        FROM products
        ORDER BY name
    ''')
    
    products = cursor.fetchall()
    conn.close()
    
    return products


def search_product_bilingual(keyword):
    """ค้นหาสินค้า (ทั้งภาษาอังกฤษและไทย)"""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, name, name_th, retail_price, current_stock, unit
        FROM products
        WHERE name LIKE ? OR name_th LIKE ?
        ORDER BY name
    ''', (f'%{keyword}%', f'%{keyword}%'))
    
    products = cursor.fetchall()
    conn.close()
    
    return products


def get_product_display_name(product_id, language='th'):
    """ดึงชื่อสินค้าตามภาษาที่เลือก
    
    Args:
        product_id (int): รหัสสินค้า
        language (str): 'th' หรือ 'en'
    """
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT name, name_th FROM products WHERE id = ?', (product_id,))
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        return None
    
    name_en, name_th = result
    
    if language == 'th' and name_th:
        return name_th
    else:
        return name_en


def update_product_name_th(product_id, name_th):
    """อัพเดทชื่อภาษาไทย"""
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute('UPDATE products SET name_th = ? WHERE id = ?', (name_th, product_id))
        
        if cursor.rowcount == 0:
            conn.close()
            return {"success": False, "message": "ไม่พบสินค้า"}
        
        conn.commit()
        conn.close()
        
        return {"success": True, "message": "อัพเดทชื่อไทยสำเร็จ"}
    
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}