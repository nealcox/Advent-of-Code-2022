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
    rucksacks = input_text.splitlines()
    for i, rucksack in enumerate(rucksacks):
        if i % 3 == 2:
            first = set(rucksacks[i - 2])
            second = set(rucksacks[i - 1])
            third = set(rucksacks[i])
            common = first & second & third

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

example_answer = 70


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
