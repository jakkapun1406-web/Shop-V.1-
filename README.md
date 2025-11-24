# 🏪 ระบบจัดการร้านค้า (Shop Management System)

REST API สำหรับจัดการร้านค้า พัฒนาด้วย Python, FastAPI และ SQLite

---

## 🎯 Features

- ✅ จัดการสินค้า (ดู/เพิ่ม/แก้ไข/ลบ)
- ✅ จัดการสต็อกสินค้า
- ✅ จัดการหมวดหมู่
- ✅ รองรับภาษาไทย-อังกฤษ
- ✅ API Documentation อัตโนมัติ (Swagger UI)
- ✅ คำนวณมูลค่าสต็อก

---

## 🛠️ เทคโนโลยีที่ใช้

- **Backend:** Python 3.11+
- **Framework:** FastAPI
- **Database:** SQLite
- **Server:** Uvicorn

---

## 📊 Database Schema

### ตารางหลัก:
- `products` - สินค้า (25+ รายการ)
- `categories` - หมวดหมู่ (6 หมวด)
- `stock_batches` - การจัดการสต็อก
- `suppliers` - ซัพพลายเออร์
- `users` - ผู้ใช้งาน
- `transactions` - บันทึกการทำงาน

---

## 🚀 การติดตั้ง

### 1. Clone โปรเจกต์
```bash
cd shopProject
```

### 2. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

หรือ
```bash
pip install fastapi uvicorn
```

### 3. รัน API Server
```bash
python -m uvicorn api_simple:app --reload
```

---

## 📡 API Endpoints

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints หลัก

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | หน้าแรก |
| GET | `/test` | ทดสอบ API |
| GET | `/products` | ดูสินค้าทั้งหมด |
| GET | `/products/{id}` | ดูสินค้า 1 รายการ |
| GET | `/docs` | API Documentation (Swagger UI) |

---

## 📖 การใช้งาน

### 1. เปิด API Server
```bash
python -m uvicorn api_simple:app --reload
```

### 2. เปิด Swagger UI
```
http://127.0.0.1:8000/docs
```

### 3. ทดสอบ API
1. คลิกที่ Endpoint ที่ต้องการ
2. คลิก "Try it out"
3. คลิก "Execute"
4. ดูผลลัพธ์

---

## 📸 ตัวอย่าง Response

### GET /products
```json
{
  "success": true,
  "total": 10,
  "products": [
    {
      "id": 1,
      "name": "Drinking Water 600ml",
      "price": 7.0
    },
    {
      "id": 2,
      "name": "Fresh Milk 200ml",
      "price": 15.0
    }
  ]
}
```

### GET /
```json
{
  "message": "✅ API ทำงานปกติ",
  "status": "online"
}
```

---

## 📂 โครงสร้างโปรเจกต์
```
shopProject/
├── shop.db              # SQLite Database
├── db_functions.py      # ฟังก์ชันจัดการ Database
├── api_simple.py        # API หลัก
├── README.md           # เอกสารนี้
├── .gitignore          # ไฟล์ที่ไม่ต้อง track
└── requirements.txt    # Dependencies
```

---

## 🔧 Development

### ติดตั้ง Development Dependencies
```bash
pip install pytest pytest-cov black flake8
```

### รัน Tests
```bash
pytest
```

### Code Formatting
```bash
black .
```

### Linting
```bash
flake8
```

---

## 📝 TODO

- [ ] เพิ่ม POST/PUT/DELETE Endpoints
- [ ] เพิ่ม Authentication (JWT)
- [ ] เพิ่ม Pagination
- [ ] สร้าง Dashboard ด้วย Streamlit
- [ ] Deploy ขึ้น Cloud (Railway/Render)
- [ ] เพิ่ม Unit Tests
- [ ] เพิ่ม Docker Support
- [ ] เพิ่ม CI/CD Pipeline

---

## 🌟 Features ที่วางแผนเพิ่ม

- 🔐 Authentication & Authorization
- 📊 Dashboard สำหรับ Analytics
- 📱 Mobile API
- 🔔 Notification System
- 📧 Email Integration
- 💳 Payment Integration

---

## 👤 ผู้พัฒนา

**Your Name**
- GitHub: [Jakkapun Srisaga](https://github.com/jakkapun1406-web)
- Email: jakkapun1406@gmail.com
- LinkedIn: [Your LinkedIn]-

---

## 📄 License

MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🙏 Credits

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [SQLite](https://www.sqlite.org/) - Database
- [DB Browser for SQLite](https://sqlitebrowser.org/) - Database management
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

---

## 📅 Version History

### v1.0.0 (2025-11-24)
- ✅ สร้าง Database schema
- ✅ เพิ่มสินค้า 25+ รายการ
- ✅ สร้าง REST API ด้วย FastAPI
- ✅ รองรับภาษาไทย-อังกฤษ
- ✅ เพิ่ม Swagger UI Documentation
- ✅ CRUD Operations สำหรับสินค้า

---

## 🚀 การ Deploy

### Deploy บน Railway (แนะนำ - ฟรี)

1. สร้าง account ที่ [Railway](https://railway.app)
2. เชื่อม GitHub Repository
3. Deploy อัตโนมัติ

### Deploy บน Render (ฟรี)

1. สร้าง account ที่ [Render](https://render.com)
2. เชื่อม GitHub Repository
3. เลือก "Web Service"
4. ตั้งค่า:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn api_simple:app --host 0.0.0.0 --port $PORT`

---

## 🐛 พบ Bug?

หากพบปัญหาหรือต้องการเสนอแนะ:
- เปิด Issue: [GitHub Issues](https://github.com/yourusername/shopProject/issues)
- Email:jakkapun1406@gmail.com

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 ติดต่อ

Project Link: [https://github.com/jakkapun1406-web/Shop-V.1-.git]

---

## ⭐ ถ้าชอบโปรเจกต์นี้

ช่วยกด ⭐ Star ให้โปรเจกต์นี้ได้ที่ [GitHub](https://github.com/jakkapun1406-web/Shop-V.1-.git)

---

**Made with ❤️ by [Your Name]**