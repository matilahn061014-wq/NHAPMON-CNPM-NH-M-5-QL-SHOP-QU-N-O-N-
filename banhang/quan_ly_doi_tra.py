# Giả định: Có các Models/Database Service đã được định nghĩa
# from app.models import Order, ReturnRequest, Product
# from app.db_service import get_order_by_id, create_return_request

class ReturnService:
    def find_and_start_return(self, order_id: str, staff_id: str) -> dict:
        """
        1. Tìm kiếm đơn hàng theo ID.
        2. Tạo một yêu cầu Đổi/Trả mới liên kết với đơn hàng đó.
        """
        # (1) Tìm kiếm đơn hàng cũ
        order = get_order_by_id(order_id)
        if not order:
            return {"success": False, "message": "Không tìm thấy đơn hàng."}

        # Kiểm tra các điều kiện Đổi/Trả (ví dụ: trong thời hạn cho phép)
        if not order.is_returnable():
             return {"success": False, "message": "Đơn hàng đã quá thời hạn Đổi/Trả."}

        # (2) Tạo yêu cầu Đổi/Trả ban đầu (Draft)
        new_return = create_return_request(
            order_id=order_id,
            status="DRAFT",
            created_by=staff_id
        )

        return {"success": True, "return_request": new_return, "order_details": order.items}
 Giả định: Có hàm cập nhật tồn kho
# from app.inventory_service import update_inventory

    def restock_products(self, return_request_id: str, restock_items: list):
        """
        Cập nhật tồn kho cho các sản phẩm được trả lại.
        restock_items: [{"product_id": "P001", "quantity": 1}]
        """
        return_request = get_return_request_by_id(return_request_id)

        if return_request.status != "ACCEPTED":
             return {"success": False, "message": "Yêu cầu Đổi/Trả chưa được chấp nhận để hoàn kho."}

        for item in restock_items:
            product_id = item["product_id"]
            quantity = item["quantity"]

            # Gọi dịch vụ tồn kho để cộng lại số lượng
            success = update_inventory(product_id, quantity) # Tăng tồn kho
            if not success:
                # Xử lý lỗi nếu không thể cập nhật tồn kho
                print(f"Lỗi hoàn kho cho sản phẩm {product_id}")
                return {"success": False, "message": "Lỗi khi cập nhật tồn kho."}

        # Cập nhật trạng thái yêu cầu Đổi/Trả (ví dụ: "RESTOCKED")
        update_return_request_status(return_request_id, "RESTOCKED")
        
        return {"success": True, "message": "Đã hoàn kho thành công."}
def calculate_refund_or_charge(self, returned_items: list, new_items: list) -> dict:
        """
        Tính toán tổng giá trị sản phẩm được trả và sản phẩm mới được đổi.
        """
        # (1) Tính tổng giá trị sản phẩm trả lại (dựa trên giá lúc mua)
        total_returned_value = 0
        for item in returned_items:
            # Giá bán lẻ tại thời điểm mua hàng
            total_returned_value += item["price_at_sale"] * item["quantity"]

        # (2) Tính tổng giá trị sản phẩm đổi (dựa trên giá hiện tại)
        total_new_value = 0
        for item in new_items:
            # Lấy giá hiện tại hoặc giá khuyến mãi
            current_price = get_product_current_price(item["product_id"])
            total_new_value += current_price * item["quantity"]

        # (3) Tính chênh lệch
        # Chênh lệch dương (> 0): Cần hoàn tiền lại cho khách
        # Chênh lệch âm (< 0): Khách cần trả thêm
        price_difference = total_returned_value - total_new_value

        return {
            "total_returned_value": total_returned_value,
            "total_new_value": total_new_value,
            "difference": price_difference,
            "action": "REFUND" if price_difference > 0 else ("CHARGE" if price_difference < 0 else "NONE")
        }
# Giả định: Có một hàm lưu trữ sự kiện giao dịch
# from app.logging_service import log_transaction

    def finalize_return_transaction(self, return_request_id: str, final_amount: float, action: str):
        """
        Lưu trữ lịch sử giao dịch chi tiết và cập nhật trạng thái cuối cùng.
        """
        # (1) Cập nhật trạng thái cuối cùng của yêu cầu Đổi/Trả
        update_return_request_status(return_request_id, "COMPLETED")
        
        # (2) Lưu trữ lịch sử giao dịch chi tiết
        transaction_log = {
            "return_id": return_request_id,
            "final_amount": abs(final_amount),
            "type": "RETURN_REFUND" if action == "REFUND" else ("RETURN_CHARGE" if action == "CHARGE" else "EXCHANGE_ONLY"),
            "timestamp": datetime.now(),
            "staff_id": current_user.id
        }
        
        log_transaction(transaction_log)

        return {"success": True, "message": "Giao dịch Đổi/Trả đã hoàn tất và được ghi lại."}
