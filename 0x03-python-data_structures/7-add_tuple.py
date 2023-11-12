#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements of each tuple (or use 0 if not available)
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    # Calculate the sum of the corresponding elements and create a new tuple
    result = (a1 + b1, a2 + b2)

    return result
