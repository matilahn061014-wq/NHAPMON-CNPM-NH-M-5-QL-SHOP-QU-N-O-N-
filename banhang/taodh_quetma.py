import os

class ClothingShopSystem:
    def __init__(self, data_file):
        self.data_file = data_file
        self.inventory = []
        self.cart = {}
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.data_file):
            return
        
        with open(self.data_file, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 6:
                    self.inventory.append({
                        'id': parts[0],
                        'name': parts[1],
                        'category': parts[2],
                        'size': parts[3],
                        'price': float(parts[4]),
                        'stock': int(parts[5])
                    })

    def process_input(self, search_term):
        product = next((p for p in self.inventory 
                        if p['id'] == search_term or search_term.lower() in p['name'].lower()), None)
        
        if not product:
            print(f"⚠️ Không tìm thấy: '{search_term}'")
            return

        if product['stock'] <= 0:
            print(f"❌ '{product['name']}' - HẾT HÀNG!")
            return

        p_id = product['id']
        if p_id in self.cart:
            self.cart[p_id]['quantity'] += 1
        else:
            self.cart[p_id] = {
                'name': product['name'],
                'size': product['size'],
                'price': product['price'],
                'quantity': 1
            }
        
        product['stock'] -= 1
        print(f"✅ Đã thêm: {product['name']} ({product['size']})")

    def show_order(self):
        print("\n" + "="*30)
        print("DANH SÁCH GIỎ HÀNG")
        print("-" * 30)
        total = 0
        for p_id, item in self.cart.items():
            subtotal = item['price'] * item['quantity']
            total += subtotal
            print(f"{item['name']} x{item['quantity']}: {subtotal:,.0f} VND")
        print("-" * 30)
        print(f"TỔNG: {total:,.0f} VND")
        print("="*30 + "\n")

if __name__ == "__main__":
    shop = ClothingShopSystem('data.txt')
    
    shop.process_input("SP001")
    shop.process_input("SP001")
    shop.process_input("Váy")
    
    shop.show_order()