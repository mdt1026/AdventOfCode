import re
def input():
    L = []
    with open("input.txt") as f:
        lines = f.read().splitlines()
        for l in lines:
            r = []
            for h in l.split(" | "):
                r2 = []
                for s in h.split():
                    r2.append(''.join(sorted(s)))
                r.append(r2)
            L.append(r)

    return L
