from aocd.models import Puzzle; import re; import pyperclip as pc; from collections import Counter, defaultdict; import numpy as np
def input():
    puzzle = Puzzle(year=2021, day=13)
    dots = []
    coords,folds = puzzle.input_data.split("\n\n")
    coords = [[int(n) for n in l.split(',')] for l in coords.splitlines()]
    sides = [max([p[0] for p in coords])+1, max([p[1] for p in coords])+1]
    folds = [0 if l.split('=')[0][-1] == 'x' else 1 for l in folds.splitlines()]
    return coords, folds, sides

def main():
    puzzle = Puzzle(year=2021, day=13)
    dots, folds, sides = input()
    o = 0
    print(folds)
    for p in folds:
        sides[p]//=2
        print(sides)
        for i in range(len(dots)):
            if dots[i][p] > sides[p]:
                dots[i][p] -= (dots[i][p] - sides[p]) * 2
    grid = [[0 for i in range(sides[0])] for i in range(sides[1])]
    for p in dots:
        x,y = p
        grid[y][x] = 1
    for r in grid:
        for c in r:
            print("#" if c else " ", end=" ")
        print()

    print(o)
    pc.copy(o)
    # puzzle.answer_b = o

main()
