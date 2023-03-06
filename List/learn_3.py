# Thao tác List, nhập, thêm - chèn, xóa, sửa, gộp

# Nhập list
from traceback import print_list


list_input = [input("Nhập list: > ")]
print(list_input)
# Enter with Loop
list_a = []
for i in range(0, 5):
    list_b = [int(input(f"Enter integer {i} > "))]
    list_a.append(list_b)
    list_a.sort()
print(list_a)

# Add to list
list_a.insert(1,"g")
print(list_a)
# Extend list
list_b = ["Phan Nguyen Quoc Huy", "23/11/2004", "Nam"]
print(list_a + list_b)
list_a.extend(list_b)
print("***********")
print(list_a)
# Remove list. remove "g" of list_a
list_a.remove("g")
print(list_a, "\n*********************")
# find less numbers of list