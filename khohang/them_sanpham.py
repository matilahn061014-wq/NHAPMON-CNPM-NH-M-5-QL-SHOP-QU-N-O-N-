import os

class ProductAdmin:
    def __init__(self, data_file):
        self.data_file = data_file

    def execute_add_product(self):
        print("--- NHẬP THÔNG TIN SẢN PHẨM MỚI ---")
        p_id = input("Mã sản phẩm: ")
        name = input("Tên sản phẩm: ")
        category = input("Loại hàng: ")
        size = input("Kích cỡ: ")
        price = input("Giá bán: ")
        stock = input("Số lượng nhập kho: ")

        if not all([p_id, name, category, size, price, stock]):
            print("❌ Lỗi: Dữ liệu nhập không đầy đủ!")
            return

        try:
            line = f"{p_id}|{name}|{category}|{size}|{float(price)}|{int(stock)}\n"
            with open(self.data_file, 'a', encoding='utf-8') as f:
                f.write(line)
            print(f"✅ Đã lưu sản phẩm '{name}' vào hệ thống thành công.")
        except ValueError:
            print("❌ Lỗi: Giá hoặc số lượng không hợp lệ!")

    def list_products(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                for line in f:
                    print(line.strip())

if _name_ == "_main_":
    admin = ProductAdmin('data.txt')
    admin.execute_add_product()
    admin.list_products()
