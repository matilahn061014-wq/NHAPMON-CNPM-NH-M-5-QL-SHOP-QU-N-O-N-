import os

class Database:
    def __init__(self):
        # Đường dẫn tới các file dữ liệu (Nhóm nên để cùng thư mục với code)
        self.files = {
            'products': 'data.txt',      # Danh mục sản phẩm (Phần I)
            'vouchers': 'vouchers.txt',  # Quản lý voucher (Phần II)
            'customers': 'customers.txt',# Hồ sơ khách hàng (Phần III)
            'employees': 'nhanvien.txt', # Quản lý nhân sự (Phần IV)
            'history': 'lichsu.txt',     # Lịch sử giao dịch (Phần V)
            'returns': 'doitra.txt'      # Nhật ký đổi trả (Phần VI)
        }
        self._ensure_files_exist()

    def _ensure_files_exist(self):
        """Tự động tạo file nếu chưa có để tránh lỗi hệ thống"""
        for filename in self.files.values():
            if not os.path.exists(filename):
                with open(filename, 'w', encoding='utf-8') as f:
                    pass

    def load_data(self, key):
        """Đọc dữ liệu từ file và chuyển thành mảng 2 chiều"""
        data = []
        filename = self.files.get(key)
        if filename and os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    # Loại bỏ dòng trống hoặc dòng gạch ngang trang trí
                    clean_line = line.strip()
                    if clean_line and not clean_line.startswith('-'):
                        # Chia dữ liệu bằng dấu gạch đứng |
                        parts = [p.strip() for p in clean_line.split('|')]
                        data.append(parts)
        return data

    def save_data(self, key, data_list):
        """Ghi mảng 2 chiều ngược lại vào file theo định dạng chuẩn |"""
        filename = self.files.get(key)
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                for row in data_list:
                    # Chuyển các phần tử thành chuỗi và nối lại bằng dấu |
                    line = " | ".join(map(str, row))
                    f.write(line + "\n")