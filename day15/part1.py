import re
import sys
from collections import defaultdict
from itertools import permutations


def main():
    filename = "input.txt"
    test_y = 2000000
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if len(sys.argv) > 2:
            test_y = int(sys.argv[2])
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text, test_y)}")


def calculate(input_text, test_y):

    answer = 0

    beacons = set()
    ranges = []

    for line in input_text.splitlines():
        x_s, y_s, x_b, y_b = get_all_ints(line)
        man_dist = abs(x_s - x_b) + abs(y_s - y_b)
        y_dist = abs(test_y - y_s)
        # On line y = y_s, there are man_dist places
        # either side of S that cannot be beacons
        # (unless the beacon is on that line)
        # from x_s - man_dist
        # to   x_s + man_dist + 1
        #
        # This range reduces by 1 for every step away
        # on y axis so range is
        # from x_s - man_dist - abs(test_y - y_s)
        # to   x_s + man_dist - abs(test_y - y_s)  6-9 at 0
        low = x_s - man_dist + y_dist
        high = x_s + man_dist - y_dist
        if low <= high:
            ranges.append((low, high))
        if y_b == test_y:
            beacons.add(x_b)

    ranges.sort()
    disjoint = []
    low, high = ranges[0]
    for r in ranges[1:]:
        test_low, test_high = r
        if high < test_low:
            # disjoint
            disjoint.append((low, high))
            low, high = test_low, test_high
        else:
            high = max(high, test_high)
    disjoint.append((low, high))

    for low, high in disjoint:
        answer += high - low + 1
        for b in beacons:
            if low <= b <= high:
                answer -= 1

    return answer


def get_all_ints(s):
    return (int(i) for i in re.findall(r"(-?\d+)", s))


example = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

example_answer = 26


def test_example():
    assert calculate(example, 10) == example_answer


if __name__ == "__main__":
    exit(main())
