#!/usr/bin/env python3

from sys import argv


def hexColor(red, green, blue):
    print("#{:>02s}{:>02s}{:>02s}".format(hex(red).replace("0x", ""), hex(
        green).replace("0x", ""), hex(blue).replace("0x", "")).upper())


if __name__ == "__main__":
    if (len(argv) < 4):
        print("you must pass 3 numbers as arguments")
        exit(-1)
    try:
        for i in range(1, 4):
            if (int(argv[i]) < 0 or int(argv[i]) > 255):
                print("the values given are not in a valid of range of 0-255 inclusive")
                exit(-3)
        hexColor(int(argv[1]), int(argv[2]), int(argv[3]))
    except Exception:
        print("the argument supplied were not numbers.")
        exit(-2)
