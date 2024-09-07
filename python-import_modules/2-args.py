#!/usr/bin/python3
import sys
if __name__ = "__main__":
    len_argv = len(sys.argv) - 1
    counter = 0
    if len_argv == 0:
        print(f"0 arguments.")
    elif len_argv == 1:
        print(f"{len_argv} argument:")
    else:
        print(f"{len_argv} arguments:")
    for elemen in sys.argv[1:]:
        counter += 1
        print(f"{counter}: {elemen}")
