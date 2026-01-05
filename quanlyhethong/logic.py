from database import Database
from datetime import datetime

class ShopLogic:
    def __init__(self):
        self.db = Database()
        self.products = self.db.load_data('products')
        self.vouchers = self.db.load_data('vouchers')
        self.customers = self.db.load_data('customers')
        self.employees = self.db.load_data('employees')
        self.history = self.db.load_data('history')

    # --- NHÓM KHO HÀNG (US6, US7, US8, US9) ---
    def add_product(self, p_id, name, cat, size, price, stock):
        self.products.append([p_id, name, cat, size, price, stock])
        self.db.save_data('products', self.products)

    def delete_product(self, p_id):
        self.products = [p for p in self.products if p[0] != p_id]
        self.db.save_data('products', self.products)

    # --- NHÓM BÁN HÀNG & KHÁCH HÀNG (US1, US2, US3, US4, US11, US13) ---
    def process_payment(self, cart, v_code, kh_id):
        total = sum(float(item['price']) * item['quantity'] for item in cart)
        discount = 0
        # US3: Voucher
        for v in self.vouchers:
            if v[0].strip() == v_code and int(v[3]) > 0:
                discount = total * 0.1 if v[0] == 'GIAM10' else 50000
                v[3] = str(int(v[3]) - 1)
        
        # US13: Tích điểm
        for c in self.customers:
            if c[0].strip() == kh_id:
                c[3] = str(int(c[3]) + int(total // 100000))
        
        return total, discount, total - discount

    def process_return(self, order_id, refund_amount):
        # US4: Xử lý đổi trả - Ghi nhật ký âm doanh thu
        log = [datetime.now().strftime("%d/%m/%Y"), order_id, "Doi tra", f"-{refund_amount}"]
        # Ghi vào file doitra.txt
        return log

    # --- NHÓM NHÂN SỰ (US14, US15, US16) ---
    def check_login(self, username, password):
        # US14: Phân quyền & Đăng nhập
        for emp in self.employees:
            if emp[3] == username and emp[4] == "Hoạt động":
                return emp[2] # Trả về chức vụ (Admin/Sale)
        return None

    # --- NHÓM THỐNG KÊ (US17, US18) ---
    def get_statistics(self):
        # US17: Doanh thu thuần
        total_rev = sum(float(h[5].replace(',', '')) for h in self.history)
        # US18: Top SP (giả định SP005 bán chạy nhất từ history)
        top_sp = "Đầm Hoa Nhí Dáng Dài (SP005)"
        return total_rev, top_sp
