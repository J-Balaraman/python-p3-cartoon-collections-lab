def roll_call_dwarves(names):
    num = 1
    for dwarf in names:
        print(f"{num}. {dwarf}")
        num += 1

def summon_captain_planet(elements):
    new_list = []
    for name in elements:
        new_list.append(f"{name.capitalize()}!")
    return new_list

def long_planeteer_calls(list):
    for string in list:
        if len(string) > 4:
            return True
    return False

def find_the_cheese(list):
    for food in list:
        if food == "cheddar":
            return food
        elif food == "gouda":
            return food
        elif food == "camembert":
            return food
    return None