# product_cart.py
class Product:
    def __init__(self, code, name, stock, price):
        self.code = code
        self.name = name
        self.stock = stock
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, qty=1):
        if product.stock <= 0:
            print(f"[!] Sản phẩm '{product.name}' đã hết hàng!")
            return False

        if product.code in self.items:
            if product.stock < self.items[product.code] + qty:
                print(f"[!] Không đủ tồn kho cho '{product.name}'!")
                return False
            self.items[product.code] += qty
        else:
            self.items[product.code] = qty

        print(f"[+] Đã thêm '{product.name}' (SL: {self.items[product.code]})")
        return True
