import re
def input():
    L = []
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for l in lines:
            r = [10]
            for c in l:
                r.append(int(c))
            L.append(r + [10])

    return [[10]*len(L[0])] + L + [[10]*len(L[0])]
