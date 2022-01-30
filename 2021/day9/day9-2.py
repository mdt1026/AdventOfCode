from input import input; import re; import pyperclip as pc; from collections import Counter; import numpy as np; from scipy.ndimage import label
def main():
    data = input()
    b, s, d = list(), list(), dict()
    for l in data:
        r = []
        for n in l:
            r.append(0 if n>8 else 1)
        b.append(r)
    b = np.array(b)
    basin = np.ones((3,3), dtype=np.int)
    basins, count = label(b)

    for r in basins:
        for c in r:
            if c:
                d[c] = (d[c]+1) if c in d else 1
    o = sorted(d.values(), reverse=True)[:3]
    print(o, np.prod(o))
    pc.copy(str(np.prod(o)))

main()
