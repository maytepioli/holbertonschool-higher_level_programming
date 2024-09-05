#!/usr/bin/python3
def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False


def uppercase(str):
    i = 0
    while i < len(str):
        if islower(str[i]):
            ascii = ord(str[i])
            ascii = ascii - 32
            ascii = chr(ascii)
        else:
            ascii = str[i]
        print("{}".format(ascii), end="")
        i = i + 1
    print()
