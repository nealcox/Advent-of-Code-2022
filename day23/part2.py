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

    elves = set()
    part2 = None
    for row, line in enumerate(input_text.splitlines()):
        for col, c in enumerate(line):
            if c == "#":
                elves.add((row, col))

    directions = "NSWE"
    neighbours = {
        "N": ((-1, -1), (-1, 0), (-1, 1)),
        "S": ((1, -1), (1, 0), (1, 1)),
        "W": ((-1, -1), (0, -1), (1, -1)),
        "E": ((-1, 1), (0, 1), (1, 1)),
    }

    rounds = 0
    while not part2:
        rounds += 1
        proposed = defaultdict(list)
        for elf in elves:
            row, col = elf
            if any(pos in elves for pos in all_neighbours(elf)):
                for d in directions:
                    neighbour_in_dir = False
                    for (dr, dc) in neighbours[d]:
                        if (row + dr, col + dc) in elves:
                            neighbour_in_dir = True
                            break
                    if not neighbour_in_dir:
                        proposed[get_pos(elf, d)].append(elf)
                        break

        moved = False
        for pos in proposed:
            if len(proposed[pos]) == 1:
                elves.add(pos)
                elves.remove(proposed[pos][0])
                moved = True
        if not moved:
            part2 = rounds
        directions = directions[1:] + directions[0]

    print_elves(elves)

    return part2


def print_elves(elves):
    r_min = min(r for (r, _) in elves)
    r_max = max(r for (r, _) in elves)
    c_min = min(c for (_, c) in elves)
    c_max = max(c for (_, c) in elves)

    for r in range(r_min, r_max + 1):
        for c in range(c_min, c_max + 1):
            if (r, c) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def get_pos(elf, d):
    r, c = elf
    if d == "N":
        return r - 1, c
    elif d == "S":
        return r + 1, c
    elif d == "W":
        return r, c - 1
    elif d == "E":
        return r, c + 1


def all_neighbours(elf):
    r, c = elf
    return [
        (r + dr, c + dc)
        for (dr, dc) in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (1, -1),
            (1, 0),
            (1, 1),
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 1),
            (0, 1),
            (1, 1),
        )
    ]


example = """\
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""

example_answer = 20


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
