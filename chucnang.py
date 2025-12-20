#us2
class PaymentService {
    constructor() {
        this.vouchers = [
            { code: "GIAM20", type: "FIXED", value: 20000, minOrder: 100000, expiry: "2025-12-31" }
        ];
        this.inventory = { "AO-THUN-01": 50, "QUAN-JEAN-02": 30 };
    }

    // Tiêu chí 1: Tự động tính tổng tiền từ danh sách sản phẩm
    calculateSubtotal(items) {
        return items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    }

    // Tiêu chí 2: Kiểm tra Voucher
    validateVoucher(code, subtotal) {
        const v = this.vouchers.find(x => x.code === code);
        const now = new Date();
        if (!v) return { valid: false, msg: "Mã không tồn tại" };
        if (new Date(v.expiry) < now) return { valid: false, msg: "Mã hết hạn" };
        if (subtotal < v.minOrder) return { valid: false, msg: "Chưa đủ giá trị tối thiểu" };
        return { valid: true, voucher: v };
    }

    // Tiêu chí 3 & 4: Xử lý thanh toán và trừ tồn kho
    processPayment(orderData) {
        const { items, voucherCode, paymentMethod } = orderData;
        const subtotal = this.calculateSubtotal(items);
        let discount = 0;

        // Tính toán chiết khấu
        if (voucherCode) {
            const check = this.validateVoucher(voucherCode, subtotal);
            if (check.valid) {
                discount = check.voucher.type === "FIXED" ? check.voucher.value : (subtotal * check.voucher.value / 100);
            }
        }

        const finalTotal = subtotal - discount;

        // Tiêu chí 4: Trừ tồn kho và Lưu giao dịch
        items.forEach(item => {
            if (this.inventory[item.id]) this.inventory[item.id] -= item.quantity;
        });

        console.log(`--- HÓA ĐƠN ---`);
        console.log(`Hình thức: ${paymentMethod}`); // Tiền mặt, Chuyển khoản, Thẻ
        console.log(`Tổng cuối: ${finalTotal.toLocaleString()}đ`);
        return { success: true, finalTotal };
    }
}
#us3
 constructor() {
        // Giả lập Database Voucher
        this.vouchers = [
            { id: 1, code: "XINCHAO", type: "FIXED", value: 20000, minOrder: 50000, expiry: "2025-12-31", limit: 100, used: 5 },
            { id: 2, code: "GIAM10", type: "PERCENT", value: 10, minOrder: 100000, expiry: "2025-01-01", limit: 50, used: 0 }
        ];
    }

    // Công việc 2: Hàm kiểm tra tính hợp lệ
    checkValidity(code, orderTotal) {
        const voucher = this.vouchers.find(v => v.code.toUpperCase() === code.toUpperCase());
        const now = new Date();

        if (!voucher) return { valid: false, msg: "Mã giảm giá không tồn tại." };
        if (new Date(voucher.expiry) < now) return { valid: false, msg: "Mã đã hết hạn sử dụng." };
        if (orderTotal < voucher.minOrder) return { valid: false, msg: `Đơn hàng chưa đạt giá trị tối thiểu (${voucher.minOrder.toLocaleString()}đ).` };
        if (voucher.used >= voucher.limit) return { valid: false, msg: "Mã đã hết lượt sử dụng." };

        return { valid: true, voucher };
    }

    // Công việc 3: Tính toán số tiền giảm
    calculateDiscount(voucher, orderTotal) {
        let discount = 0;
        if (voucher.type === "FIXED") {
            discount = voucher.value;
        } else {
            discount = (orderTotal * voucher.value) / 100;
        }
        // Đảm bảo số tiền giảm không âm và không vượt quá tổng đơn
        return Math.min(discount, orderTotal);
    }

    // Công việc 4: Cập nhật lượt sử dụng
    updateUsage(code) {
        const voucher = this.vouchers.find(v => v.code === code);
        if (voucher) {
            voucher.used += 1;
            return true;
        }
        return false;
    }
}
const service = new VoucherService();
let currentOrderTotal = 150000; // Tiêu chí 1: Hệ thống tự tính tổng trước (giả lập)
let activeVoucher = null;

