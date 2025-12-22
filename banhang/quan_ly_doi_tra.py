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
