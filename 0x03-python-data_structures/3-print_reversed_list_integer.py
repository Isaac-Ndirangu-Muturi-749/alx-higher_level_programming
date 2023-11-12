#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Use a for loop to iterate over the indices of the list in reverse order.
    # We start from the last index (len(my_list) - 1) and go backwards to 0.
    for i in range(len(my_list) - 1, -1, -1):
        if my_list is None:
            return
        print("{:d}".format(my_list[i]))
