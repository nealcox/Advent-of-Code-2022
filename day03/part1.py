import sys
from string import ascii_lowercase


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    answer = 0
    for rucksack in input_text.splitlines():
        s = len(rucksack) // 2
        first = set(rucksack[:s])
        second = set(rucksack[s:])
        common = first & second

        assert len(common) == 1
        for letter in common:
            if letter in ascii_lowercase:
                answer += 1 + ord(letter) - ord("a")
            else:
                answer += 27 + ord(letter) - ord("A")
    return answer


example = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

example_answer = 157


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
