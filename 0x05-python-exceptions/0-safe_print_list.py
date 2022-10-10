#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list[:x]:
            print(my_list[i-1], end="")
        print()
        return my_list[x-1]
    except IndexError:
        return my_list[-1]
