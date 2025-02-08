class Soda:
    """represents names and their soda choice"""

    def __init__(self):
        """initialize a Soda

        Data Members:
        _Sodas -- (dict) Keys(str) are names and values(str) are soda choice
        """
        self._sodas = {}
        return

    def add_one(self, name, soda):
        """Add an entry to the sodas dictionary"""
        self._sodas[soda] = name
        return

    def to_string():
        """creates a string of items in the dictionary"""
        display_string = ""
        for item in self._sodas:
            string = name + " recommends " + self._sodas["Carol"]
            display_string += string + "\n"

        return display_string


def main():
    sodas = Soda
    name = input("Name? ")
    soda = input("Soda? ")
    sodas.add_one(name, soda)
    name = input("Name? ")
    soda = input("Soda? ")
    sodas.add_one(name, soda)
    print(sodas.to_string())
    return


if __name__ == "__main__":
    main()

""" Correct Output with the following input:
Name? Abe
Soda? Mountain Dew
Name? Zeb
Soda? Coke
Abe recommends Mountain Dew
Zeb recommends Coke
"""
