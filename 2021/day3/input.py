def input():
    lines = []
    with open("input.txt") as f:
        L = f.read().splitlines()
        for line in L:
            lines.append(line)
        return lines
