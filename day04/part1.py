import re
import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    answer = 0
    for line in input_text.splitlines():
        i, j, x, y = get_all_ints(line)
        if (x >= i and y <= j) or (i >= x and j <= y):
            answer += 1
    return answer


def get_all_ints(s):
    return (int(i) for i in re.findall(r"(\d+)", s))


example = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

example_answer = 2


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
