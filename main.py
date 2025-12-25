import os

# 1. Kết nối với các file chức năng trong folder
try:
    from khohang import chucnang as kho
    from banhang import tao_don_hang as ban
    # Thêm các file khác tương tự ở đây
except ImportError:
    pass

def xem_data():
    """Hàm này thực hiện đúng ý thầy: Truy xuất trực tiếp data.txt"""
    print("\n--- [DỮ LIỆU TẬP TRUNG TRÊN DATA.TXT] ---")
    if os.path.exists("data.txt"):
        with open("data.txt", "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Cảnh báo: File data.txt không tồn tại!")

def hien_thi_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*60)
        print("     HỆ THỐNG QUẢN LÝ SHOP QUẦN ÁO NỮ - NHÓM 5")
        print("          (TRẠM ĐIỀU KHIỂN CHÍNH - MAIN)")
        print("="*60)
        print("1. [KHO HÀNG]   - Xem danh sách & Quản lý Sản phẩm")
        print("2. [BÁN HÀNG]   - Tạo đơn hàng & Thanh toán")
        print("3. [DỮ LIỆU]    - Truy xuất toàn bộ file data.txt")
        print("0. THOÁT CHƯƠNG TRÌNH")
        print("="*60)
        
        lua_chon = input("Mời bạn chọn chức năng (0-3): ")
        
        if lua_chon == '1':
            print("\n--- ĐANG TRUY XUẤT DỮ LIỆU KHO ---")
            # Ở đây sẽ gọi hàm hiển thị từ file chucnang.py
            # Ví dụ: kho.hien_thi_san_pham()
        elif lua_chon == '2':
            print("\n--- ĐANG MỞ GIAO DIỆN BÁN HÀNG ---")
        elif lua_chon == '3':
            xem_data()
        elif lua_chon == '0':
            print("Đang đóng hệ thống... Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    hien_thi_menu()
