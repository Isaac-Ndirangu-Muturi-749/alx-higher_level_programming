#!/usr/bin/python3

for tens in range(10):
    for ones in range(tens + 1, 10):
        if tens < 9:
            print(f"{tens}{ones}, ", end='')
        else:
            print(f"{tens}{ones}")
