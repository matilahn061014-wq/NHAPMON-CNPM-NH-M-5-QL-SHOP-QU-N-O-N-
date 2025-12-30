/**
 * 1. DỮ LIỆU MẪU (Giả lập Database đơn hàng)
 * Mỗi bản ghi bao gồm: Mã đơn, Tên nhân viên, Tổng tiền và Ngày bán.
 */
const salesDatabase = [
    { orderId: "HD001", staff: "Nguyễn Thu", total: 450000, date: "2023-10-01" },
    { orderId: "HD002", staff: "Lê Hạnh", total: 280000, date: "2023-10-01" },
    { orderId: "HD003", staff: "Nguyễn Thu", total: 640000, date: "2023-10-02" },
    { orderId: "HD004", staff: "Trần Mai", total: 1200000, date: "2023-10-05" },
    { orderId: "HD005", staff: "Lê Hạnh", total: 150000, date: "2023-10-10" },
    { orderId: "HD006", staff: "Nguyễn Thu", total: 300000, date: "2023-10-12" }
];

/**
 * 2. MODULE XỬ LÝ US15
 */
const PerformanceModule = {

    /**
     * Tiêu chí 1 & 2: Tổng hợp doanh thu/số đơn và Lọc theo thời gian
     * @param {string} fromDate - Định dạng YYYY-MM-DD
     * @param {string} toDate   - Định dạng YYYY-MM-DD
     */
    getSummaryReport: function(fromDate, toDate) {
        return salesDatabase.reduce((acc, order) => {
            // Logic lọc theo ngày (Tiêu chí 2)
            if (fromDate && order.date < fromDate) return acc;
            if (toDate && order.date > toDate) return acc;

            const staffName = order.staff;
            if (!acc[staffName]) {
                acc[staffName] = {
                    "Nhân viên": staffName,
                    "Số đơn hàng": 0,
                    "Tổng doanh thu": 0
                };
            }

            // Tổng hợp dữ liệu (Tiêu chí 1)
            acc[staffName]["Số đơn hàng"] += 1;
            acc[staffName]["Tổng doanh thu"] += order.total;

            return acc;
        }, {});
    },

    /**
     * Tiêu chí 3: Truy cập chi tiết các đơn hàng của một nhân viên
     * @param {string} staffName 
     */
    getStaffDetails: function(staffName) {
        return salesDatabase.filter(order => order.staff === staffName);
    }
};

/**
 * 3. ĐOẠN CODE CHẠY THỬ (TEST CASE)
 */

// --- TEST CASE 1: Xem báo cáo tổng hợp từ ngày 01/10 đến 05/10 ---
console.log("--- 📊 BÁO CÁO TỔNG HỢP HIỆU SUẤT (Từ 01/10 đến 05/10) ---");
const summary = PerformanceModule.getSummaryReport("2023-10-01", "2023-10-05");
console.table(Object.values(summary));

// --- TEST CASE 2: Xem toàn bộ đơn hàng của nhân viên 'Lê Hạnh' ---
console.log("\n--- 🔍 CHI TIẾT CÁC ĐƠN HÀNG CỦA NHÂN VIÊN: 'Lê Hạnh' ---");
const hanhDetails = PerformanceModule.getStaffDetails("Lê Hạnh");
console.table(hanhDetails);

// --- TEST CASE 3: Báo cáo không giới hạn thời gian (Tất cả dữ liệu) ---
console.log("\n--- 📈 TỔNG DOANH THU TẤT CẢ THỜI GIAN ---");
const allTime = PerformanceModule.getSummaryReport(null, null);
console.table(Object.values(allTime));
