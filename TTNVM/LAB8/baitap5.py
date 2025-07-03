def chatbot_response(user_input):
    if "xin chào" in user_input.lower():
        return "Xin chào! Bạn cần gì?"
    elif "tạm biệt" in user_input.lower():
        return "Tạm biệt! Hẹn gặp lại!"
    elif "bạn tên gì" in user_input.lower():
        return "Tôi là Chatbot đơn giản!"
    else:
        return "Xin lỗi, tôi không hiểu câu hỏi của bạn."

def chatbot():
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() == "tạm biệt":
            print("Chatbot: Tạm biệt! Hẹn gặp lại!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()