// 1. Dữ liệu giả lập từ hệ thống Nhóm 5
const inventory = [
    { id: "SP001", name: "Áo Sơ Mi Lụa", price: 250000, stock: 42 },
    { id: "SP005", name: "Đầm Hoa Nhí Dáng Dài", price: 450000, stock: 12 },
    { id: "SP007", name: "Áo Thun Basic", price: 150000, stock: 100 },
    { id: "SP008", name: "Áo Khoác Blazer", price: 650000, stock: 8 },
];

const vouchers = [
    { code: "GIAM10", description: "Giảm 10%", minOrder: 500000, discount: 0.1, type: "percent" },
    { code: "VUITET", description: "Giảm 50k", minOrder: 0, discount: 500000, type: "fixed" }
];

// 2. Class Quản lý Đơn hàng
class OrderSystem {
    constructor(customer = null) {
        this.customer = customer;
        this.cart = [];
        this.voucherApplied = null;
    }

    // Chức năng: Tìm kiếm hoặc Quét mã
    addProduct(input) {
        const product = inventory.find(p => p.id === input || p.name.toLowerCase().includes(input.toLowerCase()));

        if (!product) return console.error("❌ Không tìm thấy sản phẩm!");
        if (product.stock <= 0) return console.warn(`⚠️ Sản phẩm ${product.name} đã HẾT HÀNG!`);

        const itemInCart = this.cart.find(item => item.id === product.id);

        if (itemInCart) {
            itemInCart.quantity += 1;
        } else {
            this.cart.push({ ...product, quantity: 1 });
        }
        
        console.log(`✅ Đã thêm: ${product.name}`);
        this.renderCart();
    }

    // Chức năng: Điều chỉnh số lượng
    updateQuantity(id, newQty) {
        const item = this.cart.find(i => i.id === id);
        if (item) {
            if (newQty <= 0) {
                this.cart = this.cart.filter(i => i.id !== id);
            } else {
                item.quantity = newQty;
            }
        }
        this.renderCart();
    }

    // Chức năng: Tính tiền & Voucher
    calculateTotal() {
        let subTotal = this.cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        let discountValue = 0;

        if (this.voucherApplied) {
            if (subTotal >= this.voucherApplied.minOrder) {
                discountValue = this.voucherApplied.type === "percent" 
                    ? subTotal * this.voucherApplied.discount 
                    : this.voucherApplied.discount;
            }
        }
        return { subTotal, discountValue, total: subTotal - discountValue };
    }

    // Chức năng: Thanh toán & In Bill
    processPayment(method) {
        const final = this.calculateTotal();
        console.log("\n--- HÓA ĐƠN BÁN HÀNG ---");
        console.log(`Khách hàng: ${this.customer ? this.customer.name : "Khách vãng lai"}`);
        console.log(`Hình thức: ${method}`);
        this.cart.forEach(item => {
            console.log(`- ${item.name} x${item.quantity}: ${(item.price * item.quantity).toLocaleString()}đ`);
        });
        console.log(`Tổng tiền: ${final.total.toLocaleString()}đ`);
        console.log("------------------------\n");
    }

    renderCart() {
        console.table(this.cart.map(i => ({ "Tên": i.name, "SL": i.quantity, "Đơn giá": i.price })));
    }
}

// 3. Chạy thử chương trình
const myOrder = new OrderSystem({ name: "Nguyễn Thu Thảo", rank: "VIP" });

// Nhân viên quét mã SP008
myOrder.addProduct("SP008"); 
// Nhân viên quét mã SP005
myOrder.addProduct("SP005"); 
// Áp dụng voucher
myOrder.voucherApplied = vouchers[0]; // GIAM10

// Chọn thanh toán bằng THẺ VISA và in hóa đơn
myOrder.processPayment("THẺ VISA");