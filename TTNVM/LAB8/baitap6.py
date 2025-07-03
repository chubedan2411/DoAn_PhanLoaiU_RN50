import speech_recognition as sr

def recognize_speech():
    # Tạo một Recognizer để nhận diện giọng nói
    recognizer = sr.Recognizer()

    # Sử dụng micro làm nguồn âm thanh
    with sr.Microphone() as source:
        print("Xin mời bạn nói...")
        # Điều chỉnh âm lượng của micro để nhận diện tốt hơn
        recognizer.adjust_for_ambient_noise(source)
        # Nghe và ghi âm
        audio = recognizer.listen(source)

        try:
            # Sử dụng Google Web Speech API để chuyển đổi giọng nói thành văn bản
            text = recognizer.recognize_google(audio, language="vi-VN")
            print(f"Bạn đã nói: {text}")
        except sr.UnknownValueError:
            print("Xin lỗi, tôi không thể nhận diện được âm thanh.")
        except sr.RequestError:
            print("Không thể kết nối tới dịch vụ nhận diện giọng nói.")

if __name__ == "__main__":
    recognize_speech()
