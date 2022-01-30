from aocd.models import Puzzle; import re; import pyperclip as pc; from collections import Counter; import numpy as np
def main():
    puzzle = Puzzle(year=2021, day=11)
    L = [l for l in puzzle.input_data.splitlines()]
    data = [[0]*12]
    for r in L:
        row = [0]
        for n in r:
            row.append(int(n))
        data.append(row + [0])
    data.append([0]*12)
    o = 0
    x = 0
    while True:
        x += 1
        for i in range(1,len(data)-1):
            for j in range(1,len(data[i])-1):
                data[i][j] += 1
        f = []
        while True:
            c = 0
            for i in range(1,len(data)-1):
                for j in range(1,len(data[i])-1):
                    if (i,j) not in f and data[i][j] > 9:
                        f.append((i,j))
                        data[i-1][j-1] += 1
                        data[i][j-1] += 1
                        data[i+1][j-1] += 1
                        data[i-1][j] += 1
                        data[i+1][j] += 1
                        data[i-1][j+1] += 1
                        data[i][j+1] += 1
                        data[i+1][j+1] += 1
                        c += 1
            if not c: break
        # print()
        for p in f:
            data[p[0]][p[1]] = 0
            o += 1
        if len(f) == 100: puzzle.answer_b = x; break

    print(x)
    pc.copy(o)
    # puzzle.answer_a = o

main()
