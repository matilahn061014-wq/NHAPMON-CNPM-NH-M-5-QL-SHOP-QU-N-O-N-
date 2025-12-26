import os

class ProductEditor:
    def __init__(self, data_file):
        self.data_file = data_file

    def edit_product(self):
        if not os.path.exists(self.data_file):
            print("❌ File dữ liệu không tồn tại!")
            return

        target_id = input("Nhập Mã sản phẩm cần sửa: ")
        products = []
        found = False
        
        with open(self.data_file, 'r', encoding='utf-8') as f:
            products = [line.strip().split('|') for line in f if line.strip()]

        for i, p in enumerate(products):
            if p[0] == target_id:
                found = True
                print(f"\n--- THÔNG TIN HIỆN TẠI (AC1) ---")
                print(f"1. Tên: {p[1]} | 2. Loại: {p[2]} | 3. Size: {p[3]} | 4. Giá: {p[4]} | 5. Tồn: {p[5]}")
                
                choice = input("\nBạn muốn sửa sản phẩm này không? (y/n): ")
                if choice.lower() != 'y':
                    print("➡️ Đã hủy sửa (AC4). Dữ liệu giữ nguyên.")
                    return

                print("\nNhập thông tin mới (để trống nếu không muốn thay đổi):")
                new_name = input(f"Tên mới [{p[1]}]: ") or p[1]
                new_cat = input(f"Loại mới [{p[2]}]: ") or p[2]
                new_size = input(f"Size mới [{p[3]}]: ") or p[3]
                new_price = input(f"Giá mới [{p[4]}]: ") or p[4]
                new_stock = input(f"Tồn kho mới [{p[5]}]: ") or p[5]

                try:
                    # Kiểm tra dữ liệu hợp lệ (AC2, AC3)
                    float(new_price)
                    int(new_stock)
                    products[i] = [p[0], new_name, new_cat, new_size, new_price, new_stock]
                    print("✅ Dữ liệu hợp lệ.")
                except ValueError:
                    print("❌ Lỗi: Giá hoặc số lượng không hợp lệ! (AC3)")
                    return
                break

        if not found:
            print(f"❌ Không tìm thấy sản phẩm mã {target_id}")
            return

        # Lưu lại toàn bộ danh sách vào file (Task 3)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            for p in products:
                f.write("|".join(p) + "\n")
        print("🎉 Đã lưu thông tin cập nhật thành công! (AC2)")

if _name_ == "_main_":
    editor = ProductEditor('data.txt')
    editor.edit_product()