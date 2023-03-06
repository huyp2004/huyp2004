# nhập họ và tên vào bảng, họ tên ngắn < 8 ký tự thì nhập lại, có ký tự dặc biệt thì nhập lại và sau đó chèn vào list
# nhập họ và tên vào bảng, họ tên ngắn < 8 ký tự thì nhập lại, có ký tự dặc biệt thì nhập lại và sau đó chèn vào list
list_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "="]


def check_name():
    name_char = input("Nhập tên: ")
    while True:
        if len(name_char) < 8:
            print("Bạn nhập tên không hợp lệ, tên phải từ 8 ký tự")
            name_char = input("Nhập lại tên: ")
            print(name_char)
        elif any(i in list_char for i in name_char):
            print("Bạn nhập tên không hợp lệ, tên không được chứa ký tự đặc biệt")
            name_char = input("Nhập lại tên: ")
            print(name_char)
        else:
            break


check_name()
