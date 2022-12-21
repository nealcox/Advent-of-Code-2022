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
        if name != "humn":
            if len(rest) == 1:
                solved[name] = int(rest[0])
            else:
                unsolved[name] = rest
    unsolved["root"][1] = "="

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
        if not just_solved:
            for unsolved_monkey in unsolved:
                m1 = unsolved[unsolved_monkey][0]
                m2 = unsolved[unsolved_monkey][2]
                if m1 in solved:
                    unsolved[unsolved_monkey][0] = int(solved[m1])
                if m2 in solved:
                    unsolved[unsolved_monkey][2] = int(solved[m2])
            target = sum(v for v in unsolved["root"] if isinstance(v, int))
            to_eliminate = set(
                name
                for name in unsolved["root"]
                if isinstance(name, str) and len(name) == 4
            )
            while to_eliminate:
                next_to_eliminate = set()
                for eliminating in to_eliminate:
                    m1, op, m2 = unsolved[eliminating]
                    if op == "/":
                        assert isinstance(m2, int)
                        next_to_eliminate.add(m1)
                        target = m2 * target
                    elif op == "-":
                        if isinstance(m1, int):
                            target = m1 - target
                            next_to_eliminate.add(m2)
                        else:
                            target = m2 + target
                            next_to_eliminate.add(m1)
                    else:
                        if isinstance(m1, int):
                            m1, m2 = m2, m1
                        if op == "+":
                            target = target - m2
                            next_to_eliminate.add(m1)
                        if op == "*":
                            assert target % m2 == 0
                            target = target // m2
                            next_to_eliminate.add(m1)
                to_eliminate = next_to_eliminate
                if "humn" in to_eliminate:
                    to_eliminate = set()
            return target
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

example_answer = 301


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
