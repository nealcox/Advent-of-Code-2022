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

    unsolved = {}
    solved = {}
    for line in input_text.splitlines():
        name = line[:4]
        rest = line[6:].split()
        if len(rest) == 1:
            solved[name] = int(rest[0])
        else:
            unsolved[name] = rest

    solvable = defaultdict(int)
    for solved_monkey in solved:
        for unsolved_monkey in unsolved:
            if solved_monkey in unsolved[unsolved_monkey]:
                solvable[unsolved_monkey] += 1

    while "root" not in solved:
        just_solved = set()
        for monkey in unsolved:
            if solvable[monkey] == 2:
                val1 = solved[unsolved[monkey][0]]
                val2 = solved[unsolved[monkey][2]]
                if unsolved[monkey][1] == "+":
                    val = val1 + val2
                elif unsolved[monkey][1] == "-":
                    val = val1 - val2
                elif unsolved[monkey][1] == "*":
                    val = val1 * val2
                elif unsolved[monkey][1] == "/":
                    assert val1 % val2 == 0
                    val = val1 // val2
                else:
                    raise AssertionError(f"illegal operation {unsolved[monkey]}")
                just_solved.add(monkey)
                solved[monkey] = val
        for monkey in just_solved:
            del unsolved[monkey]
            for unsolved_monkey in unsolved:
                if monkey in unsolved[unsolved_monkey]:
                    solvable[unsolved_monkey] += 1
    return solved["root"]


example = """\
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""

example_answer = 152


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
