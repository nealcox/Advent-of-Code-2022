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

    # "X" I play rock, "Y" is paper and "Z" is scissors
    my_shape = {"X": 1, "Y": 2, "Z": 3}
    outcome = {
        "A X": 3,  # rock, rock - draw
        "A Y": 6,  # rock, paper - win
        "A Z": 0,  # rock, scissors - lose
        "B X": 0,  # paper, rock - lose
        "B Y": 3,  # paper, paper - draw
        "B Z": 6,  # paper, scissors - win
        "C X": 6,  # scissors, rock - lose
        "C Y": 0,  # scissoes, paper - win
        "C Z": 3,  # scissors, scissors - draw
    }
    total_score = 0
    games = Counter(input_text.splitlines())
    for game in games.keys():
        game_score = my_shape[game[-1]] + outcome[game]
        total_score += game_score * games[game]

    return total_score


example = """\
A Y
B X
C Z
"""

example_answer = 15


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
