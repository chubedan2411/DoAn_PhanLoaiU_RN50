import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class ChinhSuaKhachHangWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Thiết lập các thuộc tính của cửa sổ
        self.setWindowTitle('Chỉnh Sửa Thông Tin Khách Hàng')
        self.setGeometry(100, 100, 300, 250)

        # Tạo layout chính
        self.layout = QVBoxLayout()

        # Tạo các widget
        self.id_label = QLabel('ID Khách Hàng:')
        self.id_input = QLineEdit()

        self.ten_label = QLabel('Tên:')
        self.ten_input = QLineEdit()

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()

        self.sdt_label = QLabel('Số điện thoại:')
        self.sdt_input = QLineEdit()

        self.chinh_sua_button = QPushButton('Chỉnh Sửa Thông Tin')
        self.chinh_sua_button.clicked.connect(self.chinh_sua_khach_hang)

        # Thêm các widget vào layout
        self.layout.addWidget(self.id_label)
        self.layout.addWidget(self.id_input)

        self.layout.addWidget(self.ten_label)
        self.layout.addWidget(self.ten_input)

        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)

        self.layout.addWidget(self.sdt_label)
        self.layout.addWidget(self.sdt_input)

        self.layout.addWidget(self.chinh_sua_button)

        # Đặt layout cho cửa sổ
        self.setLayout(self.layout)

    def chinh_sua_khach_hang(self):
        khach_hang_id = self.id_input.text()
        ten = self.ten_input.text()
        email = self.email_input.text()
        sdt = self.sdt_input.text()

        # Ở đây bạn có thể thực hiện chỉnh sửa thông tin khách hàng trong cơ sở dữ liệu hoặc danh sách của mình
        print(f'Đã chỉnh sửa khách hàng với ID: {khach_hang_id}')
        print(f'Tên mới: {ten}')
        print(f'Email mới: {email}')
        print(f'Số điện thoại mới: {sdt}')

        # Xóa các trường nhập liệu sau khi chỉnh sửa
        self.id_input.clear()
        self.ten_input.clear()
        self.email_input.clear()
        self.sdt_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChinhSuaKhachHangWindow()
    window.show()
    sys.exit(app.exec_())

