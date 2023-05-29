def print_elements(lst, num_elements):
    try:
        for i in range(num_elements):
            print(lst[i])
    except IndexError:
        print("Index out of range!")
        return(x)

# Down codes are printing x list
#Return: x > my_list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_list = 10

print_elements(x, my_list)
