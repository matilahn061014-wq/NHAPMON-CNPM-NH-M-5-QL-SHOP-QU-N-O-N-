/**
 * US18: Báo cáo Top Sản phẩm Bán chạy
 * @param {Object} options - Các tham số cấu hình báo cáo
 */
function generateTopSellingReport({
    data = [],           // Dữ liệu bán hàng đầu vào
    topN = 10,           // Tiêu chí 1: Số lượng Top N hiển thị (Mặc định 10)
    timeRange = null,    // Tiêu chí 2: Khoảng thời gian { start, end }
    byVariant = false    // Tiêu chí 3: Phân tích chi tiết theo (Màu/Kích cỡ)
}) {
    
    // --- Bước 1: Lọc dữ liệu theo khoảng thời gian tùy chọn ---
    let processedData = data;
    if (timeRange && timeRange.start && timeRange.end) {
        const startDate = new Date(timeRange.start);
        const endDate = new Date(timeRange.end);
        
        processedData = data.filter(item => {
            const saleDate = new Date(item.date);
            return saleDate >= startDate && saleDate <= endDate;
        });
    }

    // --- Bước 2: Gom nhóm & Tính tổng số lượng bán được ---
    const summaryMap = processedData.reduce((acc, item) => {
        // Tạo khóa định danh: Nếu byVariant = true thì gộp theo Tên + Màu/Size
        const key = byVariant 
            ? `${item.productName} - ${item.variant}` 
            : item.productName;

        if (!acc[key]) {
            acc[key] = {
                label: key,
                totalSold: 0,
                originalName: item.productName,
                variant: item.variant || null
            };
        }
        acc[key].totalSold += item.quantity;
        return acc;
    }, {});

    // --- Bước 3: Sắp xếp giảm dần và lấy Top N ---
    const reportResult = Object.values(summaryMap)
        .sort((a, b) => b.totalSold - a.totalSold) // Cao nhất lên đầu
        .slice(0, topN); // Giới hạn số lượng N

    return reportResult;
}
console.log("File đang chạy OK")
const sampleData = [
  { productName: "Áo thun", quantity: 5, variant: "M" },
  { productName: "Áo thun", quantity: 3, variant: "L" },
  { productName: "Quần jean", quantity: 7, variant: "32" }
];

console.log(generateTopSellingReport({
  data: sampleData,
  topN: 5,
  byVariant: false
}));