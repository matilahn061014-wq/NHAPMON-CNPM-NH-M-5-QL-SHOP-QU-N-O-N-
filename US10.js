/**
 * US10: QUẢN LÝ TỒN KHO
 * Chạy test logic: Lọc phiên bản, Xem lịch sử, Điều chỉnh thủ công
 */

// --- 1. CƠ SỞ DỮ LIỆU GIẢ LẬP (Mô phỏng Kho hàng) ---
let inventory = [
    { sku: "TS-WHT-L", name: "Áo Thun", color: "Trắng", size: "L", stock: 100, lastUpdate: "2025-12-20" },
    { sku: "TS-BLK-M", name: "Áo Thun", color: "Đen", size: "M", stock: 45, lastUpdate: "2025-12-21" },
    { sku: "JN-BLU-32", name: "Quần Jean", color: "Xanh", size: "32", stock: 30, lastUpdate: "2025-12-22" },
    { sku: "JN-BLK-32", name: "Quần Jean", color: "Đen", size: "32", stock: 12, lastUpdate: "2025-12-23" }
];

// --- 2. LỊCH SỬ BIẾN ĐỘNG (Dùng cho Tiêu chí 3) ---
let transactionHistory = [];

/**
 * Hàm ghi lại lịch sử
 */
function logHistory(sku, type, quantity, reason) {
    transactionHistory.push({
        time: new Date().toLocaleString('vi-VN'),
        sku: sku,
        action: type,
        change: quantity > 0 ? `+${quantity}` : quantity,
        note: reason
    });
}

// --- 3. CÁC TÍNH NĂNG CHÍNH ---

/**
 * [Tiêu chí 1 & 2]: Hiển thị tồn kho và Lọc
 */
function displayInventory(filter = {}) {
    console.log(`\n🔍 ĐANG TÌM KIẾM TỒN KHO: ${JSON.stringify(filter)}`);
    
    const result = inventory.filter(item => {
        return (!filter.color || item.color === filter.color) &&
               (!filter.name || item.name === filter.name);
    });

    if (result.length > 0) {
        console.table(result);
    } else {
        console.log("❌ Không tìm thấy sản phẩm phù hợp.");
    }
}

/**
 * [Tiêu chí 3]: Xem lịch sử
 */
function showHistory() {
    console.log("\n📜 LỊCH SỬ XUẤT/NHẬP/ĐIỀU CHỈNH GẦN NHẤT:");
    console.table(transactionHistory);
}

/**
 * [Tiêu chí 4]: Điều chỉnh tồn kho thủ công
 */
function adjustStock(sku, newStock, reason) {
    const item = inventory.find(p => p.sku === sku);
    
    if (item) {
        const diff = newStock - item.stock;
        if (diff === 0) return;

        console.log(`\n⚙️  ĐANG ĐIỀU CHỈNH: ${sku} (${item.stock} -> ${newStock})`);
        
        item.stock = newStock;
        item.lastUpdate = new Date().toISOString().split('T')[0];

        // Ghi lại lịch sử điều chỉnh
        logHistory(sku, "ĐIỀU CHỈNH THỦ CÔNG", diff, reason);
    } else {
        console.log(`❌ Không tìm thấy SKU: ${sku}`);
    }
}

// --- 4. KỊCH BẢN KIỂM THỬ (TEST SCRIPTS) ---

// Test 1: Hiển thị tổng quan ban đầu
console.log("--- BÁO CÁO TỒN KHO TỔNG QUAN ---");
console.table(inventory);

// Test 2: Lọc sản phẩm theo màu (Tiêu chí 2)
displayInventory({ color: "Đen" });

// Test 3: Điều chỉnh tồn kho thủ công (Tiêu chí 4)
// Giả sử kiểm kho thực tế thấy mất 2 áo thun trắng, và dư 3 quần jean xanh
adjustStock("TS-WHT-L", 98, "Hàng bị lỗi rách khi kiểm kho");
adjustStock("JN-BLU-32", 33, "Tìm thấy hàng trong góc kho");

// Test 4: Hiển thị lại bảng kho sau khi chỉnh và xem lịch sử (Tiêu chí 3)
displayInventory();
showHistory();