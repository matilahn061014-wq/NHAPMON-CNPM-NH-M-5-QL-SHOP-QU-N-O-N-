from datetime import datetime
class SalaryHistory:
    """
    Lưu lịch sử thay đổi lương và vị trí
    """
    def __init__(self, old_salary, new_salary, old_position, new_position):
        self.old_salary = old_salary
        self.new_salary = new_salary
        self.old_position = old_position
        self.new_position = new_position
        self.changed_at = datetime.now()


class Employee:
    """
    Nhân viên:
    - Họ tên
    - SĐT
    - Vị trí
    - Lương cơ bản
    - Tỷ lệ hoa hồng
    """

    def __init__(self, emp_id, name, phone, position, base_salary, commission_rate=0):
        self.emp_id = emp_id
        self.name = name
        self.phone = phone
        self.position = position
        self.base_salary = base_salary
        self.commission_rate = commission_rate
        self.salary_history = []

    def update_salary_and_position(self, new_salary, new_position):
        """
        Cập nhật lương/vị trí và lưu lịch sử
        """
        history = SalaryHistory(
            old_salary=self.base_salary,
            new_salary=new_salary,
            old_position=self.position,
            new_position=new_position
        )

        self.salary_history.append(history)
        self.base_salary = new_salary
        self.position = new_position
