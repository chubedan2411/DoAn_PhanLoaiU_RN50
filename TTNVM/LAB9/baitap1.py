import tkinter as tk
from tkinter import scrolledtext
# Tạo chatbot đơn giản với các câu trả lời cố định
def chatbot_response(user_input):
    user_input = user_input.lower()    
    # Các câu trả lời dựa trên từ khóa
    responses = {
        "xin chào": "Chào bạn! Tôi có thể giúp gì cho bạn?",
        "bạn tên gì": "Tôi là chatbot đơn giản được tạo bằng Python.",
        "bạn làm gì": "Tôi đang trò chuyện với bạn.",
        "tạm biệt": "Tạm biệt! Hẹn gặp lại bạn sau.",
    }
    # Trả lời nếu tìm thấy từ khóa, nếu không trả lời mặc định
    for key in responses:
        if key in user_input:
            return responses[key]    
    return "Xin lỗi, tôi không hiểu câu hỏi của bạn."
# Hàm để hiển thị cuộc trò chuyện
def display_chat():
    user_input = user_entry.get()
    chat_area.insert(tk.END, "Bạn: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_area.insert(tk.END, "Chatbot: " + response + "\n\n")
    user_entry.delete(0, tk.END)
# Tạo giao diện người dùng với tkinter
root = tk.Tk()
root.title("Chatbot Đơn Giản")
# Khu vực hiển thị cuộc trò chuyện
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_area.pack(pady=10)
# Hộp nhập liệu cho người dùng
user_entry = tk.Entry(root, width=40)
user_entry.pack(pady=10)
# Nút gửi
send_button = tk.Button(root, text="Gửi", command=display_chat)
send_button.pack()
# Khởi động ứng dụng
root.mainloop()
