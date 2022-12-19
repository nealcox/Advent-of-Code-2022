import sys


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    cubes = []
    for line in input_text.splitlines():
        cube = [int(i) for i in line.split(",")]
        cubes.append(tuple(cube))

    # Estimate surface area as number of faces less
    # the number of faces that are touching another cube
    touching_faces = 0
    for cube in cubes:
        x, y, z = cube
        for d in (1, -1):
            if (x + d, y, z) in cubes:
                touching_faces += 1
            if (x, y + d, z) in cubes:
                touching_faces += 1
            if (x, y, z + d) in cubes:
                touching_faces += 1

    return 6 * len(cubes) - touching_faces


example = """\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

example_answer = 64


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
