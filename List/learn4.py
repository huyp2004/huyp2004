# numl = []
# for i in range(0, 5):
#     try:
#         nums = int(input('Enter integer: '))
#         numl.append(nums)
#     except ValueError:
#         print("You wrong enter !")
# print(numl)

# List 2D

my_list = [[81,8,69,7], [41,5,56], [79,58,89]]
# def sort_2d_list(my_list):
#     my_list = [sorted(i) for i in my_list]
#     return my_list
# print(sort_2d_list(my_list))

my_list = [sum(j) for j in my_list]
print(my_list)
