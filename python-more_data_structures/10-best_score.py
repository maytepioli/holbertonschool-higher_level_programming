#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    list_claves, list_value = list(a_dictionary.items())[0]
    for claves, value in a_dictionary.items():
        if value > list_value:
            value = list_value
            list_claves = claves
    return list_claves
