class EmployeeAccount:
    def __init__(self, username, password, role):
        if not username or not password:
            raise ValueError("Tên đăng nhập và mật khẩu là bắt buộc")

        self.username = username
        self.password = password
        self.role = role              # admin | ban_hang | kho
        self.is_active = True          # True: hoạt động, False: bị khóa

    def lock(self):
        self.is_active = False

    def unlock(self):
        self.is_active = True


class AccountManager:
    def __init__(self):
        self.accounts = {}

    def is_admin(self, current_user):
        return current_user.role == "admin"

    def create_account(self, current_user, username, password, role):
        if not self.is_admin(current_user):
            raise PermissionError("Chỉ quản trị viên mới được tạo tài khoản")

        if role not in ["admin", "ban_hang", "kho"]:
            raise ValueError("Vai trò không hợp lệ")

        if username in self.accounts:
            raise ValueError("Tên đăng nhập đã tồn tại")

        self.accounts[username] = EmployeeAccount(username, password, role)
        print(f"Đã tạo tài khoản cho {username} với vai trò {role}")

    def lock_account(self, current_user, username):
        if not self.is_admin(current_user):
            raise PermissionError("Chỉ quản trị viên mới được khóa tài khoản")

        self.accounts[username].lock()
        print(f"Tài khoản {username} đã bị khóa")

    def unlock_account(self, current_user, username):
        if not self.is_admin(current_user):
            raise PermissionError("Chỉ quản trị viên mới được mở khóa tài khoản")

        self.accounts[username].unlock()
        print(f"Tài khoản {username} đã được mở khóa")

    def change_role(self, current_user, username, new_role):
        if not self.is_admin(current_user):
            raise PermissionError("Chỉ quản trị viên mới được đổi vai trò")

        self.accounts[username].role = new_role
        print(f"Đã đổi vai trò của {username} thành {new_role}")
