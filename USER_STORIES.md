# 📋 DANH SÁCH USER STORIES - QUẢN LÝ SHOP QUẦN ÁO NỮ (NHÓM 5)

## 👥 Thành viên nhóm & Phân công
* **Nguyễn Hoàng Nhi (Nhóm trưởng):** US1, US6, US8, US16.
* **Nguyễn Phương Anh:** US4, US9, US10, US11.
* **Nguyễn Quỳnh Hương:** US4, US7, US12, US18.
* **Nguyễn Thị Thuý Lê:** US13, US14, US17.
* **Trần Đình Khánh Uyên:** US2, US3, US5, US15.

---

## I. QUẢN LÝ BÁN HÀNG
### US01: Tạo đơn hàng & Quét mã
* **Mô tả:** Nhân viên tạo đơn hàng mới nhanh chóng bằng cách quét mã vạch hoặc tìm kiếm sản phẩm.
* **Tiêu chí chấp nhận (AC):** Quét mã thành công sản phẩm tự động vào giỏ; Cảnh báo nếu hết hàng.

### US02: Thanh toán đơn hàng
* **Mô tả:** Xử lý thanh toán nhanh, hỗ trợ Voucher và nhiều hình thức (Tiền mặt/Chuyển khoản).
* **Tiêu chí chấp nhận (AC):** Tự động tính tổng tiền; Kiểm tra tính hợp lệ của Voucher; Tự động trừ tồn kho sau khi xong.

### US03: Áp dụng Voucher
* **Mô tả:** Nhân viên áp dụng mã giảm giá để kích thích mua sắm.
* **Tiêu chí chấp nhận (AC):** Kiểm tra hạn dùng và giá trị đơn hàng tối thiểu; Cập nhật lượt sử dụng Voucher.

### US04: Quản lý Đổi/Trả hàng
* **Mô tả:** Tìm kiếm đơn hàng cũ để xử lý đổi trả và tính chênh lệch giá.
* **Tiêu chí chấp nhận (AC):** Hệ thống tự cộng lại tồn kho khi trả hàng; Lưu lịch sử đổi trả.

---

## II. QUẢN LÝ KHO HÀNG & SẢN PHẨM
### US06: Thêm sản phẩm mới
* **Mô tả:** Cho phép thêm sản phẩm với các thông tin: Tên, danh mục, giá, số lượng.
* **Tiêu chí chấp nhận (AC):** Dữ liệu hợp lệ mới được lưu; Hiển thị ngay trong danh sách sau khi thêm.

### US07: Sửa thông tin sản phẩm
* **Mô tả:** Cập nhật thông tin sản phẩm để đảm bảo dữ liệu luôn chính xác.
* **Tiêu chí chấp nhận (AC):** Hiển thị đúng thông tin cũ; Cảnh báo nếu dữ liệu sửa không hợp lệ.

### US08: Xóa sản phẩm
* **Mô tả:** Loại bỏ sản phẩm không còn kinh doanh khỏi hệ thống.
* **Tiêu chí chấp nhận (AC):** Có hộp thoại xác nhận trước khi xóa; Chỉ người có quyền mới được thực hiện.

### US09: Tạo Phiếu Nhập hàng
* **Mô tả:** Ghi nhận lô hàng nhập từ nhà cung cấp để tăng tồn kho.
* **Tiêu chí chấp nhận (AC):** Ghi nhận được giá vốn; Tự động cộng tồn kho theo Màu/Size.

### US10: Quản lý Tồn kho
* **Mô tả:** Theo dõi số lượng chi tiết theo Màu sắc và Kích cỡ.
* **Tiêu chí chấp nhận (AC):** Cập nhật số liệu ngay lập tức; Cho phép điều chỉnh thủ công có ghi chú.

---

## III. QUẢN LÝ KHÁCH HÀNG
### US11: Tạo & Cập nhật Khách hàng
* **Mô tả:** Quản lý hồ sơ khách hàng (Tên, SĐT, Địa chỉ).
* **Tiêu chí chấp nhận (AC):** Số điện thoại là duy nhất; Tìm kiếm nhanh theo SĐT.

### US12: Xem Lịch sử Chi tiêu
* **Mô tả:** Theo dõi hành vi mua sắm và tổng giá trị khách đã chi tiêu.
* **Tiêu chí chấp nhận (AC):** Tính toán chính xác tổng chi tiêu lũy kế và điểm tích lũy.

### US13: Tích & Sử dụng Điểm
* **Mô tả:** Tích điểm sau mỗi đơn hàng và dùng điểm để giảm trừ thanh toán.
* **Tiêu chí chấp nhận (AC):** Điểm sử dụng không được vượt quá số điểm hiện có.

---

## IV. QUẢN LÝ NHÂN VIÊN
### US14: Tạo Tài khoản Nhân viên
* **Mô tả:** Cấp tài khoản và phân quyền (Admin, Bán hàng, Kho).
* **Tiêu chí chấp nhận (AC):** Chỉ Admin mới có quyền tạo tài khoản; Tên đăng nhập không được trùng.

### US15: Theo dõi Hiệu suất Bán hàng
* **Mô tả:** Đánh giá hiệu quả làm việc qua doanh thu cá nhân.
* **Tiêu chí chấp nhận (AC):** Báo cáo theo khoảng thời gian; Truy cập được chi tiết các đơn đã bán.

### US16: Thông tin & Lương nhân viên
* **Mô tả:** Lưu trữ thông tin cá nhân, lương cơ bản và hoa hồng.
* **Tiêu chí chấp nhận (AC):** Bảo mật thông tin lương; Chỉ Admin mới có quyền xem/sửa.

---

## V. BÁO CÁO & THỐNG KÊ
### US17: Báo cáo Doanh thu
* **Mô tả:** Tổng hợp doanh thu thuần theo ngày/tuần/tháng.
* **Tiêu chí chấp nhận (AC):** Có biểu đồ trực quan xu hướng doanh thu.

### US18: Top Sản phẩm Bán chạy
* **Mô tả:** Xác định các mặt hàng được ưa chuộng nhất.
* **Tiêu chí chấp nhận (AC):** Hiển thị danh sách Top 10; Lọc được theo Màu/Kích cỡ.
