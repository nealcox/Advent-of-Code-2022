import re
import sys
from string import ascii_uppercase


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    stacks_in, instructions = input_text.split("\n\n")
    stacks_text = stacks_in.split("\n")
    stack_lables = stacks_text[-1]
    num_stacks = get_all_ints(stack_lables)[-1]
    stacks = [[] for _ in range(num_stacks + 1)]
    for line in stacks_text[:-1]:
        for i, c in enumerate(line):
            if c in ascii_uppercase:
                stacks[i // 4 + 1].append(c)
    for i, s in enumerate(stacks):
        stacks[i] = s[::-1]

    for instr in instructions.splitlines():
        count, from_stack, to_stack = get_all_ints(instr)
        stacks[to_stack] += stacks[from_stack][-count:]
        stacks[from_stack] = stacks[from_stack][:-count]

    return "".join(s[-1] for s in stacks[1:])


def get_all_ints(s):
    return [int(i) for i in re.findall(r"(-?\d+)", s)]


example = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

example_answer = "MCD"


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
