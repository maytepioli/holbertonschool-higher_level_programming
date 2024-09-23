#!/usr/bin/python3
"""
Módulo que define la clase MyList.

La clase MyList hereda de la clase list y añade un método
para imprimir la lista en orden ascendente.
"""


class MyList(list):
    """
    Clase que hereda de list y añade un método para imprimir la lista ordenada.
    """
    def print_sorted(self):
        """
        Imprime la lista en orden ascendente.
        """
        print(sorted(self))
