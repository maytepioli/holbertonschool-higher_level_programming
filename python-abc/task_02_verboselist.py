#!/usr/bin/python3
class VerboseList(list):
    def append(self, element):
        super().append(element)
        print(f"Added [{element}] to the list.")


    def extend(self, element):
        super().extend(element)
        print(f"Extended the list with [{len(element)}] items.")

    def remove(self, element):
        super().remove(element)
        print(f"Removed [element] from the list.")

    def pop(self, element = -1):
        value = super().pop(element)
        print(f"Popped [{value}] from the list.")
        return value
