#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    ab = add(a, b)
    print("{} + {} = {}".format(a, b, ab))
    ab = sub(a, b)
    print("{} - {} = {}".format(a, b, ab))
    ab = mul(a, b)
    print("{} * {} = {}".format(a, b, ab))
    ab = div(a, b)
    print("{} / {} = {}".format(a, b, ab))
