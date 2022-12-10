import re
import sys
from collections import defaultdict
from itertools import permutations


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    cycles = 0
    X = 1
    hist = {0: X}
    for line in input_text.splitlines():
        inst = line.split()
        if inst[0] == "noop":
            cycles += 1
        elif inst[0] == "addx":
            X += int(inst[1])
            cycles += 2
        else:
            raise ValueError(inst)
        hist[cycles] = X

    X = hist[0]
    for r in range(6):
        for c in range(40):
            i = r * 40 + c
            if i in hist.keys():
                X = hist[i]
            if abs(X - c) < 2:
                print("#", end="")
            else:
                print(".", end="")
        print()
    return


if __name__ == "__main__":
    exit(main())
