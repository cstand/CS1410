from pokemon_debug import Pokemon


# from  pokemon import *
# import pokemon


def add_pokemon(pokedex):
    print("Give me the new pokemon's information.")
    name = input("Name? ")
    type_name = input("Type? ")
    type_number = int(input("Number? "))
    max_hp = int(input("Max HP? "))
    p = Pokemon(name, type_name, type_number, max_hp, max_hp)
    pokedex.append(p)
    return


def display_all_pokemon(pokedex):
    for p in range(len(pokedex)):
        print(str(p))
    return


def pika_example():
    pikachu = Pokemon("Pikachu", "Electric", 25, 35, 35)
    print(pikachu.getName())
    pikachu.setName("Joe")
    print(str(pikachu.getName()))

    pikachu.takeDamage(10)
    pikachu.takeDamage(3)

    return


def main():
    pokedex = []
    pika_example()
    choice == "n"
    while choice != "N":
        add_pokemon(pokedex)
        display_all_pokemon(pokedex)
        choice = input("Are you done? (Y/N)").upper()
    return


main()

"""Output should be:
Pikachu
JOE{Electric:25} Max HP: 35 Current HP: 35
JOE{Electric:25} Max HP: 35 Current HP: 22
Give me the new pokemon's information.
Name? Charmander
Type? Fire
Number? 4
Max HP? 39
CHARMANDER{Fire:4} Max HP: 39 Current HP: 39
Are you done? (Y/N)n
Give me the new pokemon's information.
Name? Bellossom
Type? Grass
Number? 182
Max HP? 75
CHARMANDER{Fire:4} Max HP: 39 Current HP: 39
BELLOSSOM{Grass:182} Max HP: 75 Current HP: 75
Are you done? (Y/N)y
"""
