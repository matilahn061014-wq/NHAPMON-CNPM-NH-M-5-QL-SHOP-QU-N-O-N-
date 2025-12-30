// [I. DANH MỤC SẢN PHẨM TRONG KHO] - Dữ liệu ban đầu
let inventory = [
    { maSP: "SP001", ten: "Áo Sơ Mi Lụa", phanLoai: "Áo", size: "S", gia: 250000, ton: 42 },
    { maSP: "SP002", ten: "Áo Sơ Mi Lụa", phanLoai: "Áo", size: "M", gia: 250000, ton: 35 },
    { maSP: "SP010", ten: "Quần Tây Công Sở", phanLoai: "Quần", size: "L", gia: 350000, ton: 22 }
];

/**
 * Hàm thêm sản phẩm mới
 * Đáp ứng các tiêu chí: Tên, Danh mục, Giá, Số lượng, Chất liệu, Size, Màu sắc
 */
function addProduct(ten, phanLoai, gia, ton, chatLieu, size, mauSac) {
    console.log("\n--- ĐANG XỬ LÝ THÊM SẢN PHẨM MỚI ---");

    // 1. Kiểm tra dữ liệu bắt buộc (Checklist Task 2)
    if (!ten || !phanLoai || !gia || ton === undefined || !size || !mauSac) {
        console.log("❌ LỖI: Thiếu thông tin bắt buộc!");
        return;
    }

    // 2. Kiểm tra tính hợp lệ (Giá và Số lượng phải dương)
    if (gia <= 0 || ton < 0) {
        console.log("❌ LỖI: Giá bán (>0) và Số lượng (>=0) không hợp lệ!");
        return;
    }

    // 3. Tự động tạo mã sản phẩm mới dựa trên danh sách cũ
    const lastID = inventory[inventory.length - 1].maSP;
    const nextNumber = parseInt(lastID.replace("SP", "")) + 1;
    const newMaSP = "SP" + nextNumber.toString().padStart(3, '0');

    // 4. Tạo đối tượng sản phẩm mới
    const newProduct = {
        maSP: newMaSP,
        ten: ten,
        phanLoai: phanLoai,
        size: size,
        gia: gia,
        ton: ton,
        chatLieu: chatLieu, // Thông tin bổ sung
        mauSac: mauSac     // Thông tin bổ sung
    };

    // 5. Lưu vào hệ thống
    inventory.push(newProduct);
    console.log(`✅ THÀNH CÔNG: Đã thêm sản phẩm [${newMaSP} - ${ten}]`);
}

// --- THỰC THI CHẠY THỬ TRÊN TERMINAL ---

// Thử thêm 1 sản phẩm đúng yêu cầu
addProduct("Váy Midi Voan", "Váy", 290000, 15, "Voan", "Fre", "Hoa nhí");

// Thử thêm 1 sản phẩm thiếu thông tin (để test lỗi)
addProduct("", "Áo", 100000, 10, "Cotton", "L", "Xanh");

// Hiển thị danh sách sau khi thêm (Tiêu chí: Hiển thị trong danh sách sản phẩm)
console.log("\n[DANH SÁCH SẢN PHẨM HIỆN TẠI TRONG KHO]");
console.table(inventory);
