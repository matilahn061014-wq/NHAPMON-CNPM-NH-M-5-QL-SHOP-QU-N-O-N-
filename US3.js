class VoucherService {
    constructor() {
        // Dữ liệu mẫu (CVC 2: Mã tồn tại, còn hạn, đạt minOrder)
        this.vouchers = [
            { code: "GIAM20", type: "FIXED", value: 20000, minOrder: 100000, expiry: "2025-12-31", limit: 10 }
        ];
    }

    applyVoucher(items, voucherCode) {
        // TC1: Tự động tính tổng giá trị đơn hàng
        const subtotal = items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        let discount = 0;

        // TC3 & CVC 2: Kiểm tra tính hợp lệ
        const v = this.vouchers.find(x => x.code === voucherCode);
        if (v && subtotal >= v.minOrder && new Date(v.expiry) > new Date() && v.limit > 0) {
            discount = v.value;
            v.limit -= 1; // CVC 4: Cập nhật lượt sử dụng
        }

        // TC4 & CVC 3: Hiển thị rõ ràng số tiền giảm và tổng cuối cùng
        return {
            orderId: "DH" + Math.floor(Math.random() * 1000),
            subtotal: subtotal,
            discount: discount,
            finalTotal: subtotal - discount,
            status: "Thanh toán thành công"
        };
    }
}

// --- CHẠY THỬ ---
const service = new VoucherService();
const cart = [{ name: "Áo sơ mi", price: 150000, quantity: 2 }]; // Tổng 300k
console.table(service.applyVoucher(cart, "GIAM20"));