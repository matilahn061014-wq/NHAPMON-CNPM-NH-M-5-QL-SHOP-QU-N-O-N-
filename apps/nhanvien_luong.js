// [IV. QUẢN LÝ NHÂN SỰ & TÀI KHOẢN] - Dữ liệu gốc Nhóm 5
let staffList = [
    { maNV: "ADMIN", ten: "Quản Trị Viên", chucVu: "Chủ shop", luongCB: 15000000 },
    { maNV: "NV001", ten: "Trần Văn Nam", chucVu: "Bán hàng", luongCB: 7500000 },
    { maNV: "NV002", ten: "Nguyễn Mai Chi", chucVu: "Kho vận", luongCB: 8200000 }
];

/**
 * Hàm tính toán lương kèm hoa hồng 5%
 * Đáp ứng yêu cầu quản lý lương của Nhóm 5
 */
function tinhLuongHeThong() {
    console.log("\n=== BẢNG LƯƠNG NHÂN VIÊN (HOA HỒNG 5%) ===");
    
    // Tạo mảng mới đã tính toán lương
    const bangLuong = staffList.map(nv => {
        const hoaHong = nv.luongCB * 0.05;
        const thucNhan = nv.luongCB + hoaHong;
        return {
            "Mã NV": nv.maNV,
            "Họ Tên": nv.ten,
            "Chức Vụ": nv.chucVu,
            "Lương CB": nv.luongCB.toLocaleString() + "đ",
            "Thực Nhận": thucNhan.toLocaleString() + "đ"
        };
    });

    // Hiển thị dạng bảng trên Terminal
    console.table(bangLuong);
}

/**
 * Hàm thêm nhân viên mới (Logic chạy trên Terminal)
 */
function addNV_Terminal(id, name, chucVu, baseSalary) {
    // Kiểm tra dữ liệu hợp lệ
    if (!id || !name || baseSalary <= 0) {
        console.log("❌ Lỗi: Dữ liệu không hợp lệ!");
        return;
    }

    // Thêm vào danh sách
    staffList.push({
        maNV: id.toUpperCase(),
        ten: name,
        chucVu: chucVu,
        luongCB: baseSalary
    });
    
    console.log(`✅ Đã thêm nhân viên: ${name}`);
}

// --- THỰC THI (Thay vì dùng window.onload) ---
addNV_Terminal("NV004", "Phạm Phương Linh", "Bán hàng", 7000000); // Thêm thử 1 người
tinhLuongHeThong(); // In bảng lương ra màn hình
