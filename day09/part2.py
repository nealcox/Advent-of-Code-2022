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

    num_knots = 10
    dirs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    seen = set()
    knots = [(0, 0)] * 10
    seen.add(knots[-1])
    for line in input_text.splitlines():
        d, count = line.split()
        for _ in range(int(count)):
            move = dirs[d]
            knots[0] = (knots[0][0] + move[0], knots[0][1] + move[1])
            for t in range(1, num_knots):
                move_dir = (
                    knots[t - 1][0] - knots[t][0],
                    knots[t - 1][1] - knots[t][1],
                )
                if abs(move_dir[0]) > 1 or abs(move_dir[1]) > 1:
                    move = (sign(move_dir[0]), sign(move_dir[1]))
                    knots[t] = (knots[t][0] + move[0], knots[t][1] + move[1])
            seen.add(knots[-1])

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

example_answer = 1


def test_example():
    assert calculate(example) == example_answer


example2 = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

example_answer2 = 36


def test_example2():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
