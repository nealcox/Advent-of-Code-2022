import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    answer = 0
    for i, pair in enumerate(input_text.split("\n\n"), start=1):
        left_s, right_s = pair.splitlines()
        left = parse(left_s)
        right = parse(right_s)
        if right_order(left, right):
            answer += i
    return answer


def right_order(a, b):
    if len(a) == 0 and len(b) > 0:
        return True
    elif len(a) > 0 and len(b) == 0:
        return False

    l1, l2 = a[0], b[0]

    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return True
        if l2 < l1:
            return False
        else:
            return right_order(a[1:], b[1:])
    elif isinstance(l1, list) and isinstance(l2, list):
        if len(l1) == 0 and len(l2) > 0:
            return True
        elif len(l1) > 0 and len(l2) == 0:
            return False
        elif len(l1) == 0:  # Both empty
            return right_order(a[1:], b[1:])
        else:  # both non empty
            return right_order(
                [l1[0], l1[1:], a[1:]],
                [l2[0], l2[1:], b[1:]],
            )
    elif isinstance(l1, int) and isinstance(l2, list):  # one a list and the otheran int
        return right_order(
            [[l1], a[1:]],
            b,
        )
    elif isinstance(l1, list) and isinstance(l2, int):  # one a list and the otheran int
        return right_order(
            a,
            [[l2], b[1:]],
        )
    else:
        raise ValueError(f"Unexpected comparison {a} v {b}")


def parse(s):
    l = []
    prev = None
    for c in s:
        if c.isnumeric():
            if prev is not None:
                prev = prev * 10 + int(c)
            else:
                prev = int(c)
        else:
            if prev is not None:
                l.append(prev)
                prev = None
            if c != ",":
                l.append(c)
    while "]" in l:
        end = l.index("]")
        if end == len(l) - 1:
            return l[1:-1]
        start = end
        while l[start] != "[":
            start -= 1
        to_start = l[:start][:]
        middle = l[start + 1 : end][:]
        to_end = l[end + 1 :]
        to_start.append(middle)
        l = to_start + to_end


def test1():
    assert (
        right_order(
            [1, 1, 3, 1, 1],
            [1, 1, 5, 1, 1],
        )
        == True
    )


def test2():
    assert (
        right_order(
            [[1], [2, 3, 4]],
            [[1], 4],
        )
        == True
    )


def test3():
    assert (
        right_order(
            [9],
            [[8, 7, 6]],
        )
        == False
    )


def test4():
    assert (
        right_order(
            [[4, 4], 4, 4],
            [[4, 4], 4, 4, 4],
        )
        == True
    )


def test5():
    assert (
        right_order(
            [7, 7, 7, 7],
            [7, 7, 7],
        )
        == False
    )


def test6():
    assert (
        right_order(
            [],
            [3],
        )
        == True
    )


def test7():
    assert (
        right_order(
            [[[]]],
            [[]],
        )
        == False
    )


def test8():
    assert (
        right_order(
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        )
        == False
    )


example = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

example_answer = 13


def test_example():
    assert calculate(example) == example_answer


def test_as():
    with open("as_input.txt") as f:
        txt = f.read().strip()
    assert calculate(txt) == 6656


if __name__ == "__main__":
    exit(main())
