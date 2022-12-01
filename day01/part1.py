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
    cals = defaultdict(int)
    for i, elf in enumerate(input_text.split("\n\n")):
        for snack in elf.split("\n"):
            cals[i] += int(snack)

    return max(cals.values())


example = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

example_answer = 24000


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
