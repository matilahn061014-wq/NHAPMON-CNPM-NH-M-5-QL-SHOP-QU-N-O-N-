# NHAPMON-CNPM-NH-M-5-QL-SHOP-QU-N-O-N-
Nhóm thực hành gồm 5 thành viên: 
1. Nguyễn Hoàng Nhi
2. Trần Đình Khánh Uyên
3. Nguyễn Thị Thúy Lê
4. Nguyễn Phương Anh
5. Nguyễn Quỳnh Hương
   
🛠 Hướng dẫn Cài đặt & Chạy Project
1. Tải Project về máy
Có 2 cách để lấy mã nguồn:
Cách 1 (Dùng Git): Mở terminal và gõ lệnh:
Bash
git clone https://github.com/matilahn061014-wq/NHAPMON-CNPM-NH-M-5-QL-SHOP-QU-N-O-N-.git
Cách 2 (Tải trực tiếp): Nhấn vào nút Code (màu xanh) trên GitHub và chọn Download ZIP, sau đó giải nén file vừa tải.
2. Cài đặt môi trường phát triển 
Để project chạy ổn định nhất và hỗ trợ tự động cập nhật khi sửa code, bạn nên sử dụng Visual Studio Code (VS Code):
Tải và cài đặt VS Code.
Mở thư mục project vừa tải về bằng VS Code.
Cài đặt Extension Live Server:
Vào mục Extensions (phím tắt Ctrl + Shift + X).
Tìm kiếm "Live Server" và nhấn Install.
3. Cách chạy chương trình
Cách 1 (Dùng Live Server):
Mở file .html bất kỳ trong thư mục interface.
Chuột phải vào màn hình code và chọn Open with Live Server.
Trình duyệt sẽ tự động mở giao diện tại địa chỉ: http://127.0.0.1:5500.
Cách 2 (Mở thủ công):
Truy cập vào thư mục interface.
Click đúp chuột vào file giao_dien_US01.html (hoặc file trang chủ) để mở bằng trình duyệt (Chrome, Edge...).
⚠️ Lưu ý quan trọng
Hỗ trợ trình duyệt: Tốt nhất trên Google Chrome hoặc Microsoft Edge bản mới nhất.
Độ phân giải: Giao diện đang được tối ưu hóa cho màn hình Desktop (1920x1080).

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

