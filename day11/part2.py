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


class Monkey:
    def __init__(self, items, operation, test, target_true, target_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.target_true = target_true
        self.target_false = target_false
        self.inspected = 0

    def turn(self, big):
        gives = []
        for item in self.items:
            if self.operation[1].isnumeric():
                val = int(self.operation[1])
            elif self.operation[1] == "old":
                val = item
            else:
                raise ValueError(f"Invalid Value {self.operation}")
            if self.operation[0] == "+":
                item += val
            elif self.operation[0] == "*":
                item *= val
            else:
                raise ValueError("Invalid operation {operation}")
            # item = item // 3
            if item > big:
                item = item % big
            if item % self.test == 0:
                gives.append((self.target_true, item))
            else:
                gives.append((self.target_false, item))
            self.inspected += 1
            self.items = []
        return gives


def calculate(input_text):

    monkeys = []
    starting_items = []
    big = 1
    for monkey in input_text.split("\n\n"):
        lines = monkey.splitlines()
        items = get_all_ints(lines[1])
        operation = lines[2].split()[-2:]
        test = int(lines[3].split()[-1])
        big *= test
        target_true = int(lines[4].split()[-1])
        target_false = int(lines[5].split()[-1])
        m = Monkey(
            items,
            operation,
            test,
            target_true,
            target_false,
        )
        monkeys.append(m)

    for i in range(10000):
        for m in monkeys:
            gives = m.turn(big)
            for target, value in gives:
                monkeys[target].items.append(value)
    inspected = sorted([m.inspected for m in monkeys])

    return inspected[-1] * inspected[-2]


def get_all_ints(s):
    return [int(i) for i in re.findall(r"(-?\d+)", s)]


example = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

example_answer = 2713310158


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
