import os

class ProductManager:
    def __init__(self, data_file):
        self.data_file = data_file

    def add_new_product(self, product_id, name, category, size, price, stock):
        if not all([product_id, name, category, size, price, stock]):
            print("❌ Lỗi: Vui lòng nhập đầy đủ thông tin sản phẩm!")
            return False

        try:
            price_val = float(price)
            stock_val = int(stock)
        except ValueError:
            print("❌ Lỗi: Giá và số lượng phải là số hợp lệ!")
            return False

        new_line = f"{product_id}|{name}|{category}|{size}|{price_val}|{stock_val}\n"

        try:
            with open(self.data_file, 'a', encoding='utf-8') as f:
                f.write(new_line)
            
            print(f"✅ Thêm sản phẩm '{name}' thành công.")
            return True
        except Exception as e:
            print(f"❌ Lỗi khi lưu: {e}")
            return False

    def show_all_products(self):
        if not os.path.exists(self.data_file):
            print("Hệ thống chưa có dữ liệu.")
            return

        print("\n--- DANH SÁCH SẢN PHẨM ---")
        with open(self.data_file, 'r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())

if __name__ == "__main__":
    manager = ProductManager('data.txt')

    manager.add_new_product(
        product_id="SP003",
        name="Chân váy chữ A",
        category="Váy",
        size="S",
        price="280000",
        stock="20"
    )

    manager.show_all_products()