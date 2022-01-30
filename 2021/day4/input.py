import re
def input():
    L = []
    with open("input.txt") as f:
        lines = f.read().strip().split("\n\n")
        for i in lines:
            L.append(i)

    return L
