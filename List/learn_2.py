from datetime import datetime
list_in = []
name_sv = input('nhập họ và tên: ')
age = input("nhập ngày / tháng / năm sinh: ")
now = datetime.now()
list_in.append(name_sv)
list_in.append(age)

print(list_in)
print("*"*15)

list_insert = [1, 2, 3, 4]
list_in.insert(3, list_insert)
print(list_in)
print("*"*15)
del list_insert[0]
print(list_insert)
print("*"*15)

hotday = True
if hotday:
    print("so hot")
