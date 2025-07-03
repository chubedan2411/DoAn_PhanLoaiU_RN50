import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class LuuKhachHangWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Thiết lập các thuộc tính của cửa sổ
        self.setWindowTitle('Lưu Thông Tin Khách Hàng')
        self.setGeometry(100, 100, 300, 200)

        # Tạo layout
        self.layout = QVBoxLayout()

        # Tạo các widget
        self.ten_label = QLabel('Tên:')
        self.ten_input = QLineEdit()

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()

        self.sdt_label = QLabel('Số điện thoại:')
        self.sdt_input = QLineEdit()

        self.luu_button = QPushButton('Lưu Khách Hàng')
        self.luu_button.clicked.connect(self.luu_khach_hang)

        # Thêm các widget vào layout
        self.layout.addWidget(self.ten_label)
        self.layout.addWidget(self.ten_input)

        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)

        self.layout.addWidget(self.sdt_label)
        self.layout.addWidget(self.sdt_input)

        self.layout.addWidget(self.luu_button)

        # Đặt layout cho cửa sổ
        self.setLayout(self.layout)

        # Danh sách lưu thông tin khách hàng
        self.khach_hang_list = []

    def luu_khach_hang(self):
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()

        # Tạo dictionary chứa thông tin khách hàng
        khach_hang = {
            'Tên': ten,
            'Email': email,
            'Số điện thoại': sdt
        }

        # Thêm thông tin khách hàng vào danh sách
        self.khach_hang_list.append(khach_hang)

        # In danh sách khách hàng để kiểm tra
        print('Danh sách khách hàng:', self.khach_hang_list)

        # Xóa các trường nhập liệu sau khi lưu
        self.ten_input.clear()
        self.email_input.clear()
        self.sdt_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LuuKhachHangWindow()
    window.show()
    sys.exit(app.exec_())
