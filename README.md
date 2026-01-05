# NHAPMON-CNPM-NH-M-5-QL-SHOP-QU-N-O-N-
Nhóm thực hành gồm 5 thành viên: 
1. Nguyễn Hoàng Nhi
2. Trần Đình Khánh Uyên
3. Nguyễn Thị Thúy Lê
4. Nguyễn Phương Anh
5. Nguyễn Quỳnh Hương
   
🛠 Hướng dẫn Cài đặt & Chạy Project
 🛒 DỰ ÁN QUẢN LÝ SHOP QUẦN ÁO - NHÓM 5
📋 1. YÊU CẦU HỆ THỐNG 
Ngôn ngữ lập trình: Python 3.x trở lên.
Trình duyệt: Ưu tiên Google Chrome hoặc Microsoft Edge bản mới nhất.
Công cụ hỗ trợ: Visual Studio Code (VS Code).

🚀 2. HƯỚNG DẪN CÀI ĐẶT CHI TIẾT
Bước 1: Tải mã nguồn
* Mở Terminal/Command Prompt và sử dụng lệnh Git Clone:
  `git clone https://github.com/matilahn061014-wq/NHAPMON-CNPM-NH-M-5-QL-SHOP-QU-N-O-N-.git`
* Hoặc tải trực tiếp file ZIP từ GitHub và giải nén vào thư mục làm việc.
Bước 2: Thiết lập môi trường
1. Mở thư mục dự án bằng phần mềm **VS Code**.
2. Cài đặt Extension **Live Server** (Phím tắt `Ctrl+Shift+X` -> Tìm "Live Server" -> Nhấn Install).
3. Đảm bảo máy đã cài đặt Python (Kiểm tra bằng lệnh `python --version` trong terminal).
   
💻 3. HƯỚNG DẪN VẬN HÀNH 
 3.1. Chạy Giao diện người dùng 
1. Truy cập vào thư mục `interface`.
2. Tìm và mở file **`giao_dien_US01.html`**.
3. Chuột phải vào màn hình code, chọn **Open with Live Server**.
4. Trình duyệt sẽ tự động mở giao diện tại: `http://127.0.0.1:5500`.
 3.2. Chạy chức năng Quản lý 
Sử dụng Terminal trong VS Code (Phím tắt `` Ctrl + ` ``) để chạy các file xử lý dữ liệu

 ⚠️ 4. CÁC QUY TẮC QUAN TRỌNG
* Dữ liệu hệ thống:** Tuyệt đối không xóa hoặc đổi tên file `data.txt` và `nhanvien.txt` vì đây là nơi lưu trữ toàn bộ thông tin.
* Địa chỉ truy cập:** Chỉ sử dụng địa chỉ `localhost (127.0.0.1)` do Live Server cung cấp. **Không tự ý thay đổi (fake) địa chỉ IP** để tránh lỗi script.
* Độ phân giải:** Giao diện được tối ưu hóa cho màn hình Desktop độ phân giải **1920x1080**.

A. MÔ TẢ HỆ THỐNG: ​Hệ thống quản lý shop quần áo nữ giúp các cửa hàng thời trang nữ tối ưu hóa quy trình bán hàng và quản lý tồn kho đa thuộc tính. Mục tiêu là tăng tốc độ xử lý đơn hàng và nhận diện mẫu mã bán chạy để ra quyết định kinh doanh kịp thời, tăng lợi nhuận.
​Hệ thống được thiết kế cho các đối tượng sử dụng chính:
- ​Nhân viên bán hàng
- ​Khách hàng: Thông qua trải nghiệm mua – đổi trả – tích điểm.

​B. MỤC TIÊU HỆ THỐNG
​1. Hướng tới cửa hàng:
- ​Tự động hóa các công việc: bán hàng, nhập kho, tồn kho, báo cáo.
- ​Giảm sai sót khi tính tiền, quản lý voucher, trừ kho.
​2. Hướng tới khách hàng:
- ​Hệ thống được thiết kế để tối ưu trải nghiệm khách mua sắm.
- ​Tương tác cá nhân hóa thông qua thông tin khách hàng (hồ sơ, thói quen mua sắm).

​C. LỢI ÍCH KHI XÂY DỰNG HỆ THỐNG
- ​Quy trình mua bán hàng nhanh – chính xác.
- ​Kiểm soát tồn kho chặt chẽ.
- ​Báo cáo rõ ràng giúp ra quyết định tốt hơn.
- ​Giảm thất thoát, giảm sai sót thủ công.
- ​Chính sách tích điểm rõ ràng.
- ​Đổi trả dễ dàng – minh bạch.
- ​Trải nghiệm chuyên nghiệp hơn.
  
D. QUY TRÌNH VẬN HÀNH CỦA HỆ THỐNG
1. Giai đoạn Nhập hàng & Quản lý kho
Đây là bước đầu tiên để hệ thống có dữ liệu vận hành:
Quản lý thuộc tính: Khi nhập hàng, nhân viên khai báo sản phẩm kèm theo các thuộc tính (Size, màu sắc, chất liệu).
Số hóa tồn kho: Mỗi sản phẩm được gán mã để hệ thống tự động theo dõi số lượng tồn thực tế, thay vì ghi chép sổ sách.
2. Giai đoạn Bán hàng & Giao dịch (Tại quầy)
Đây là phần cốt lõi để "tăng tốc độ" như trong mô tả của bạn:
- Quét mã nhanh: Nhân viên dùng máy quét để tính tiền, hệ thống tự lấy giá và áp dụng các chương trình khuyến mãi/voucher có sẵn.
- Nhận diện khách hàng: Nhân viên nhập số điện thoại để kiểm tra hồ sơ khách, lịch sử mua sắm và tích điểm tự động.
- Xử lý thanh toán: In hóa đơn và hệ thống tự động trừ kho ngay lập tức để tránh lệch số liệu.
3. Giai đoạn Sau bán hàng & Quản trị
Hệ thống sử dụng dữ liệu đã thu thập để phục vụ quản lý:
- Đổi trả hàng: Dựa trên hóa đơn lưu trữ, hệ thống kiểm tra điều kiện đổi trả để thực hiện nhanh chóng và minh bạch.
- Báo cáo tự động: Cuối ngày, chủ shop không cần cộng sổ. Hệ thống tự xuất báo cáo:
Mẫu mã nào bán chạy nhất (để nhập thêm).
Doanh thu theo ngày/nhân viên.
Cảnh báo hàng sắp hết kho.
Chăm sóc khách hàng: Dựa trên thói quen mua sắm (size thường mua, kiểu dáng yêu thích) để gửi tin nhắn ưu đãi cá nhân hóa.

