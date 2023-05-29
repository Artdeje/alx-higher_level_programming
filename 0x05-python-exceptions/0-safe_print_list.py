#!/usr/bin/python3
def print_elements(lst, num_elements):
    try:
        for i in range(num_elements):
            print(lst[i])
    except IndexError:
        print("Index out of range!")

# Down codes are printing x list
#Return: x > my_list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
x = 15

print_elements(my_list, x)
