import re
import sys
from collections import deque
from itertools import permutations


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    numbers = [int(i) * 811589153 for i in re.findall(r"(-?\d+)", input_text)]
    decrypted = deque(range(len(numbers)))
    length = len(decrypted)
    for i in range(10):
        for num in range(len(numbers)):
            from_pos = decrypted.index(num)
            decrypted.remove(num)
            decrypted.rotate(-numbers[num])
            decrypted.insert(from_pos, num)
    idx = decrypted.index(numbers.index(0))
    return (
        numbers[decrypted[(idx + 1000) % length]]
        + numbers[decrypted[(idx + 2000) % length]]
        + numbers[decrypted[(idx + 3000) % length]]
    )


example = """\
1
2
-3
3
-2
0
4
"""

example_answer = 1623178306


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
