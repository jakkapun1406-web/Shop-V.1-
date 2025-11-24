#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ไฟล์: main_fixed.py
โปรแกรมหลักสำหรับจัดการร้านค้า (แก้ไขปัญหาภาษาไทยแล้ว)
"""

import os
import sys
from pathlib import Path

# เพิ่ม path และจัดการ directory
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))
os.chdir(current_dir)

# Import ฟังก์ชันจากฐานข้อมูล
from db_functions import *

def show_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*50)
    print("🏪 ระบบจัดการร้านค้า")
    print("="*50)
    print("1. ดูสินค้าทั้งหมด")
    print("2. ค้นหาสินค้า")
    print("3. ดูสินค้าที่มีสต็อก")
    print("4. ดูมูลค่าสต็อก")
    print("5. ดูหมวดหมู่")
    print("6. ดูสินค้าตามหมวดหมู่")
    print("0. ออกจากโปรแกรม")
    print("="*50)


def display_products(products):
    """แสดงรายการสินค้า (รองรับ 2 ภาษา)"""
    if not products:
        print("❌ ไม่พบสินค้า")
        return
    
    print("\n" + "-"*120)
    print(f"{'ID':<5} {'ชื่อภาษาอังกฤษ':<35} {'ชื่อภาษาไทย':<35} {'ราคา':<10} {'สต็อก':<10} {'หน่วย':<10}")
    print("-"*120)
    
    for product in products:
        product_id = product[0]
        name_en = product[1]
        
        # ตรวจสอบว่ามี name_th หรือไม่
        if len(product) >= 6:
            # ข้อมูลแบบ bilingual (6 คอลัมน์)
            name_th = product[2] if product[2] else "-"
            price = product[3] if product[3] else 0
            stock = product[4] if product[4] else 0
            unit = product[5] if product[5] else "-"
        else:
            # ข้อมูลแบบไม่มี name_th (5 คอลัมน์)
            name_th = "-"
            price = product[2] if product[2] else 0
            stock = product[3] if product[3] else 0
            unit = product[4] if product[4] else "-"
        
        # แสดงผล
        print(f"{product_id:<5} {name_en:<35} {name_th:<35} {price:<10.2f} {stock:<10} {unit:<10}")
    
    print("-"*120)
    print(f"รวม {len(products)} รายการ")


def display_categories(categories):
    """แสดงหมวดหมู่"""
    if not categories:
        print("❌ ไม่พบหมวดหมู่")
        return
    
    print("\n" + "-"*60)
    print(f"{'ID':<5} {'ชื่อหมวดหมู่':<20} {'คำอธิบาย':<30}")
    print("-"*60)
    
    for cat in categories:
        cat_id = cat[0]
        name = cat[1]
        description = cat[2] if cat[2] else "-"
        print(f"{cat_id:<5} {name:<20} {description:<30}")
    
    print("-"*60)
    print(f"รวม {len(categories)} หมวดหมู่")


def main():
    """ฟังก์ชันหลัก"""
    while True:
        show_menu()
        choice = input("\nเลือกเมนู (0-6): ").strip()
        
        if choice == "1":
            # ดูสินค้าทั้งหมด - แก้ไข: ใช้ get_all_products_bilingual()
            print("\n📋 สินค้าทั้งหมด:")
            products = get_all_products_bilingual()  # ✅ แก้ไขจาก get_all_products()
            display_products(products)
        
        elif choice == "2":
            # ค้นหาสินค้า - แก้ไข: ใช้ search_product_bilingual()
            keyword = input("\n🔍 พิมพ์ชื่อสินค้าที่ต้องการค้นหา (ไทย/อังกฤษ): ").strip()
            if keyword:
                products = search_product_bilingual(keyword)  # ✅ แก้ไขจาก search_product_by_name()
                print(f"\n📋 ผลการค้นหา '{keyword}':")
                display_products(products)
            else:
                print("❌ กรุณาใส่คำค้นหา")
        
        elif choice == "3":
            # ดูสินค้าที่มีสต็อก - แก้ไข: เพิ่มภาษาไทย
            print("\n📦 สินค้าที่มีสต็อก:")
            # ใช้ query แบบ custom เพื่อดึงภาษาไทยด้วย
            conn = sqlite3.connect('shop.db')
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, name, name_th, retail_price, current_stock, unit
                FROM products
                WHERE current_stock > 0
                ORDER BY current_stock DESC
            ''')
            products = cursor.fetchall()
            conn.close()
            display_products(products)
        
        elif choice == "4":
            # ดูมูลค่าสต็อก
            print("\n💰 มูลค่าสต็อกทั้งหมด:")
            print("-"*50)
            values = get_total_stock_value()
            print(f"   💵 ต้นทุนรวม:    {values['total_cost']:>15,.2f} บาท")
            print(f"   💰 มูลค่าขายปลีก: {values['total_retail']:>15,.2f} บาท")
            print(f"   📈 กำไรคาดการณ์: {values['profit']:>15,.2f} บาท")
            
            # คำนวณ % กำไร
            if values['total_cost'] > 0:
                profit_margin = (values['profit'] / values['total_cost']) * 100
                print(f"   📊 อัตรากำไร:    {profit_margin:>15.1f} %")
            print("-"*50)
        
        elif choice == "5":
            # ดูหมวดหมู่
            print("\n📂 หมวดหมู่ทั้งหมด:")
            categories = get_all_categories()
            display_categories(categories)
        
        elif choice == "6":
            # ดูสินค้าตามหมวดหมู่
            # แสดงหมวดหมู่ก่อน
            categories = get_all_categories()
            print("\n📂 หมวดหมู่ที่มี:")
            for cat in categories:
                print(f"   {cat[0]}. {cat[1]}")
            
            cat_id = input("\n📂 ระบุเลขหมวดหมู่: ").strip()
            if cat_id.isdigit():
                # ดึงข้อมูลสินค้าพร้อมภาษาไทย
                conn = sqlite3.connect('shop.db')
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT p.id, p.name, p.name_th, p.retail_price, p.current_stock, p.unit
                    FROM products p
                    WHERE p.category_id = ?
                    ORDER BY p.name
                ''', (int(cat_id),))
                products = cursor.fetchall()
                conn.close()
                
                # หาชื่อหมวดหมู่
                category_name = next((cat[1] for cat in categories if cat[0] == int(cat_id)), "ไม่ทราบ")
                print(f"\n📋 สินค้าในหมวดหมู่ '{category_name}':")
                display_products(products)
            else:
                print("❌ กรุณาใส่ตัวเลข")
        
        elif choice == "0":
            # ออกจากโปรแกรม
            print("\n👋 ขอบคุณที่ใช้งาน!")
            print("   ลาก่อน! 😊")
            break
        
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่")
        
        # รอให้ผู้ใช้กด Enter
        input("\n📌 กด Enter เพื่อดำเนินการต่อ...")


if __name__ == "__main__":
    print("="*60)
    print("🏪 ยินดีต้อนรับสู่ระบบจัดการร้านค้า")
    print("   Shop Management System v2.0")
    print("="*60)
    
    # ตรวจสอบว่าฐานข้อมูลมีอยู่หรือไม่
    if not os.path.exists('shop.db'):
        print("❌ ไม่พบฐานข้อมูล shop.db")
        print("   กรุณาตรวจสอบว่าไฟล์อยู่ใน directory เดียวกัน")
        sys.exit(1)
    
    # เริ่มโปรแกรม
    main()
