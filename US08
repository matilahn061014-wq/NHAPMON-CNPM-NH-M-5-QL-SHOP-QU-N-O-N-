products = [
    {"id": 101, "name": "Váy hoa nhí", "price": 250000},
    {"id": 102, "name": "Áo sơ mi lụa", "price": 180000},
    {"id": 103, "name": "Quần jean ống rộng", "price": 320000}
]

def delete_product_process(product_id, user_role):
    if user_role != "Admin":
        return "❌ THẤT BẠI: Bạn không có quyền xóa."

    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if product is None:
        return "❌ THẤT BẠI: Không tìm thấy sản phẩm."

    confirmation = input("Xác nhận xóa (y/n): ")
    if confirmation.lower() != "y":
        return "⚠️ Thao tác xóa đã bị hủy."

    products.remove(product)
    return f"✅ Đã xóa sản phẩm {product['name']}."

current_role = "Admin"

for p in products:
    print(p)

result = delete_product_process(102, current_role)
print(result)

for p in products:
    print(p)
