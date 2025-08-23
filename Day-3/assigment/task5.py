my_list = [1, 2, 3, 4, 5]

# Identity operators
a = my_list
b = [1, 2, 3, 4, 5]

same_object = a is my_list
not_same_object = b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 5 not in my_list



print("a is my_list:", same_object)
print("b is not my_list:", not_same_object)
print("element_in_list:", element_in_list)
print("element_not_in_list:", element_not_in_list)