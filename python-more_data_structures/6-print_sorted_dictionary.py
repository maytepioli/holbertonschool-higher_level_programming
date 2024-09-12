#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary_sort = sorted(a_dictionary)
    for clave in dictionary_sort:
        print(f"{clave}: {a_dictionary[clave]}")
