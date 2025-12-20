#us18
from datetime import datetime
from collections import defaultdict

sales_data = [
    {
        "product_id": "SP01",
        "product_name": "Áo thun",
        "color": "Đen",
        "size": "M",
        "quantity": 3,
        "date": "12/01/2025",
    },
    {
        "product_id": "SP02",
        "product_name": "Quần jean",
        "color": "Đen",
        "size": "M",
        "quantity": 5,
        "date": "01/01/2025",
    },
    {
        "product_id": "SP03",
        "product_name": "Giày thể thao",
        "color": "white",
        "size": "40",
        "quantity": 7,
        "date": "04/04/2004"
    },
]

def parse_date(date_str: str):
    return datetime.strptime(date_str, "%d/%m/%Y")

def top_selling_products(data, top_n=10, start_date=None, end_date=None, color=None, size=None):
    if start_date:
        start_date = parse_date(start_date)
    if end_date:
        end_date = parse_date(end_date)

    summary = defaultdict(int)

    for row in data:
        sales_date = parse_date(row["date"])

        if start_date and sales_date < start_date:
            continue
        if end_date and sales_date > end_date:
            continue
        if color and row["color"] != color:
            continue
        if size and row["size"] != size:
            continue

        key = (
            row["product_id"],
            row["product_name"],
            row["color"],
            row["size"],
        )
        summary[key] += row["quantity"]

    result = sorted(summary.items(), key=lambda x: x[1], reverse=True)
    return result[:top_n]

if __name__ == "__main__":
    report = top_selling_products(
        sales_data,
        start_date="01/01/2025",
        end_date="31/12/2025"
    )

    for idx, (info, total_qty) in enumerate(report, 1):
        pid, name, color, size = info
        print(f"{idx}. {name} | {pid} | {color} | {size} | {total_qty}")

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

