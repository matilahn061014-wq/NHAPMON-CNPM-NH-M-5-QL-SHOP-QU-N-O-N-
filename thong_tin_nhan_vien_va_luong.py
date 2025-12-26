import os
from datetime import datetime

class EmployeeManager:
    def __init__(self, emp_file, history_file):
        self.emp_file = emp_file
        self.history_file = history_file

    def save_employee(self, id, name, phone, position, base_salary, commission):
        if not all([id, name, phone, position, base_salary, commission]):
            print("❌ Lỗi: Vui lòng nhập đầy đủ thông tin nhân viên!")
            return

        try:
            salary_val = float(base_salary)
            comm_val = float(commission)
        except ValueError:
            print("❌ Lỗi: Lương và hoa hồng phải là số!")
            return

        new_data = f"{id}|{name}|{phone}|{position}|{salary_val}|{comm_val}\n"
        
        with open(self.emp_file, 'a', encoding='utf-8') as f:
            f.write(new_data)
        
        self.log_history(id, f"Khởi tạo: Lương {salary_val}, Vị trí {position}")
        print(f"✅ Đã lưu thông tin nhân viên {name} (AC1, AC2).")

    def log_history(self, emp_id, action):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_entry = f"{timestamp}|{emp_id}|{action}\n"
        with open(self.history_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def update_salary_position(self, emp_id, new_position=None, new_salary=None):
        employees = []
        updated = False
        
        if not os.path.exists(self.emp_file): return

        with open(self.emp_file, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip().split('|')
                if data[0] == emp_id:
                    if new_position: data[3] = new_position
                    if new_salary: data[4] = str(new_salary)
                    updated = True
                    self.log_history(emp_id, f"Cập nhật: Vị trí mới {new_position}, Lương mới {new_salary}")
                employees.append("|".join(data))

        if updated:
            with open(self.emp_file, 'w', encoding='utf-8') as f:
                for emp in employees:
                    f.write(emp + "\n")
            print(f"✅ Đã cập nhật lịch sử thay đổi cho nhân viên {emp_id} (Công việc con 3).")

if _name_ == "_main_":
    manager = EmployeeManager('nhanvien.txt', 'lichsu_luong.txt')

    manager.save_employee("NV01", "Nguyen Van A", "0901234567", "Ban hang", "5000000", "0.05")
    
    manager.update_salary_position("NV01", new_position="Quan ly", new_salary=7000000)