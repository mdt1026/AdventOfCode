import re
def input():
    L = []
    with open("input.txt") as f:
        line = f.read().strip().split(',')
        for c in line:
            L.append(int(c))

    return L
