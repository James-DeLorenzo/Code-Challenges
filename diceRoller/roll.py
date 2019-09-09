from random import randrange as rand
from re import match

def validate_input(die):
    test = die.split("d")
    if not match(r"^[1-9][0-9]*d[2-9][0-9]*", die):
        print("input is not formatted as #d#")
        return False
    if (int(test[0]) < 1 or int(test[0]) > 100):
        print("number of dice is not between 1 and 100 inclusive")
        return False
    if (int(test[1]) < 2 or int(test[1]) > 100):
        print("number of sides is not between 1 and 100 inclusive")
        return False
    return True


def roll(die):
    if (not validate_input(die)):
        return
    die_rolls = die.split('d')
    total = 0
    rolls = []
    for n in range(int(die_rolls[0])):
        roll = rand(1, int(die_rolls[1]) + 1)
        rolls.append(roll)
        total += roll
    print("{}: {}".format(total, " ".join(str(x) for x in rolls)))


if __name__ == "__main__":
    die = input(
        'Please enter number of die and in #d# format, or \'q\' to quit: ')
    while (die != "q"):
        roll(die)
        die = input(
            "Please enter number of die and sides in #d# format, or 'q' to quit: ")
