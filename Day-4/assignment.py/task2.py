my_tuple = (1, 2, 'apple', 'banana')

first_element = my_tuple[1],[3]

print(len(first_element))

#second_element = my_tuple.append("ram")
#print(second_element)

new_tuple = my_tuple + (3.14, "cherry")
print(new_tuple)

is_present = 'apple' in my_tuple
print(is_present)

is_present = 'siva' in my_tuple
print(is_present)

def get_coordinates():
    return(3, 4)

x, y = get_coordinates()