def reverse_string():
    user_input = input("Nhập một chuỗi: ")
    reversed_string = user_input[::-1]
    print(f"Chuỗi đảo ngược là: {reversed_string}")
if __name__ == "__main__":
    reverse_string()
