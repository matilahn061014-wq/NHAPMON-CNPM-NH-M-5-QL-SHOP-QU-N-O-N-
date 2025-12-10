# NHAPMON-CNPM-NH-M-5-QL-SHOP-QU-N-O-N-
US4.1.Quan ly doi/tra hang
fORDERS_DB = [
    {
        "order_id": "DH2025001",
        "customer_id": "KH001",
        "order_date": "2025-11-20",
        "status": "Completed",
        "items": [
            {"sku": "SP001", "name": "Áo thun Cotton", "quantity": 2, "unit_price": 200000},
            {"sku": "SP002", "name": "Quần Jeans Slimfit", "quantity": 1, "unit_price": 500000}
        ],
        "total_amount": 900000
    },
    {
        "order_id": "DH2025002",
        "customer_id": "KH002",
        "order_date": "2025-11-25",
        "status": "Completed",
        "items": [
            {"sku": "SP003", "name": "Giày chạy bộ", "quantity": 1, "unit_price": 1200000}
        ],
        "total_amount": 1200000
    }
]

def search_order(order_id):
    """
    Tìm kiếm đơn hàng theo ID.
    Input: order_id (string)
    Output: Dictionary đơn hàng hoặc None
    """
    for order in ORDERS_DB:
        if order["order_id"] == order_id:
            return order
    return None
US4.2.Them/sua/xoa san pham
INVENTORY_DB = {
    "SP001": 50,  # Áo thun
    "SP002": 15,  # Quần Jeans
    "SP003": 30   # Giày chạy bộ
}

def replenish_inventory(return_items):
    """
    Cộng tồn kho cho các sản phẩm được trả lại.
    Input: return_items (list of dicts) - [{"sku": "SPxxx", "quantity": N}]
    Output: True nếu thành công
    """
    print("\n--- BƯỚC 2: CẬP NHẬT TỒN KHO ---")
    for item in return_items:
        sku = item["sku"]
        quantity = item["quantity"]
        
        current_stock = INVENTORY_DB.get(sku, 0) # Lấy tồn kho hiện tại, nếu không có mặc định là 0
        INVENTORY_DB[sku] = current_stock + quantity
        
        print(f"Hoàn nhập: {sku} | Số lượng: {quantity}. Tồn mới: {INVENTORY_DB[sku]}")

    return True
US4.3.Tao phieu nhap hang
    CURRENT_PRICES = {
    "SP001": 200000,
    "SP002": 500000,
    "SP004": 650000, # Sản phẩm đổi mới: Váy đầm
    "SP005": 1000000 # Sản phẩm đổi mới: Đồng hồ
}

def calculate_price_difference(items_returned, items_exchanged):
    """
    Tính toán chênh lệch giá trị.
    Chênh lệch = Tổng giá trị đổi mới - Tổng giá trị hàng trả.
    Input: 
        items_returned (list) - Sản phẩm trả, giá trị tính theo giá **lúc mua** (hoặc giá trị hoàn lại)
        items_exchanged (list) - Sản phẩm đổi, giá trị tính theo giá **hiện tại**
    Output: difference (float)
    """
    print("\n--- BƯỚC 3: TÍNH CHÊNH LỆCH GIÁ ---")
    
    total_returned_value = sum(item["unit_price"] * item["quantity"] for item in items_returned)
    
    total_exchange_value = 0
    for item in items_exchanged:
        sku = item["sku"]
        quantity = item["quantity"]
        price = CURRENT_PRICES.get(sku, 0)
        total_exchange_value += price * quantity
    
    difference = total_exchange_value - total_returned_value
    
    print(f"Tổng giá trị hàng trả: {total_returned_value:,.0f} VND")
    print(f"Tổng giá trị hàng đổi: {total_exchange_value:,.0f} VND")
    print(f"Chênh lệch: {difference:,.0f} VND")
    
    return difference



