# tìm giá trị có trong list
print("nhập 4 giá trị vào: ")
list_py = []
for i in range(1, 5):
    list_py.append(input(f'giá trị {i}: '))
print(list_py)
print("tìm giá trị có trong list")
a = input("giá trị cần tìm: ")
if a in list_py:
    print(f'{a} có trong list')
else:
    print(f'{a} không có trong list')
