// 1. DỮ LIỆU ĐƯỢC TRÍCH XUẤT TỪ HỆ THỐNG NHÓM 5
let inventory = [
    { ma: "SP001", ten: "Áo Sơ Mi Lụa", loai: "Áo", size: "S", gia: 250000, ton: 42 },
    { ma: "SP002", ten: "Áo Sơ Mi Lụa", loai: "Áo", size: "M", gia: 250000, ton: 35 },
    { ma: "SP003", ten: "Chân Váy Chữ A", loai: "Váy", size: "S", gia: 320000, ton: 20 },
    { ma: "SP004", ten: "Chân Váy Chữ A", loai: "Váy", size: "M", gia: 320000, ton: 18 },
    { ma: "SP005", ten: "Đầm Hoa Nhí Dáng Dài", loai: "Đầm", size: "L", gia: 450000, ton: 12 },
    { ma: "SP006", ten: "Quần Jean Baggy", loai: "Quần", size: "M", gia: 380000, ton: 25 },
    { ma: "SP007", ten: "Áo Thun Basic", loai: "Áo", size: "S", gia: 150000, ton: 100 },
    { ma: "SP008", ten: "Áo Khoác Blazer", loai: "Khoác", size: "M", gia: 650000, ton: 8 },
    { ma: "SP009", ten: "Chân Váy Midi", loai: "Váy", size: "Fre", gia: 290000, ton: 15 },
    { ma: "SP010", ten: "Quần Tây Công Sở", loai: "Quần", size: "L", gia: 350000, ton: 22 }
];

/**
 * HÀM SỬA THÔNG TIN SẢN PHẨM
 * @param {string} targetId - Mã SP cần sửa (ví dụ: "SP001")
 * @param {object} updates - Các trường cần thay đổi
 */
function editProduct(targetId, updates) {
    // Tìm sản phẩm theo mã (AC1: Hiển thị đúng thông tin)
    const product = inventory.find(p => p.ma === targetId);

    if (!product) {
        console.log(`❌ Không tìm thấy sản phẩm mã ${targetId}`);
        return;
    }

    console.log(`\n--- THÔNG TIN TRƯỚC KHI SỬA ---`);
    console.log(`${product.ma} | ${product.ten} | Giá: ${product.gia} | Tồn: ${product.ton}`);

    // Kiểm tra dữ liệu hợp lệ (AC3)
    if (updates.gia !== undefined && (isNaN(updates.gia) || updates.gia < 0)) {
        console.log("❌ Lỗi: Giá bán không hợp lệ!");
        return;
    }
    if (updates.ton !== undefined && (isNaN(updates.ton) || updates.ton < 0)) {
        console.log("❌ Lỗi: Số lượng tồn kho không hợp lệ!");
        return;
    }

    // Cập nhật thông tin (AC2)
    product.ten = updates.ten || product.ten;
    product.loai = updates.loai || product.loai;
    product.size = updates.size || product.size;
    product.gia = updates.gia !== undefined ? updates.gia : product.gia;
    product.ton = updates.ton !== undefined ? updates.ton : product.ton;

    console.log(`✅ Đã cập nhật sản phẩm ${targetId} thành công!`);
}

// --- TEST CHƯƠNG TRÌNH ---

// Ví dụ: Sửa Giá và Tên của SP001
editProduct("SP001", { 
    ten: "Áo Sơ Mi Lụa Cao Cấp", 
    gia: 275000 
});

// Ví dụ: Sửa số lượng tồn của SP008
editProduct("SP008", { 
    ton: 15 
});

// Hiển thị lại bảng dữ liệu sau khi sửa
console.log("\n--- DANH MỤC SAU KHI CẬP NHẬT ---");
console.table(inventory);