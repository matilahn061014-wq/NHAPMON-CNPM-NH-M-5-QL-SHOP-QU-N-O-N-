# ==============================
# ĐỒ ÁN: QUẢN LÝ TỒN KHO
# ==============================

inventory = {}
history = []

# --------- NHẬP KHO ----------
def import_product():
    name = input("Tên sản phẩm: ")
    color = input("Màu sắc: ")
    size = input("Kích cỡ: ")
    quantity = int(input("Số lượng nhập: "))

    key = (name, color, size)
    inventory[key] = inventory.get(key, 0) + quantity
    history.append(f"Nhập | {name} | {color} | {size} | +{quantity}")

    print("✅ Nhập kho thành công")

# --------- XUẤT KHO ----------
def export_product():
    name = input("Tên sản phẩm: ")
    color = input("Màu sắc: ")
    size = input("Kích cỡ: ")
    quantity = int(input("Số lượng xuất: "))

    key = (name, color, size)

    if key not in inventory:
        print("❌ Sản phẩm không tồn tại")
    elif inventory[key] < quantity:
        print("❌ Không đủ hàng trong kho")
    else:
        inventory[key] -= quantity
        history.append(f"Xuất | {name} | {color} | {size} | -{quantity}")
        print("✅ Xuất kho thành công")

# ------ ĐIỀU CHỈNH TỒN KHO ------
def adjust_inventory():
    name = input("Tên sản phẩm: ")
    color = input("Màu sắc: ")
    size = input("Kích cỡ: ")
    new_quantity = int(input("Số lượng mới: "))

    key = (name, color, size)
    inventory[key] = new_quantity
    history.append(f"Điều chỉnh | {name} | {color} | {size} | = {new_quantity}")

    print("✅ Điều chỉnh thành công")

# -------- XEM TỒN KHO --------
def view_inventory():
    print("\n===== TỒN KHO HIỆN TẠI =====")
    if not inventory:
        print("Kho trống")
        return

    for (name, color, size), qty in inventory.items():
        print(f"Sản phẩm: {name} | Màu: {color} | Size: {size} | SL: {qty}")

# -------- XEM LỊCH SỬ --------
def view_history():
    print("\n===== LỊCH SỬ XUẤT / NHẬP =====")
    if not history:
        print("Chưa có lịch sử")
        return

    for item in history[-10:]:
        print(item)

# ------------ MENU ------------
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Nhập kho")
        print("2. Xuất kho")
        print("3. Điều chỉnh tồn kho")
        print("4. Xem tồn kho")
        print("5. Xem lịch sử")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            import_product()
        elif choice == "2":
            export_product()
        elif choice == "3":
            adjust_inventory()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            view_history()
        elif choice == "0":
            print("👋 Kết thúc chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

menu()
