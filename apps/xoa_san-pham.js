**
 * Chức năng: US07 - Xóa sản phẩm
 * Gộp: Công việc con (1-5) & Tiêu chí chấp nhận (1-4)
 */

async function deleteProduct(productId) {
    // --- TIÊU CHÍ 1: Chỉ người có quyền mới được xóa ---
    const userRole = "admin"; // Giả sử lấy từ hệ thống
    if (userRole !== "admin") {
        alert("Thất bại: Bạn không có quyền xóa sản phẩm!"); // TIÊU CHÍ 4
        return;
    }

    // --- CÔNG VIỆC CON 1: (Đã hiển thị nút xóa trên UI để kích hoạt hàm này) ---

    // --- CÔNG VIỆC CON 2 & TIÊU CHÍ 2: Có hộp thoại xác nhận xóa ---
    const confirmDelete = confirm("Bạn có chắc chắn muốn xóa sản phẩm này không?");
    
    if (confirmDelete) {
        try {
            // --- CÔNG VIỆC CON 3: Thực hiện xóa dữ liệu (Gọi API) ---
            console.log(Đang xóa sản phẩm ID: ${productId}...);
            
            // Giả lập gọi API server
            const response = await fakeApiDeleteCall(productId); 

            if (response.success) {
                // --- CÔNG VIỆC CON 4 & TIÊU CHÍ 3: Cập nhật danh sách & Không còn hiển thị ---
                removeProductFromUI(productId); 

                // --- CÔNG VIỆC CON 5 & TIÊU CHÍ 4: Thông báo thành công ---
                alert("Chúc mừng: Sản phẩm đã được xóa thành công!");
            } else {
                throw new Error("Lỗi từ server");
            }

        } catch (error) {
            // --- CÔNG VIỆC CON 5 & TIÊU CHÍ 4: Thông báo thất bại ---
            alert("Thất bại: Không thể xóa sản phẩm. Vui lòng thử lại.");
        }
    }
}

// --- CÁC HÀM PHỤ TRỢ MÔ PHỎNG ---

function removeProductFromUI(id) {
    // Logic để xóa element khỏi DOM hoặc cập nhật State (React/Vue)
    const element = document.getElementById(product-${id});
    if (element) element.remove(); 
    console.log("Tiêu chí 3: Sản phẩm không còn hiển thị trên màn hình.");
}

function fakeApiDeleteCall(id) {
    return new Promise((resolve) => {
        setTimeout(() => resolve({ success: true }), 500);
    });
}
