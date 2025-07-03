import tkinter as tk

def greet():
    name = name_entry.get()
    greeting_label.config(text=f"Xin chào, {name}!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Chào")

# Tạo các thành phần giao diện
name_label = tk.Label(root, text="Nhập tên của bạn:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

greet_button = tk.Button(root, text="Chào!", command=greet)
greet_button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

# Bắt đầu vòng lặp chính
root.mainloop()
