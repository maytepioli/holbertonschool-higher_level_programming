#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            ele = my_list[i]
            if isinstance(ele, int):
                print("{:d}".format(ele), end="")
                count += 1
            elif isinstance(ele, list):
                for j in ele:
                    break
        print()
    except TypeError:
        print()
    return count