function onApplyVoucher() {
    const inputCode = document.getElementById("voucherInput").value;
    const result = service.checkValidity(inputCode, currentOrderTotal);

    const msgElement = document.getElementById("message");
    const discountElement = document.getElementById("discountDisplay");
    const finalTotalElement = document.getElementById("finalTotal");

    if (result.valid) {
        const discount = service.calculateDiscount(result.voucher, currentOrderTotal);
        activeVoucher = result.voucher.code;

        // Tiêu chí 4: Hiển thị rõ ràng số tiền giảm và tổng cuối cùng
        msgElement.className = "success";
        msgElement.innerText = "Áp dụng mã thành công!";
        discountElement.innerText = `-${discount.toLocaleString()}đ`;
        finalTotalElement.innerText = `${(currentOrderTotal - discount).toLocaleString()}đ`;
    } else {
        msgElement.className = "error";
        msgElement.innerText = result.msg;
        activeVoucher = null;
    }
}

// Giả lập sự kiện Thanh toán hoàn tất
function onCompletePayment() {
    if (activeVoucher) {
        service.updateUsage(activeVoucher);
        alert("Thanh toán thành công! Lượt dùng voucher đã được cập nhật.");
    }
}
<div class="checkout-card">
    <h3>Thanh toán đơn hàng</h3>
    <p>Tạm tính: <span id="subtotal">150,000đ</span></p>

    <div class="voucher-group">
        <input type="text" id="voucherInput" placeholder="Nhập mã (VD: XINCHAO)">
        <button onclick="onApplyVoucher()">Áp dụng</button>
    </div>
    <p id="message"></p>

    <hr>
    <p>Giảm giá: <span id="discountDisplay">0đ</span></p>
    <p><strong>Tổng cộng: <span id="finalTotal">150,000đ</span></strong></p>
    
    <button class="btn-pay" onclick="onCompletePayment()">Xác nhận thanh toán</button>
</div>
#us5
# Giả định: Có các Models/Database Service đã được định nghĩa
# from app.models import Order, ReturnRequest, Product
# from app.db_service import get_order_by_id, create_return_request

class ReturnService:
    def find_and_start_return(self, order_id: str, staff_id: str) -> dict:
        """
        1. Tìm kiếm đơn hàng theo ID.
        2. Tạo một yêu cầu Đổi/Trả mới liên kết với đơn hàng đó.
        """
        # (1) Tìm kiếm đơn hàng cũ
        order = get_order_by_id(order_id)
        if not order:
            return {"success": False, "message": "Không tìm thấy đơn hàng."}

        # Kiểm tra các điều kiện Đổi/Trả (ví dụ: trong thời hạn cho phép)
        if not order.is_returnable():
             return {"success": False, "message": "Đơn hàng đã quá thời hạn Đổi/Trả."}

        # (2) Tạo yêu cầu Đổi/Trả ban đầu (Draft)
        new_return = create_return_request(
            order_id=order_id,
            status="DRAFT",
            created_by=staff_id
        )

        return {"success": True, "return_request": new_return, "order_details": order.items}
        # Giả định: Có hàm cập nhật tồn kho
