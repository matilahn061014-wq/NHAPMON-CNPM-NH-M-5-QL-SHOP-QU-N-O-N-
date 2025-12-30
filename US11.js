/**
 * US11: QUẢN LÝ KHÁCH HÀNG
 * Chạy test logic: Tạo mới, Tìm kiếm, Cập nhật và Ràng buộc SĐT
 */

// --- 1. CƠ SỞ DỮ LIỆU GIẢ LẬP (Mô phỏng Danh sách khách hàng) ---
let customers = [
    { id: 1, name: "Nguyễn Văn A", phone: "0901234567", address: "123 Lê Lợi, Đà Nẵng" },
    { id: 2, name: "Trần Thị B", phone: "0908888888", address: "456 Nguyễn Huệ, HCM" }
];

// --- 2. CÁC HÀM XỬ LÝ CHÍNH ---

/**
 * [Tiêu chí 1 & 4]: Tạo khách hàng mới
 * Kiểm tra SĐT duy nhất trước khi thêm
 */
function createCustomer(name, phone, address) {
    console.log(`\n➕ ĐANG TẠO KHÁCH HÀNG: ${name} (${phone})`);
    
    // Tiêu chí 4: Kiểm tra trùng SĐT
    const isExist = customers.find(c => c.phone === phone);
    if (isExist) {
        console.error(`❌ LỖI: Số điện thoại ${phone} đã tồn tại trong hệ thống!`);
        return null;
    }

    // Tiêu chí 1: Tạo hồ sơ nếu hợp lệ
    const newCustomer = {
        id: customers.length + 1,
        name: name,
        phone: phone,
        address: address
    };
    customers.push(newCustomer);
    console.log(`✅ Thành công: Đã thêm khách hàng #${newCustomer.id}`);
    return newCustomer;
}

/**
 * [Tiêu chí 2]: Tìm kiếm khách hàng theo SĐT hoặc Tên
 */
function searchCustomer(query) {
    console.log(`\n🔍 TÌM KIẾM VỚI TỪ KHÓA: "${query}"`);
    const results = customers.filter(c => 
        c.phone.includes(query) || 
        c.name.toLowerCase().includes(query.toLowerCase())
    );

    if (results.length > 0) {
        console.table(results);
    } else {
        console.log("❌ Không tìm thấy khách hàng nào.");
    }
    return results;
}

/**
 * [Tiêu chí 3]: Chỉnh sửa thông tin hồ sơ
 */
function updateCustomer(phone, newInfo) {
    console.log(`\n⚙️  CẬP NHẬT THÔNG TIN CHO SĐT: ${phone}`);
    const customer = customers.find(c => c.phone === phone);

    if (customer) {
        if (newInfo.name) customer.name = newInfo.name;
        if (newInfo.address) customer.address = newInfo.address;
        console.log(`✅ Đã cập nhật hồ sơ khách hàng ${customer.name}`);
    } else {
        console.log("❌ Không tìm thấy khách hàng để sửa.");
    }
}

/**
 * [Công việc con 4]: Gán khách hàng vào đơn hàng
 */
function assignToOrder(orderId, customerPhone) {
    const customer = customers.find(c => c.phone === customerPhone);
    if (customer) {
        console.log(`\n🛒 ĐƠN HÀNG #${orderId}: Đã gán cho khách hàng [${customer.name} - ${customer.phone}]`);
    } else {
        console.log(`\n❌ LỖI: Không thể gán khách hàng vào đơn hàng #${orderId} (SĐT không tồn tại)`);
    }
}

// --- 3. KỊCH BẢN KIỂM THỬ (TEST CASES) ---

// Test 1: Hiển thị danh sách ban đầu
console.log("--- DANH SÁCH KHÁCH HÀNG HIỆN TẠI ---");
console.table(customers);

// Test 2: Tạo khách hàng mới (Hợp lệ)
createCustomer("Lê Văn C", "0912345678", "789 Phan Châu Trinh, Hà Nội");

// Test 3: Tạo khách hàng trùng SĐT (Tiêu chí 4 - Phải báo lỗi)
createCustomer("Người lạ", "0901234567", "Địa chỉ giả");

// Test 4: Tìm kiếm nhanh (Tiêu chí 2)
searchCustomer("Trần Thị"); // Tìm theo tên
searchCustomer("0912");     // Tìm theo đầu số điện thoại

// Test 5: Cập nhật thông tin (Tiêu chí 3)
updateCustomer("0908888888", { name: "Trần Thị B (VIP)", address: "Căn hộ Landmark 81, HCM" });

// Test 6: Gán vào đơn hàng (Công việc con 4)
assignToOrder("DH-20251226-001", "0912345678");

// Cuối cùng: Xem lại danh sách tổng hợp
console.log("\n--- DANH SÁCH KHÁCH HÀNG SAU KHI TEST ---");
console.table(customers);