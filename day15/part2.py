import re
import sys


def main():
    filename = "input.txt"
    max_xy = 4000000
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if len(sys.argv) > 2:
            max_xy = int(sys.argv[2])
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text, max_xy)}")


def calculate(input_text, max_xy):

    beacons = []
    for line in input_text.splitlines():
        x_s, y_s, x_b, y_b = get_all_ints(line)
        man_dist = abs(x_s - x_b) + abs(y_s - y_b)
        beacons.append((x_s, y_s, x_b, y_b, man_dist))
    beacons.sort()

    for test_y in range(max_xy + 1):
        ranges = []
        for b in beacons:
            x_s, y_s, x_b, y_b, man_dist = b
            y_dist = abs(test_y - y_s)
            # On line y = y_s, there are man_dist places
            # either side of S that cannot be beacons
            # (unless the beacon is on that line)
            # from x_s - man_dist
            # to   x_s + man_dist + 1
            #
            # This range reduces by 1 on each side for every step away
            # on y axis so range is
            # from x_s - man_dist - abs(test_y - y_s)
            # to   x_s + man_dist - abs(test_y - y_s)  6-9 at 0
            low = x_s - man_dist + y_dist
            high = x_s + man_dist - y_dist
            if low <= high:
                ranges.append((low, high))

        ranges.sort()
        min_x = min(x for (x, _) in ranges)
        max_x = max(x for (_, x) in ranges)
        assert min_x <= 0
        high = 0  # All sensors have x > 0, as long as min_x <=0 this is ok
        for r in ranges:
            if r[0] > high:
                return (4000000 * (high + 1)) + test_y
            else:
                high = max(r[1], high)


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

example_answer = 56000011


def test_example():
    assert calculate(example, 20) == example_answer


if __name__ == "__main__":
    exit(main())
