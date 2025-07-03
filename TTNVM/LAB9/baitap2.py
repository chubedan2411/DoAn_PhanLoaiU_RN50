import tkinter as tk
from tkinter import messagebox
import random
# Tạo một số ngẫu nhiên
secret_number = random.randint(1, 100)
attempts = 0
# Hàm kiểm tra dự đoán của người dùng
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        if guess < secret_number:
            result_label.config(text="Số bạn đoán quá nhỏ!")
        elif guess > secret_number:
            result_label.config(text="Số bạn đoán quá lớn!")
        else:
            result_label.config(text=f"Chúc mừng! Bạn đã đoán đúng số {secret_number} sau {attempts} lần.")
            messagebox.showinfo("Chiến thắng!", f"Bạn đã đoán đúng số {secret_number} sau {attempts} lần.")
            reset_game()
    except ValueError:
        messagebox.showwarning("Lỗi", "Vui lòng nhập một số hợp lệ!")
# Hàm để khởi động lại trò chơi
def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, tk.END)
    result_label.config(text="")
# Tạo giao diện người dùng với tkinter
root = tk.Tk()
root.title("Trò chơi Đoán Số")
# Nhãn và hộp nhập liệu
instruction_label = tk.Label(root, text="Tôi đã nghĩ ra một số từ 1 đến 100. Hãy đoán số đó!")
instruction_label.pack(pady=10)
guess_entry = tk.Entry(root, width=10)
guess_entry.pack(pady=5)
# Nút kiểm tra
check_button = tk.Button(root, text="Đoán", command=check_guess)
check_button.pack(pady=10)

# Nhãn kết quả
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
# Khởi động lại trò chơi
reset_button = tk.Button(root, text="Chơi lại", command=reset_game)
reset_button.pack(pady=10)
# Khởi động ứng dụng
root.mainloop()
