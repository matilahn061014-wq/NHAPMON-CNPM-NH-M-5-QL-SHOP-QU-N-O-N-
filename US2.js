class PaymentService {
    constructor() {
        // Tiêu chí: Quản lý danh sách Voucher
        this.vouchers = [
            { code: "GIAM20", type: "FIXED", value: 20000, minOrder: 100000, expiry: "2025-12-31" }
        ];
        // Tiêu chí: Quản lý tồn kho cơ bản để trừ hàng khi thanh toán
        this.inventory = { "AO-THUN-01": 50, "QUAN-JEAN-02": 30 };
    }

    // Tiêu chí 1: Tự động tính tổng tiền từ danh sách sản phẩm
    calculateSubtotal(items) {
        return items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    }

    // Tiêu chí 2: Kiểm tra Voucher (Hạn dùng, giá trị tối thiểu)
    validateVoucher(code, subtotal) {
        const v = this.vouchers.find(x => x.code === code);
        const now = new Date();
        
        if (!v) return { valid: false, msg: "Mã không tồn tại" };
        if (new Date(v.expiry) < now) return { valid: false, msg: "Mã đã hết hạn" };
        if (subtotal < v.minOrder) return { valid: false, msg: "Chưa đủ giá trị tối thiểu" };
        
        return { valid: true, voucher: v };
    }

    // Tiêu chí 3 & 4: Xử lý thanh toán và trừ tồn kho
    processPayment(orderData) {
        const subtotal = this.calculateSubtotal(orderData.items);
        let discount = 0;

        // Tính toán chiết khấu nếu có Voucher
        if (orderData.voucherCode) {
            const check = this.validateVoucher(orderData.voucherCode, subtotal);
            if (check.valid) {
                discount = check.voucher.value;
            } else {
                console.log("⚠️ Cảnh báo Voucher:", check.msg);
            }
        }

        const finalTotal = subtotal - discount;

        // Giả lập trừ tồn kho
        orderData.items.forEach(item => {
            if (this.inventory[item.name]) {
                this.inventory[item.name] -= item.quantity;
            }
        });

        return {
            orderId: "DH" + Math.floor(Math.random() * 1000),
            subtotal: subtotal,
            discount: discount,
            finalTotal: finalTotal,
            paymentMethod: orderData.paymentMethod,
            status: "Thanh toán thành công"
        };
    }
}

// --- ĐOẠN CODE CHẠY THỬ (TEST) ---
const paymentService = new PaymentService();

const myCart = [
    { name: "AO-THUN-01", price: 200000, quantity: 2 }, // 400,000đ
    { name: "QUAN-JEAN-02", price: 300000, quantity: 1 } // 300,000đ
];

const orderData = {
    items: myCart,
    voucherCode: "GIAM20",
    paymentMethod: "Tiền mặt"
};

console.log("=== KIỂM TRA HỆ THỐNG THANH TOÁN US2 ===");
const result = paymentService.processPayment(orderData);
console.table(result);
console.log("Tồn kho sau khi bán:", paymentService.inventory);