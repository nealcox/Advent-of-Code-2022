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

    dirs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    seen = set()
    x_head, y_head = 0, 0
    x_tail, y_tail = 0, 0
    seen.add((x_tail, y_tail))
    for line in input_text.splitlines():
        d, count = line.split()
        dx_h, dy_h = dirs[d]
        for i in range(int(count)):
            x_head, y_head = x_head + dx_h, y_head + dy_h
            dx_tail, dy_tail = x_head - x_tail, y_head - y_tail
            if abs(dx_tail) > 1 or abs(dy_tail) > 1:
                dx_tail = sign(dx_tail)
                x_tail += dx_tail
                dy_tail = sign(dy_tail)
                y_tail += dy_tail
            seen.add((x_tail, y_tail))

    return len(seen)


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


example = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

example_answer = 13


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
