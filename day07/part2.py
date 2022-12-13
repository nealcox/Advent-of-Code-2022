import sys
from collections import defaultdict


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    path = []
    wd = ""
    all_dirs = ["/"]
    sub_dirs = defaultdict(list)
    direct_size = defaultdict(int)
    lsed = set()
    in_ls = False
    for line in input_text.splitlines():
        if line.startswith("$"):
            in_ls = False
        elif in_ls:
            parts = line.split()
            if parts[0] == "dir":
                sub_dirs[wd].append(parts[1])
            elif parts[0].isnumeric():
                direct_size[wd] += int(parts[0])
        if line.startswith("$ cd"):
            to = line.split()[-1]
            if to == "..":
                path.pop()
            else:
                path.append(to)
            wd = "/".join(path)
            if wd not in all_dirs:
                all_dirs.append(wd)
        elif line.startswith("$ ls"):
            in_ls = True
            lsed.add(wd)

    sizes = {}
    while all_dirs:
        d = all_dirs.pop()
        s = direct_size[d]
        for sub_d in sub_dirs[d]:
            s += sizes[d + "/" + sub_d]
        sizes[d] = s

    to_delete = 30000000 - 70000000 + sizes["/"]
    return min(s for s in sizes.values() if s > to_delete)


example = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

example_answer = 24933642


def test_example():
    assert calculate(example) == example_answer


if __name__ == "__main__":
    exit(main())
