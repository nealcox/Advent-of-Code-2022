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


def calculate(input_text):

    cubes = set()
    for line in input_text.splitlines():
        cube = [int(i) for i in line.split(",")]
        cubes.add(tuple(cube))

    return surface_area(cubes)


def surface_area(cubes):

    # Estimate surface area as number of faces less
    # the number of faces that are touching another cube
    # But need to exclude interal air pockets
    # Get all air that touches the cubes we have
    air = set()
    touching_faces = 0
    for cube in cubes:
        for neighbour in neighbours(cube):
            if neighbour in cubes:
                touching_faces += 1
            else:
                air.add(neighbour)

    # Pad out air boundary with adjacent air cells
    padding = set()
    for x, y, z in air:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if (x + dx, y + dy, z + dz) not in cubes:
                        padding.add((x + dx, y + dy, z + dz))
    air |= padding

    # We need to separate the air that is internal to the shape from
    # that which is external
    # Get some cells of air that is definitely outside the lava cells
    min_x_lava = min(x for (x, _, _) in cubes)
    external_air = set()
    for a in air:
        x, _, _ = a
        if x < min_x_lava:
            external_air.add(a)

    # Now add any air that touches the external air we have to the external air
    # until theres none left of our aoutching air and its padding
    changed = True
    while changed:
        changed = False
        new_external = set()
        for ext in external_air:
            for neighbour in neighbours(ext):
                if neighbour in air and neighbour not in external_air:
                    new_external.add(neighbour)
        if new_external:
            external_air |= new_external & air
            changed = True
            new_external = set()
        external_air |= new_external
    internal_air = air - external_air

    if internal_air:
        # Consider surface area of lava if we fill in the internal holes
        answer = surface_area(internal_air | cubes)
    else:
        # No internal holes
        answer = 6 * len(cubes) - touching_faces

    return answer


def neighbours(cell):
    x, y, z = cell
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]


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

example_answer = 58


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
