class QuanLySanPham:
    def __init__(self):
        self.danh_sach_san_pham = []

    def them_san_pham(self, ten, danh_muc, gia, so_luong, mo_ta=""):
        # 1. Kiểm tra dữ liệu
        loi = []
        if not ten or not ten.strip(): loi.append("Tên sản phẩm không được để trống")
        if not danh_muc or not danh_muc.strip(): loi.append("Danh mục không được để trống")
        if not isinstance(gia, (int, float)) or gia < 0: loi.append("Giá bán không hợp lệ")
        if not isinstance(so_luong, int) or so_luong < 0: loi.append("Số lượng không hợp lệ")

        if loi:
            return {"trang_thai": "loi", "chi_tiet": loi}

        # 2. Lưu sản phẩm
        san_pham_moi = {
            "id": len(self.danh_sach_san_pham) + 1,
            "ten": ten.strip(),
            "danh_muc": danh_muc.strip(),
            "gia": gia,
            "so_luong": so_luong,
            "mo_ta": mo_ta
        }
        self.danh_sach_san_pham.append(san_pham_moi)

        # 3. Thông báo kết quả
        return {"trang_thai": "thanh_cong", "du_lieu": san_pham_moi}
