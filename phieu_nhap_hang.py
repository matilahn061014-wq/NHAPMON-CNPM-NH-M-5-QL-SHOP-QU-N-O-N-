# ===============================
# QUẢN LÝ PHIẾU NHẬP HÀNG
# ===============================

# Tồn kho: key = (ten_sp, mau, size), value = so_luong
ton_kho = {}

def tao_phieu_nhap():
    print("=== TẠO PHIẾU NHẬP HÀNG ===")
    ngay_nhap = input("Nhập ngày nhập (dd/mm/yyyy): ")
    nha_cung_cap = input("Nhập nhà cung cấp: ")

    phieu_nhap = {
        "ngay_nhap": ngay_nhap,
        "nha_cung_cap": nha_cung_cap,
        "chi_tiet": []
    }

    while True:
        print("\n--- Thêm sản phẩm ---")
        ten_sp = input("Tên sản phẩm: ")
        mau = input("Màu: ")
        size = input("Size: ")
        so_luong = int(input("Số lượng: "))
        gia_nhap = float(input("Giá nhập: "))

        chi_tiet_sp = {
            "ten_sp": ten_sp,
            "mau": mau,
            "size": size,
            "so_luong": so_luong,
            "gia_nhap": gia_nhap
        }

        phieu_nhap["chi_tiet"].append(chi_tiet_sp)

        tiep_tuc = input("Thêm sản phẩm khác? (y/n): ")
        if tiep_tuc.lower() != "y":
            break

    cap_nhat_ton_kho(phieu_nhap)
    print("\n✅ Tạo phiếu nhập thành công!")
    return phieu_nhap


def cap_nhat_ton_kho(phieu_nhap):
    for sp in phieu_nhap["chi_tiet"]:
        key = (sp["ten_sp"], sp["mau"], sp["size"])
        if key in ton_kho:
            ton_kho[key] += sp["so_luong"]
        else:
            ton_kho[key] = sp["so_luong"]


def hien_thi_ton_kho():
    print("\n=== TỒN KHO HIỆN TẠI ===")
    for key, so_luong in ton_kho.items():
        ten_sp, mau, size = key
        print(f"{ten_sp} | Màu: {mau} | Size: {size} | SL: {so_luong}")


# ===============================
# CHƯƠNG TRÌNH CHÍNH
# ===============================
phieu = tao_phieu_nhap()
hien_thi_ton_kho()
