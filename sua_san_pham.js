/**
 * US07: Logic Sửa sản phẩm
 */
class ProductManager {
    constructor() {
        // Dữ liệu mẫu (DB giả lập)
        this.products = [
            { id: 1, name: "Giày Sneaker", price: 500000, stock: 10 }
        ];
    }

    // 1. Hiển thị form sửa với thông tin sản phẩm
    // (Công việc con 1 & Tiêu chí 1)
    displayEditForm(productId) {
        const product = this.products.find(p => p.id === productId);

        if (!product) {
            console.error("Không tìm thấy sản phẩm!");
            return;
        }

        console.log("--- Form Chỉnh Sửa ---");
        console.log(Tên: ${product.name});
        console.log(Giá: ${product.price});

        // Ở thực tế, bạn sẽ gán giá trị này vào input.value
        return product;
    }

    // 2. Kiểm tra dữ liệu và Lưu
    // (Công việc con 2, 3 & Tiêu chí 2, 3)
    updateProduct(productId, newData) {
        // Kiểm tra dữ liệu hợp lệ (Tiêu chí 3)
        if (!newData.name || newData.price <= 0) {
            this.notify(
                "Dữ liệu không hợp lệ! Vui lòng kiểm tra lại.",
                "error"
            );
            return false;
        }

        // Tìm và cập nhật
        const index = this.products.findIndex(p => p.id === productId);

        if (index !== -1) {
            this.products[index] = {
                ...this.products[index],
                ...newData
            };

            this.notify("Cập nhật thông tin thành công!", "success");
            return true;
        }

        this.notify("Không tìm thấy sản phẩm!", "error");
        return false;
    }

    // 3. Thông báo kết quả (Công việc con 4)
    notify(message, type) {
        console.log(
            [THÔNG BÁO - ${type.toUpperCase()}]: ${message}
        );
    }

    // 4. Hủy sửa (Tiêu chí 4)
    cancelEdit() {
        console.log("Đã hủy chỉnh sửa. Dữ liệu được giữ nguyên.");
        // Thực tế: Đóng modal hoặc quay lại trang danh sách
    }
}

// --- THỰC THI GIẢ LẬP ---
const manager = new ProductManager();

// Bước 1: Người dùng nhấn nút sửa
const currentProduct = manager.displayEditForm(1);

// Bước 2: Người dùng nhập liệu mới và Lưu
const updatedData = {
    name: "Giày Sneaker Cao Cấp",
    price: 750000
};
manager.updateProduct(1, updatedData);

// Hoặc Bước 2: Người dùng nhập sai giá
manager.updateProduct(1, { name: "Lỗi", price: -100 });

// Hoặc Bước 2: Người dùng nhấn Hủy
manager.cancelEdit();