# from app.inventory_service import update_inventory

    def restock_products(self, return_request_id: str, restock_items: list):
        """
        Cập nhật tồn kho cho các sản phẩm được trả lại.
        restock_items: [{"product_id": "P001", "quantity": 1}]
        """
        return_request = get_return_request_by_id(return_request_id)

        if return_request.status != "ACCEPTED":
             return {"success": False, "message": "Yêu cầu Đổi/Trả chưa được chấp nhận để hoàn kho."}

        for item in restock_items:
            product_id = item["product_id"]
            quantity = item["quantity"]

            # Gọi dịch vụ tồn kho để cộng lại số lượng
            success = update_inventory(product_id, quantity) # Tăng tồn kho
            if not success:
                # Xử lý lỗi nếu không thể cập nhật tồn kho
                print(f"Lỗi hoàn kho cho sản phẩm {product_id}")
                return {"success": False, "message": "Lỗi khi cập nhật tồn kho."}

        # Cập nhật trạng thái yêu cầu Đổi/Trả (ví dụ: "RESTOCKED")
        update_return_request_status(return_request_id, "RESTOCKED")
        
        return {"success": True, "message": "Đã hoàn kho thành công."}
        def calculate_refund_or_charge(self, returned_items: list, new_items: list) -> dict:
        """
        Tính toán tổng giá trị sản phẩm được trả và sản phẩm mới được đổi.
        """
        # (1) Tính tổng giá trị sản phẩm trả lại (dựa trên giá lúc mua)
        total_returned_value = 0
        for item in returned_items:
            # Giá bán lẻ tại thời điểm mua hàng
            total_returned_value += item["price_at_sale"] * item["quantity"]

        # (2) Tính tổng giá trị sản phẩm đổi (dựa trên giá hiện tại)
        total_new_value = 0
        for item in new_items:
            # Lấy giá hiện tại hoặc giá khuyến mãi
            current_price = get_product_current_price(item["product_id"])
            total_new_value += current_price * item["quantity"]

        # (3) Tính chênh lệch
        # Chênh lệch dương (> 0): Cần hoàn tiền lại cho khách
        # Chênh lệch âm (< 0): Khách cần trả thêm
        price_difference = total_returned_value - total_new_value

        return {
            "total_returned_value": total_returned_value,
            "total_new_value": total_new_value,
            "difference": price_difference,
            "action": "REFUND" if price_difference > 0 else ("CHARGE" if price_difference < 0 else "NONE")
        }
        # Giả định: Có một hàm lưu trữ sự kiện giao dịch
# from app.logging_service import log_transaction

    def finalize_return_transaction(self, return_request_id: str, final_amount: float, action: str):
        """
        Lưu trữ lịch sử giao dịch chi tiết và cập nhật trạng thái cuối cùng.
        """
        # (1) Cập nhật trạng thái cuối cùng của yêu cầu Đổi/Trả
        update_return_request_status(return_request_id, "COMPLETED")
        
        # (2) Lưu trữ lịch sử giao dịch chi tiết
        transaction_log = {
            "return_id": return_request_id,
            "final_amount": abs(final_amount),
            "type": "RETURN_REFUND" if action == "REFUND" else ("RETURN_CHARGE" if action == "CHARGE" else "EXCHANGE_ONLY"),
            "timestamp": datetime.now(),
            "staff_id": current_user.id
        }
        
        log_transaction(transaction_log)

        return {"success": True, "message": "Giao dịch Đổi/Trả đã hoàn tất và được ghi lại."}
        #us15
        class ReportService {
    constructor(orders) {
        this.orders = orders; // Danh sách đơn hàng từ US02
    }

    // Công việc 1: Tổng hợp doanh thu và số đơn hàng theo nhân viên
    getRevenueByStaff() {
        return this.orders.reduce((report, order) => {
            if (!report[order.staffId]) {
                report[order.staffId] = { totalRevenue: 0, orderCount: 0 };
            }
            report[order.staffId].totalRevenue += order.finalTotal;
            report[order.staffId].orderCount += 1;
            return report;
        }, {});
    }

    // Công việc 2: Lọc báo cáo theo khoảng thời gian (ngày, tháng)
    filterOrdersByDate(startDate, endDate) {
        const start = new Date(startDate);
        const end = new Date(endDate);
        
        return this.orders.filter(order => {
            const orderDate = new Date(order.timestamp);
            return orderDate >= start && orderDate <= end;
        });
    }

    // Công việc 3: Hiển thị chi tiết các đơn hàng của một nhân viên
    getStaffDetailReport(staffId) {
        const staffOrders = this.orders.filter(order => order.staffId === staffId);
        return {
            staffId: staffId,
            orders: staffOrders,
            summary: staffOrders.reduce((acc, curr) => acc + curr.finalTotal, 0)
        };
    }
}