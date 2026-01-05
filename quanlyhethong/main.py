from logic import ShopLogic
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    logic = ShopLogic()
    
    while True:
        clear_screen()
        print("==============================================")
        print(" HỆ THỐNG QUẢN LÝ SHOP QUẦN ÁO NỮ - NHÓM 5 ")
        print("==============================================")
        print("1. Đăng nhập hệ thống (US14)")
        print("0. Thoát chương trình")
        
        choice = input("\nMời chọn: ")
        
        if choice == '1':
            user = input("Tài khoản: ")
            role = logic.check_login(user, "") # US14: Kiểm tra quyền
            
            if not role:
                print("❌ Tài khoản không tồn tại hoặc bị khóa!")
                input("Nhấn Enter để tiếp tục...")
                continue
            
            if role == "Chủ shop" or role == "Admin":
                admin_menu(logic)
            else:
                staff_menu(logic)
        elif choice == '0':
            break

def staff_menu(logic):
    cart = []
    while True:
        clear_screen()
        print(f"--- MENU NHÂN VIÊN BÁN HÀNG ---")
        print("1. Tạo đơn hàng & Quét mã (US1, US2)")
        print("2. Áp dụng Voucher & Tích điểm (US3, US13)")
        print("3. Xử lý Đổi/Trả hàng (US4)")
        print("4. Xem tồn kho nhanh (US10)")
        print("0. Đăng xuất")
        
        cmd = input("\nChọn chức năng: ")
        
        if cmd == '1':
            while True:
                term = input("Nhập mã SP (hoặc 'q' để xong): ")
                if term == 'q': break
                p = logic.find_product(term)
                if p:
                    cart.append({'id': p[0], 'name': p[1], 'price': p[4].replace(',', ''), 'quantity': 1})
                    print(f"✅ Đã thêm: {p[1]}")
                else: print("❌ Không tìm thấy sản phẩm!")
        
        elif cmd == '2':
            if not cart:
                print("⚠️ Giỏ hàng đang trống!"); input(); continue
            v_code = input("Nhập mã Voucher: ")
            kh_id = input("Nhập mã Khách hàng: ")
            total, dis, final = logic.process_payment(cart, v_code, kh_id)
            print(f"Tổng: {total:,.0f} | Giảm: {dis:,.0f} | Cần thu: {final:,.0f}")
            if input("Xác nhận thanh toán? (y/n): ") == 'y':
                logic.update_stock(cart)
                print("🎉 Thanh toán thành công & Đã tích điểm!"); cart = []
            input("Nhấn Enter để quay lại...")

        elif cmd == '3': # US4
            order_id = input("Nhập mã đơn hàng cần đổi trả: ")
            amount = float(input("Số tiền hoàn trả: "))
            log = logic.process_return(order_id, amount)
            print(f"✅ Đã ghi nhận: {log}")
            input()

        elif cmd == '0': break

def admin_menu(logic):
    while True:
        clear_screen()
        print("--- MENU QUẢN TRỊ VIÊN (ADMIN) ---")
        print("1. Quản lý kho (Thêm/Sửa/Xóa SP) (US6,7,8)")
        print("2. Xem báo cáo doanh thu thuần (US17)")
        print("3. Xem Top sản phẩm bán chạy (US18)")
        print("4. Quản lý nhân sự & Lương (US14,16)")
        print("0. Đăng xuất")
        
        cmd = input("\nChọn chức năng: ")
        
        if cmd == '1': # US6, 7, 8
            print("1. Thêm SP | 2. Xóa SP")
            sub_cmd = input("Chọn: ")
            if sub_cmd == '1':
                p_id = input("Mã SP: "); name = input("Tên: ")
                logic.add_product(p_id, name, "Áo", "S", "200000", "50")
                print("✅ Đã thêm sản phẩm thành công.")
            elif sub_cmd == '2':
                p_id = input("Nhập mã SP cần xóa: ")
                logic.delete_product(p_id)
                print("✅ Đã xóa.")
            input()

        elif cmd == '2' or cmd == '3': # US17, 18
            rev, top = logic.get_statistics()
            print(f"📊 Doanh thu thuần: {rev:,.0f} VND")
            print(f"🏆 Sản phẩm hot: {top}")
            input("Nhấn Enter để quay lại...")

        elif cmd == '0': break

if __name__ == "__main__":
    main()

