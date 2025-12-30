/**
 * Hệ thống Báo cáo Doanh thu Thuần (Net Sales)
 */
class SalesReportSystem {
    constructor() {
        // Giả lập dữ liệu giao dịch trong 30 ngày qua
        this.transactions = this.generateMockData();
    }

    // Tạo dữ liệu mẫu để test
    generateMockData() {
        const data = [];
        const today = new Date();
        for (let i = 0; i < 30; i++) {
            const date = new Date();
            date.setDate(today.getDate() - i);
            data.push({
                date: date.toISOString().split('T')[0],
                grossSales: Math.floor(Math.random() * 5000000) + 2000000,
                discounts: Math.floor(Math.random() * 500000),
                returns: Math.floor(Math.random() * 200000)
            });
        }
        return data;
    }

    // Công việc con 1 & 2: Tính toán doanh thu theo mốc thời gian
    getNetSales(period) {
        const today = new Date().toISOString().split('T')[0];
        const lastWeek = new Date(); lastWeek.setDate(lastWeek.getDate() - 7);
        
        let filteredData = [];

        if (period === 'Hôm nay') {
            filteredData = this.transactions.filter(t => t.date === today);
        } else if (period === 'Tuần này') {
            filteredData = this.transactions.slice(0, 7);
        } else if (period === 'Tháng này') {
            filteredData = this.transactions.slice(0, 30);
        }

        const stats = filteredData.reduce((acc, curr) => {
            acc.totalGross += curr.grossSales;
            acc.totalDiscount += curr.discounts;
            acc.totalReturn += curr.returns;
            return acc;
        }, { totalGross: 0, totalDiscount: 0, totalReturn: 0 });

        const netSales = stats.totalGross - stats.totalDiscount - stats.totalReturn;

        return {
            period: period,
            netSales: netSales,
            details: stats
        };
    }

    // Công việc con 3: Trực quan hóa xu hướng (Mô phỏng biểu đồ bằng text)
    visualizeTrend() {
        console.log("\n--- BIỂU ĐỒ XU HƯỚNG DOANH THU (7 NGÀY QUA) ---");
        const last7Days = this.transactions.slice(0, 7).reverse();
        
        last7Days.forEach(day => {
            const net = day.grossSales - day.discounts - day.returns;
            const barLength = Math.floor(net / 500000);
            const bar = "█".repeat(barLength);
            console.log(`${day.date}: ${bar} | ${net.toLocaleString()}đ`);
        });
    }
}

// --- CHẠY KIỂM THỬ ---

const report = new SalesReportSystem();

console.log("--- BÁO CÁO DOANH THU THUẦN ---");

// Test tiêu chí 1 & 2: Xem theo các mốc thời gian
const periods = ['Hôm nay', 'Tuần này', 'Tháng này'];
const results = periods.map(p => {
    const data = report.getNetSales(p);
    return {
        "Mốc thời gian": data.period,
        "Doanh thu thuần": data.netSales.toLocaleString() + "đ",
        "Tổng giảm giá": data.details.totalDiscount.toLocaleString() + "đ",
        "Tổng hoàn trả": data.details.totalReturn.toLocaleString() + "đ"
    };
});

console.table(results);

// Test tiêu chí 3: Biểu đồ xu hướng
report.visualizeTrend();