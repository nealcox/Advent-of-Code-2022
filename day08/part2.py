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
    scenic = {}
    for c in range(width):
        for r in range(height):
            # down
            visible_down = 0
            max_height = area[r, c]
            for r_target in range(r + 1, height):
                visible_down += 1
                if area[r_target, c] >= max_height:
                    break
            # up
            visible_up = 0
            max_height = area[r, c]
            for r_target in range(r - 1, -1, -1):
                visible_up += 1
                if area[r_target, c] >= max_height:
                    break
            # right
            visible_right = 0
            max_height = area[r, c]
            for c_target in range(c + 1, width):
                visible_right += 1
                if area[r, c_target] >= max_height:
                    break
            # Left
            visible_left = 0
            max_height = area[r, c]
            for c_target in range(c - 1, -1, -1):
                visible_left += 1
                if area[r, c_target] >= max_height:
                    break

            scenic[r, c] = visible_left * visible_right * visible_up * visible_down

    return max(scenic.values())


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

example_answer = 8


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
