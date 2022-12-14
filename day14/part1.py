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

    cave = defaultdict(lambda: ".")
    for path in input_text.splitlines():
        corners = path.split(" -> ")
        points = []
        for c in corners:
            x, y = c.split(",")
            points.append((int(x), int(y)))
        start = points[0]
        start_x, start_y = start[0], start[1]
        for end_x, end_y in points[1:]:
            dx = sgn(end_x - start_x)
            dy = sgn(end_y - start_y)
            if dx:
                for x in range(start_x, end_x + dx, dx):
                    cave[x, start_y] = "#"
            if dy:
                for y in range(start_y, end_y + dy, dy):
                    cave[start_x, y] = "#"
            start_x, start_y = end_x, end_y
    max_y = max(y for (_, y) in cave.keys())

    grains = 1
    while True:
        x, y = 500, 0
        blocked = False
        while y <= max_y and not blocked:
            # Prefer down ...
            if cave[x, y + 1] not in "#o":
                y += 1
            # ... then down left ...
            elif cave[x - 1, y + 1] not in "#o":
                x, y = x - 1, y + 1
            # ... then down right ...
            elif cave[x + 1, y + 1] not in "#o":
                x, y = x + 1, y + 1
            else:
                blocked = True
        cave[x, y] = "o"
        if y >= max_y:
            min_x = min(x for (x, _) in cave.keys())
            max_x = max(x for (x, _) in cave.keys())
            max_y = max(y for (_, y) in cave.keys())
            for r in range(0, max_y + 1):
                for c in range(min_x, max_x + 1):
                    print(cave[c, r], end="")
                print()
            return grains - 1
        grains += 1


def sgn(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


example = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

example_answer = 24


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
