/**
 * US04: Xử lý Giao dịch và Trừ tồn kho
 */

// Giả lập cơ sở dữ liệu
let inventory = {
    "SP001": { name: "Sản phẩm A", stock: 10, price: 100000 },
    "SP002": { name: "Sản phẩm B", stock: 5, price: 200000 }
};

let transactionLogs = [];

const PAYMENT_METHODS = {
    CASH: "Tiền mặt",
    TRANSFER: "Chuyển khoản",
    ATM: "Thẻ ATM",
    MEMBER: "Thẻ thành viên"
};

/**
 * Hàm xử lý thanh toán và cập nhật kho
 * Thỏa mãn yêu cầu 1, 2, 3, 4 trong checklist
 */
async function processTransaction(orderItems, paymentMethod) {
    try {
        console.log("--- Bắt đầu xử lý giao dịch ---");

        // 1. Kiểm tra hình thức thanh toán (Yêu cầu 1)
        if (!Object.values(PAYMENT_METHODS).includes(paymentMethod)) {
            throw new Error(`Phương thức thanh toán ${paymentMethod} không được hỗ trợ.`);
        }

        // 2. Trừ tồn kho tự động (Yêu cầu 2)
        for (const item of orderItems) {
            if (!inventory[item.id] || inventory[item.id].stock < item.quantity) {
                throw new Error(`Sản phẩm ${item.id} không đủ tồn kho!`);
            }
            inventory[item.id].stock -= item.quantity;
            console.log(`> Đã trừ kho: ${inventory[item.id].name} (Còn lại: ${inventory[item.id].stock})`);
        }

        // 3. Lưu trữ thông tin đơn hàng vào sổ giao dịch (Yêu cầu 4)
        const transactionId = `TXN_${Date.now()}`;
        const transactionRecord = {
            id: transactionId,
            items: orderItems,
            paymentMethod: paymentMethod,
            timestamp: new Date().toISOString(),
            status: "Thành công" // Yêu cầu 3: Giao dịch coi là thành công khi đã ghi nhận và trừ kho
        };
        transactionLogs.push(transactionRecord);
        console.log("> Đã ghi sổ giao dịch thành công.");

        // 4. In hóa đơn (Yêu cầu 3 & 4)
        printInvoice(transactionRecord);

        return { success: true, transactionId };

    } catch (error) {
        console.error("!!! Giao dịch thất bại:", error.message);
        return { success: false, message: error.message };
    }
}

/**
 * Hàm in hóa đơn giả lập (Yêu cầu 4)
 */
function printInvoice(txn) {
    console.log("\n--- HÓA ĐƠN BÁN HÀNG ---");
    console.log(`Mã GD: ${txn.id}`);
    console.log(`Ngày: ${txn.timestamp}`);
    console.log(`Thanh toán: ${txn.paymentMethod}`);
    console.log("Chi tiết sản phẩm:");
    txn.items.forEach(i => console.log(` - SP: ${i.id} | SL: ${i.quantity}`));
    console.log("------------------------\n");
}

// --- CHẠY THỬ NGHIỆM ---
const cart = [
    { id: "SP001", quantity: 2 },
    { id: "SP002", quantity: 1 }
];

// Thực hiện thanh toán bằng Chuyển khoản
processTransaction(cart, PAYMENT_METHODS.TRANSFER);
