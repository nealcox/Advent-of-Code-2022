import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    area, height, width = get_map(input_text)
    visible_trees = set()
    # from top
    for c in range(width):
        max_height = -1
        for r in range(height):
            if area[r, c] > max_height:
                visible_trees.add((r, c))
                max_height = area[r, c]
    # from bottom
    for c in range(width):
        max_height = -1
        for r in range(height - 1, -1, -1):
            if area[r, c] > max_height:
                visible_trees.add((r, c))
                max_height = area[r, c]
    # from left
    for r in range(height):
        max_height = -1
        for c in range(width):
            if area[r, c] > max_height:
                visible_trees.add((r, c))
                max_height = area[r, c]
    # from right
    for r in range(height):
        max_height = -1
        for c in range(width - 1, -1, -1):
            if area[r, c] > max_height:
                visible_trees.add((r, c))
                max_height = area[r, c]

    return len(visible_trees)


def get_map(s):
    area = {}

    lines = s.splitlines()
    height = len(lines)
    width = len(lines[0])

    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            area[r, c] = int(char)
    given = (area, height, width)
    return given


example = """\
30373
25512
65332
33549
35390"""

example_answer = 21


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
