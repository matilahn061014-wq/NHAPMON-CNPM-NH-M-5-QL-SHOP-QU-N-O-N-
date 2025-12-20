PAYMENT_METHODS = [
    "TIEN_MAT",
    "CHUYEN_KHOAN",
    "ATM",
    "THE_THANH_VIEN"
]

def check_payment_method(method):
    if method not in PAYMENT_METHODS:
        raise Exception("Phương thức thanh toán không hợp lệ")

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


def deduct_inventory(order_items):
    for product, quantity in order_items.items():
        if product.stock < quantity:
            raise Exception(f"{product.name} không đủ tồn kho")
        product.stock -= quantity

def print_bill(order_items, payment_method):
    print("===== HÓA ĐƠN =====")
    for product, quantity in order_items.items():
        print(f"{product.name} x {quantity}")
    print(f"Hình thức thanh toán: {payment_method}")
    print("Trạng thái: Giao dịch thành công")

transaction_book = []

def save_transaction(order_items, payment_method):
    transaction_book.append({
        "items": [(p.name, q) for p, q in order_items.items()],
        "payment_method": payment_method
    })

ALLOWED_PAYMENTS = ["TIEN_MAT", "CHUYEN_KHOAN"]

def validate_payment(method):
    if method not in ALLOWED_PAYMENTS:
        raise Exception("Chỉ hỗ trợ Tiền mặt hoặc Chuyển khoản")

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


def reduce_stock(order_items):
    for product, quantity in order_items.items():
        if product.stock < quantity:
            raise Exception(f"{product.name} không đủ tồn kho")
        product.stock -= quantity

def is_transaction_success(is_paid, is_stock_reduced):
    return is_paid and is_stock_reduced

def print_bill(order_items, payment_method):
    print("===== HÓA ĐƠN =====")
    for product, quantity in order_items.items():
        print(f"{product.name} x {quantity}")
    print(f"Thanh toán: {payment_method}")
    print("Trạng thái: Thành công")
