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


# us12

def hien_thi_danh_sach_don_hang(don_hang):
    if not don_hang:
        print("Không có đơn hàng nào.")
        return

    print("=== DANH SÁCH ĐƠN HÀNG ===")
    for don in don_hang:
        print("Mã đơn:", don["ma_don"])
        print("Tổng tiền:", don["tong_tien"])
        print("Ngày mua:", don["ngay"])
        print("------------------")

def tinh_tong_chi_tieu_luy_ke(don_hang):
    tong = 0
    for don in don_hang:
        tong += don["tong_tien"]

    print("Tổng chi tiêu lũy kế:", tong, "VND")
    return tong

def hien_thi_diem_tich_luy(tong_chi_tieu):
    # Quy ước: 10.000đ = 1 điểm
    diem = tong_chi_tieu // 10000
    print("Điểm tích lũy hiện tại:", diem, "điểm")

def tc1_hien_thi_don_hang(don_hang):
    if don_hang is None:
        return "❌ Không có dữ liệu đơn hàng"

    if len(don_hang) == 0:
        return "✅ Hiển thị: Khách hàng chưa có đơn hàng"

    return "✅ Hiển thị đầy đủ danh sách đơn hàng của khách hàng"

def tc2_tinh_tong_chi_tieu(don_hang, tong_hien_thi):
    tong_thuc_te = 0
    for don in don_hang:
        tong_thuc_te += don["tong_tien"]

    if tong_thuc_te == tong_hien_thi:
        return "✅ Tổng chi tiêu lũy kế hiển thị chính xác"
    else:
        return "❌ Tổng chi tiêu lũy kế hiển thị sai"

def tc3_hien_thi_diem_tich_luy(tong_chi_tieu, diem_hien_thi):
    # Quy ước: 10.000đ = 1 điểm
    diem_thuc_te = tong_chi_tieu // 10000

    if diem_thuc_te == diem_hien_thi:
        return "✅ Điểm tích lũy hiển thị chính xác"
    else:
        return "❌ Điểm tích lũy hiển thị không chính xác"