from aocd.models import Puzzle; import re; import pyperclip as pc; from collections import Counter; import numpy as np
def main():
    puzzle = Puzzle(year=2021, day=10)
    data = [l for l in puzzle.input_data.splitlines()]
    q = []
    open = ['(', '[', '{', '<']
    close = {'(':')', '[':']', '{':'}', '<':'>'}
    d = {')':1, ']':2, '}':3, '>':4}
    o = []
    for l in data:
        for c in l:
            if not q:
                q.append(c)
            elif c in open:
                q.append(c)
            elif c == close[q[-1]]:
                q.pop()
            else:
                q = []
                break
        if q:
            q.reverse()
            ts = 0
            for c in q:
                ts = ts*5 + d[close[c]]
            o.append(ts)
        q = []
    o = sorted(o)
    o = o[len(o)//2]
    print(o)
    pc.copy(o)
    puzzle.answer_b

main()
