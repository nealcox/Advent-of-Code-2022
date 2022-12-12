import sys
from collections import defaultdict


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    area, height, width, pos, dest = get_map(input_text)
    a_s = set(position for position, char in area.items() if char == ord("a"))

    best = defaultdict(lambda: float("inf"))
    best[dest] = 0
    possible = [(dest, area[dest], 0)]
    deltas = ((1, 0), (0, -1), (-1, 0), (0, 1))
    while possible:
        next_possible = []
        for (r, c), cur_height, cur_steps in possible:
            next_steps = cur_steps + 1
            for (dr, dc) in deltas:
                next_r, next_c = r + dr, c + dc
                if (next_r, next_c) in area.keys():
                    if (
                        area[next_r, next_c] >= cur_height - 1
                        and next_steps < best[next_r, next_c]
                    ):
                        best[next_r, next_c] = next_steps
                        next_possible.append(
                            ((next_r, next_c), area[next_r, next_c], next_steps)
                        )
        possible = next_possible

    return min(best[a] for a in a_s)


def get_map(s):
    area = {}

    lines = s.splitlines()
    height = len(lines)
    width = len(lines[0])

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if char == "S":
                pos = (r, c)
                char = "a"
            elif char == "E":
                dest = (r, c)
                char = "z"
            area[r, c] = ord(char)
    return area, height, width, pos, dest


example = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

example_answer = 29


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
