class ReturnService {
    constructor() {
        this.inventory = { "SP01": 50, "SP02": 30 };
        this.returnRequests = [];
    }

    processReturn(orderId, type, reason) {
        const request = {
            requestId: "RQ" + Math.floor(Math.random() * 1000),
            orderId: orderId,
            type: type, // "Return" hoặc "Exchange"
            reason: reason,
            status: "Success"
        };
        this.returnRequests.push(request);
        return { success: true, data: request };
    }

    showSummary() {
        console.log("--- DANH SÁCH YÊU CẦU ĐỔI TRẢ ---");
        console.table(this.returnRequests);
        console.log("--- KHO HÀNG HIỆN TẠI ---");
        console.table(this.inventory);
    }
}

const service = new ReturnService();
service.processReturn("DH001", "Return", "Sản phẩm bị lỗi");
service.showSummary();