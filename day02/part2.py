import sys
from collections import Counter


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    # "X" I lose
    # "Y" We draw
    # "Z" I win
    result = {"X":0, "Y":3, "Z":6}
    my_play = {
            "A X": 3,  # rock, lose - scissors
            "A Y": 1,  # rock, draw - rock 
            "A Z": 2,  # rock, win - paper
            "B X": 1,  # paper, lose - rock
            "B Y": 2,  # paper, draw - paper
            "B Z": 3,  # paper, win - scissors
            "C X": 2,  # scissors, lose - paper
            "C Y": 3,  # scissoes, draw - scissors
            "C Z": 1,  # scissors, win - rock
            }
    total_score = 0
    games = Counter(input_text.splitlines())
    for game in games.keys():
        game_score = result[game[-1]] + my_play[game]
        total_score += game_score * games[game]

    return total_score


example = """\
A Y
B X
C Z
"""

example_answer = 12


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
