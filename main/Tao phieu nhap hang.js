/**
 * MÃ NGUỒN KIỂM THỬ HỆ THỐNG NHẬP KHO (US09)
 * Chạy trực tiếp trên VS Code bằng Node.js
 */

// --- 1. CƠ SỞ DỮ LIỆU GIẢ LẬP (Mô phỏng dữ liệu ban đầu) ---
let inventory = [
    { sku: "AO-THUN-TRANG-L", name: "Áo Thun", color: "Trắng", size: "L", stock: 10, costPrice: 100000 },
    { sku: "AO-THUN-DEN-M", name: "Áo Thun", color: "Đen", size: "M", stock: 5, costPrice: 105000 },
    { sku: "QUAN-JEAN-32", name: "Quần Jean", color: "Xanh", size: "32", stock: 2, costPrice: 300000 }
];

// --- 2. LOGIC XỬ LÝ NHẬP HÀNG ---

/**
 * Hàm xử lý Phiếu Nhập Hàng
 * @param {string} supplier - Nhà cung cấp
 * @param {string} date - Ngày nhập
 * @param {Array} items - Danh sách các sản phẩm nhập (sku, qty, importPrice)
 */
function createPurchaseOrder(supplier, date, items) {
    console.log(`\n================================================`);
    console.log(`TIẾN HÀNH NHẬP HÀNG: ${supplier} | Ngày: ${date}`);
    console.log(`================================================`);

    let totalOrderValue = 0;

    items.forEach((item, index) => {
        // Tìm sản phẩm trong kho bằng mã SKU (đảm bảo đúng Màu/Size)
        const product = inventory.find(p => p.sku === item.sku);

        if (!product) {
            console.error(`❌ [Lỗi]: SKU ${item.sku} không tồn tại trong hệ thống.`);
            return;
        }

        // Thực hiện các tiêu chí chấp nhận của US09:
        
        // TC 3: Ghi nhận giá nhập vào giá vốn
        product.costPrice = item.importPrice;

        // TC 4: Tự động cộng số lượng vào tồn kho
        const oldStock = product.stock;
        product.stock += item.qty;

        // Tính toán bổ sung: Thành tiền
        const subTotal = item.qty * item.importPrice;
        totalOrderValue += subTotal;

        console.log(`${index + 1}. ✅ SKU: ${item.sku}`);
        console.log(`   - Trạng thái: Tồn kho ${oldStock} -> ${product.stock} (Cộng thêm ${item.qty})`);
        console.log(`   - Giá vốn cập nhật: ${item.importPrice.toLocaleString()}đ`);
    });

    console.log(`------------------------------------------------`);
    console.log(`TỔNG GIÁ TRỊ PHIẾU NHẬP: ${totalOrderValue.toLocaleString()} VNĐ`);
    console.log(`================================================\n`);
}

// --- 3. KỊCH BẢN KIỂM THỬ (TEST CASE) ---

// In trạng thái kho trước khi nhập
console.log("📊 TRẠNG THÁI KHO TRƯỚC KHI TEST:");
console.table(inventory);

// Giả lập dữ liệu từ một phiếu nhập hàng thực tế
const mockImportData = [
    { sku: "AO-THUN-TRANG-L", qty: 50, importPrice: 95000 },  // Nhập thêm 50 Áo Trắng, giá rẻ hơn cũ
    { sku: "AO-THUN-DEN-M", qty: 20, importPrice: 102000 },  // Nhập thêm 20 Áo Đen
    { sku: "QUAN-JEAN-32", qty: 10, importPrice: 310000 }    // Nhập thêm 10 Quần Jean, giá tăng
];

// Chạy hàm xử lý
createPurchaseOrder("Công ty May Mặc ABC", "26/12/2025", mockImportData);

// In trạng thái kho sau khi nhập để kiểm tra kết quả cuối cùng
console.log("📊 TRẠNG THÁI KHO SAU KHI TEST (Đã cộng tồn & Cập nhật giá):");
console.table(inventory);
