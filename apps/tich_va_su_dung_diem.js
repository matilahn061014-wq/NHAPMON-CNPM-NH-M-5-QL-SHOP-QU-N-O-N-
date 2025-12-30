/**
 * Hệ thống Quản lý Tích điểm Khách hàng
 */
class LoyaltySystem {
    constructor(conversionRate = 0.01) {
        // 1. Thiết lập tỷ lệ tích điểm (Ví dụ: 0.01 = 1% giá trị đơn hàng)
        this.conversionRate = conversionRate;
        this.pointValue = 1000; // Ví dụ: 1 điểm = 1,000 VNĐ khi giảm trừ
    }

    // 2. Tự động cộng điểm sau khi thanh toán thành công
    processSuccessfulOrder(customer, orderAmount) {
        const pointsEarned = Math.floor(orderAmount * this.conversionRate);
        customer.points += pointsEarned;
        console.log(`> Đơn hàng thành công: +${pointsEarned} điểm cho ${customer.name}.`);
        return pointsEarned;
    }

    // 3. Áp dụng điểm để giảm giá
    applyPointsDiscount(customer, pointsToUse, orderTotal) {
        // Tiêu chí 3: Tổng số điểm sử dụng không được vượt quá tổng điểm đang có
        if (pointsToUse > customer.points) {
            throw new Error(`Thất bại: Khách hàng chỉ có ${customer.points} điểm, không thể dùng ${pointsToUse} điểm.`);
        }

        const discountAmount = pointsToUse * this.pointValue;
        
        // Đảm bảo giảm giá không vượt quá tổng đơn hàng
        const finalAmount = Math.max(0, orderTotal - discountAmount);
        
        // Trừ điểm sau khi áp dụng thành công
        customer.points -= pointsToUse;
        
        console.log(`> Áp dụng ${pointsToUse} điểm. Giảm giá: ${discountAmount.toLocaleString()}đ. Còn lại: ${finalAmount.toLocaleString()}đ.`);
        return { finalAmount, discountAmount };
    }
}

class Customer {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        this.points = 0;
    }
}

// --- CHẠY THỬ (TEST CASES) ---

const system = new LoyaltySystem(0.05); // Tỷ lệ 5%
const myCustomer = new Customer(1, "Nguyễn Văn A");

console.log("--- Bắt đầu Test ---");

// Test 1: Tích điểm
console.log(`\nBước 1: Khách mua đơn hàng 1,000,000đ`);
system.processSuccessfulOrder(myCustomer, 1000000); 
console.log(`Số dư điểm hiện tại: ${myCustomer.points}`); // Mong đợi: 50,000 điểm

// Test 2: Sử dụng điểm hợp lệ
console.log(`\nBước 2: Khách mua đơn mới 200,000đ và muốn dùng 20 điểm`);
system.applyPointsDiscount(myCustomer, 20, 200000); 
console.log(`Số dư điểm còn lại: ${myCustomer.points}`);

// Test 3: Sử dụng vượt quá số điểm (Tiêu chí chấp nhận số 3)
console.log(`\nBước 3: Thử dùng 1,000,000 điểm (Vượt quá số dư)`);
try {
    system.applyPointsDiscount(myCustomer, 1000000, 500000);
} catch (error) {
    console.error(error.message);
}

console.log("\n--- Kết thúc Test ---");