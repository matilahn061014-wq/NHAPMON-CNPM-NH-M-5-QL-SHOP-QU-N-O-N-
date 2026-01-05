/**
 * Hệ thống Quản lý Tài khoản và Phân quyền Nhân viên
 */
class AuthSystem {
    constructor() {
        this.users = []; // Danh sách lưu trữ tài khoản
        this.roles = ['Quản trị viên', 'Bán hàng', 'Kho'];
    }

    // 1 & 2. Tạo tài khoản với Tên, Mật khẩu và Vai trò
    createUser(executor, username, password, role) {
        // 3. Tiêu chí chấp nhận: Chỉ Admin mới có quyền tạo
        if (!executor || executor.role !== 'Quản trị viên') {
            throw new Error(`[Từ chối]: Chỉ Quản trị viên mới có thể tạo tài khoản.`);
        }

        // Kiểm tra dữ liệu đầu vào (Tiêu chí 1 & 2)
        if (!username || !password || !role) {
            throw new Error("[Lỗi]: Thiếu Tên đăng nhập, Mật khẩu hoặc Vai trò.");
        }

        if (!this.roles.includes(role)) {
            throw new Error(`[Lỗi]: Vai trò '${role}' không hợp lệ.`);
        }

        const newUser = {
            id: this.users.length + 1,
            username: username,
            password: password, // Trong thực tế cần băm (hash) mật khẩu
            role: role,
            isActive: true
        };

        this.users.push(newUser);
        console.log(`[Thành công]: Đã tạo tài khoản '${username}' với vai trò '${role}'.`);
        return newUser;
    }

    // 3. Chức năng khóa/mở khóa tài khoản
    toggleAccountStatus(executor, targetUsername) {
        if (!executor || executor.role !== 'Quản trị viên') {
            throw new Error(`[Từ chối]: Chỉ Quản trị viên mới có quyền khóa/mở khóa.`);
        }

        const user = this.users.find(u => u.username === targetUsername);
        if (!user) throw new Error("[Lỗi]: Không tìm thấy nhân viên.");

        user.isActive = !user.isActive;
        const status = user.isActive ? "Mở khóa" : "Khóa";
        console.log(`[Trạng thái]: Tài khoản '${targetUsername}' đã được ${status}.`);
        return user;
    }
}

// --- KỊCH BẢN KIỂM THỬ (TEST CASES) ---

const system = new AuthSystem();

// Khởi tạo một Admin mặc định để vận hành hệ thống
const rootAdmin = { username: 'admin_root', role: 'Quản trị viên' };

console.log("--- BẮT ĐẦU TEST HỆ THỐNG QUẢN LÝ ---");

try {
    // Test 1: Tạo tài khoản hợp lệ (Đáp ứng TC 1 & 2)
    console.log("\n1. Kiểm tra tạo tài khoản:");
    const staff1 = system.createUser(rootAdmin, "nhanvien_banhang", "123456", "Bán hàng");
    const staff2 = system.createUser(rootAdmin, "nhanvien_kho", "abc@123", "Kho");

    // Test 2: Kiểm tra phân quyền (Tiêu chí 3)
    console.log("\n2. Kiểm tra bảo mật (Nhân viên thường không được tạo tài khoản):");
    try {
        system.createUser(staff1, "hacker_user", "123", "Quản trị viên");
    } catch (e) {
        console.error(e.message); // Mong đợi: Bị từ chối
    }

    // Test 3: Khóa tài khoản
    console.log("\n3. Kiểm tra chức năng Khóa tài khoản:");
    system.toggleAccountStatus(rootAdmin, "nhanvien_kho");
    console.log("Dữ liệu hiện tại:", system.users.map(u => ({ user: u.username, active: u.isActive })));

} catch (error) {
    console.error("Lỗi không xác định:", error.message);
}

console.log("\n--- KẾT THÚC TEST ---");