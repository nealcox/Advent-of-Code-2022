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

    length = 14
    answer = 0
    while True:
        diff = set(input_text[answer : answer + length])
        if len(diff) == length:
            return answer + length
        answer += 1


example = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

example_answer = 19


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
