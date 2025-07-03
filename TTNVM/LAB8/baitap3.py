import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập nhiệm vụ!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhiệm vụ!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("To-do List")

# Tạo các thành phần giao diện
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Thêm nhiệm vụ", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Xóa nhiệm vụ", command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

# Bắt đầu vòng lặp chính
root.mainloop()
