# us7
def hien_thi_san_pham(sp):
    print("=== Thông tin sản phẩm hiện tại ===")
    print("Tên:", sp["ten"])
    print("Giá:", sp["gia"])
    print("Mô tả:", sp["mo_ta"])

def nhap_du_lieu_moi():
    ten = input("Nhập tên mới: ")
    gia = input("Nhập giá mới: ")
    mo_ta = input("Nhập mô tả mới: ")

    if ten == "" or gia == "":
        return None, "Tên và giá không được để trống"

    try:
        gia = float(gia)
        if gia <= 0:
            return None, "Giá phải lớn hơn 0"
    except:
        return None, "Giá phải là số"

    return {"ten": ten, "gia": gia, "mo_ta": mo_ta}, None

def luu_san_pham(sp, du_lieu_moi):
    sp["ten"] = du_lieu_moi["ten"]
    sp["gia"] = du_lieu_moi["gia"]
    sp["mo_ta"] = du_lieu_moi["mo_ta"]

def thong_bao(thong_diep):
    print("👉", thong_diep)

def tieu_chi_chap_nhan(sp_cu, sp_moi, huy_sua=False):
    # 1. Hệ thống hiển thị đúng thông tin sản phẩm cần sửa
    if sp_cu is None:
        return "❌ Không hiển thị được sản phẩm cần sửa"

    # 4. Người dùng có thể hủy sửa mà không thay đổi dữ liệu
    if huy_sua:
        if sp_cu == sp_moi:
            return "✅ Hủy sửa thành công, dữ liệu không thay đổi"
        else:
            return "❌ Hủy sửa nhưng dữ liệu đã bị thay đổi"

    # 3. Dữ liệu không hợp lệ được cảnh báo lỗi
    if sp_moi["ten"] == "" or sp_moi["gia"] <= 0:
        return "❌ Dữ liệu không hợp lệ, hiển thị cảnh báo lỗi"