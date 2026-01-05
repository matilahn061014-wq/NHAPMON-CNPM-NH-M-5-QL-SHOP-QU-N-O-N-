/**
 * HỆ THỐNG QUẢN LÝ THƯƠNG MẠI ĐIỆN TỬ TỔNG HỢP
 * Bao gồm: US07 (Sửa SP), US12 (Lịch sử chi tiêu), US18 (Báo cáo Top SP)
 */
const EcommerceSystem = {
    // Dữ liệu mẫu giả lập
    db: {
        products: [
            { id: 101, name: "Áo Thun", variant: "M/Trắng", price: 200000 },
            { id: 102, name: "Quần Jean", variant: "32/Xanh", price: 500000 }
        ],

        sales: [
            {
                id: 1,
                productId: 101,
                name: "Áo Thun",
                variant: "M/Trắng",
                quantity: 50,
                date: "2024-03-01",
                customerId: "KH01"
            },
            {
                id: 2,
                productId: 101,
                name: "Áo Thun",
                variant: "L/Đen",
                quantity: 30,
                date: "2024-03-15",
                customerId: "KH01"
            },
            {
                id: 3,
                productId: 102,
                name: "Quần Jean",
                variant: "32/Xanh",
                quantity: 10,
                date: "2024-03-20",
                customerId: "KH02"
            }
        ],

        loyaltyRate: 0.01 // 1% tích điểm
    },

    // ==========================================
    // US07: SỬA SẢN PHẨM
    // ==========================================
    productModule: {
        // 1. Hiển thị đúng thông tin sản phẩm (AC1)
        loadToForm(productId) {
            const product = EcommerceSystem.db.products.find(
                p => p.id === productId
            );

            return product ? { ...product } : null;
        },

        // 2 & 3. Kiểm tra dữ liệu và Lưu (AC2, AC3)
        saveUpdate(productId, newData) {
            if (!newData.name || newData.price <= 0) {
                return {
                    success: false,
                    message: "Dữ liệu không hợp lệ! (AC3)"
                };
            }

            const index = EcommerceSystem.db.products.findIndex(
                p => p.id === productId
            );

            if (index !== -1) {
                EcommerceSystem.db.products[index] = {
                    ...EcommerceSystem.db.products[index],
                    ...newData
                };

                return {
                    success: true,
                    message: "Lưu thành công (AC2)"
                };
            }
        },

        // 4. Hủy sửa (AC4)
        cancel() {
            return "Đã hủy, không thay đổi dữ liệu.";
        }
    },

    // ==========================================
    // US12: LỊCH SỬ CHI TIÊU
    // ==========================================
    customerModule: {
        getCustomerHistory(customerId) {
            // 1. Hiển thị danh sách đơn hàng đã mua
            const orders = EcommerceSystem.db.sales.filter(
                s => s.customerId === customerId
            );

            // 2. Tính toán tổng chi tiêu lũy kế
            // (Giả định giá cố định)
            const totalSpent = orders.reduce(
                (sum, item) => sum + item.quantity * 200000,
                0
            );

            // 3. Tính điểm tích lũy
            const points = Math.floor(
                totalSpent * EcommerceSystem.db.loyaltyRate
            );

            return { orders, totalSpent, points };
        }
    },

    // ==========================================
    // US18: TOP SẢN PHẨM BÁN CHẠY
    // ==========================================
    reportModule: {
        getTopSelling({ topN = 10, startDate, endDate, byVariant = false }) {
            let data = EcommerceSystem.db.sales;

            // 1. Lọc theo thời gian (AC2)
            if (startDate && endDate) {
                data = data.filter(
                    item =>
                        item.date >= startDate &&
                        item.date <= endDate
                );
            }

            // 2. Gom nhóm theo Tên hoặc Phiên bản (AC3)
            const summary = data.reduce((acc, item) => {
                const key = byVariant
                    ? `${item.name} (${item.variant})`
                    : item.name;

                acc[key] = (acc[key] || 0) + item.quantity;
                return acc;
            }, {});

            // 3. Sắp xếp và lấy Top N (AC1)
            return Object.entries(summary)
                .map(([name, qty]) => ({
                    name,
                    quantity: qty
                }))
                .sort((a, b) => b.quantity - a.quantity)
                .slice(0, topN);
        }
    }
};

// ===== DEMO CHẠY THỬ =====

// US07: Sửa sản phẩm
console.log("US07 - Load sản phẩm:");
console.log(
    EcommerceSystem.productModule.loadToForm(101)
);

console.log("US07 - Lưu cập nhật:");
console.log(
    EcommerceSystem.productModule.saveUpdate(101, {
        name: "Áo Thun Cao Cấp",
        price: 250000
    })
);

// US12: Lịch sử chi tiêu
console.log("\nUS12 - Lịch sử chi tiêu KH01:");
console.log(
    EcommerceSystem.customerModule.getCustomerHistory("KH01")
);

// US18: Top sản phẩm bán chạy
console.log("\nUS18 - Top sản phẩm bán chạy:");
console.log(
    EcommerceSystem.reportModule.getTopSelling({
        topN: 3,
        byVariant: true
    })
);
