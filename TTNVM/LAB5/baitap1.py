import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class ThemKhachHangWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Thiết lập các thuộc tính của cửa sổ
        self.setWindowTitle('Thêm Khách Hàng')
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

        self.them_button = QPushButton('Thêm Khách Hàng')
        self.them_button.clicked.connect(self.them_khach_hang)

        # Thêm các widget vào layout
        self.layout.addWidget(self.ten_label)
        self.layout.addWidget(self.ten_input)

        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)

        self.layout.addWidget(self.sdt_label)
        self.layout.addWidget(self.sdt_input)

        self.layout.addWidget(self.them_button)

        # Đặt layout cho cửa sổ
        self.setLayout(self.layout)

    def them_khach_hang(self):
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()

        # Ở đây bạn có thể thêm khách hàng vào cơ sở dữ liệu hoặc danh sách của mình
        print(f'Đã thêm khách hàng: {ten}, {email}, {sdt}')

        # Xóa các trường nhập liệu sau khi thêm
        self.ten_input.clear()
        self.email_input.clear()
        self.sdt_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ThemKhachHangWindow()
    window.show()
    sys.exit(app.exec_())

