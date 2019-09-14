#!/usr/bin/env python3

from sys import argv
from re import match
# TODO: set global errno as return value

def validateHexString(hexstr):
    return match(r"#[0-9a-fA-F]{6}", hexstr)


def validateInput(*args):
    if (len(argv) < 3):
        print("you must pass 3 numbers as arguments, or lists containing numbers")
        return False
    try:
        for i in range(len(args)):
            if type(args[i]) is list:
                for j in range(len(args[i])):
                    if (int(args[i][j]) < 0 or int(args[i][j]) > 255):
                        print(
                            "the values given are not in a valid of range of 0-255 inclusive")
                        return False
        return True
    except Exception:
        print("the argument supplied were not numbers.")
        return False


def hexblend(*args):
    print(args)


def hexColor(red, green, blue):
    print("#{:>02s}{:>02s}{:>02s}".format(hex(red).replace("0x", ""), hex(
        green).replace("0x", ""), hex(blue).replace("0x", "")).upper())


if __name__ == "__main__":
    if not validateInput(argv[-(len(argv)-1):]):
        exit(-1)
    hexColor(int(argv[1]), int(argv[2]), int(argv[3]))
