/**
 * US15: Báo cáo và Thống kê Doanh thu
 */
class ReportService {
    constructor(orders) {
        this.orders = orders; // Danh sách đơn hàng từ US02
    }

    // Công việc 1: Tổng hợp doanh thu và số đơn hàng theo nhân viên
    getRevenueByStaff() {
        return this.orders.reduce((report, order) => {
            if (!report[order.staffId]) {
                report[order.staffId] = { totalRevenue: 0, orderCount: 0 };
            }
            report[order.staffId].totalRevenue += order.finalTotal;
            report[order.staffId].orderCount += 1;
            return report;
        }, {});
    }

    // Công việc 2: Lọc báo cáo theo khoảng thời gian (ngày, tháng)
    filterOrdersByDate(startDate, endDate) {
        const start = new Date(startDate);
        const end = new Date(endDate);
        
        return this.orders.filter(order => {
            const orderDate = new Date(order.timestamp);
            return orderDate >= start && orderDate <= end;
        });
    }

    // Công việc 3: Hiển thị chi tiết các đơn hàng của một nhân viên
    getStaffDetailReport(staffId) {
        const staffOrders = this.orders.filter(order => order.staffId === staffId);
        return {
            staffId: staffId,
            orders: staffOrders,
            summary: staffOrders.reduce((acc, curr) => acc + curr.finalTotal, 0)
        };
    }
}
// Tạo dữ liệu mẫu để chạy thử
const mockOrders = [
    { staffId: "NV01", finalTotal: 100, timestamp: "2023-10-01" },
    { staffId: "NV01", finalTotal: 200, timestamp: "2023-10-02" },
    { staffId: "NV02", finalTotal: 150, timestamp: "2023-10-01" }
];

// Khởi tạo class
const service = new ReportService(mockOrders);

// Gọi hàm và in kết quả ra Terminal
console.log("--- Báo cáo theo nhân viên ---");
console.log(service.getRevenueByStaff());

// 2. Chạy thử hàm tính doanh thu theo nhân viên và in ra màn hình
const report = service.getRevenueByStaff();
console.log("KẾT QUẢ BÁO CÁO:");
console.table(report); // Dùng console.table nhìn cho đẹp
console.log("--- Kết quả báo cáo ---");
console.table(service.getRevenueByStaff()); // Dùng console.table để xem dạng bảng cho đẹp
