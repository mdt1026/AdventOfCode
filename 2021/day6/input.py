import re
def input():
    L = {}
    for i in range(9):
        L[i] = 0
    with open("input.txt") as f:
        line = f.read().strip().split(',')
        for c in line:
            L[int(c)] += 1

    return L
