from input import input; import re; import pyperclip as pc; from collections import Counter; import numpy as np
def main():
    data = input()
    q = []
    open = ['(', '[', '{', '<']
    close = {'(':')', '[':']', '{':'}', '<':'>'}
    d = {')':3, ']':57, '}':1197, '>':25137}
    o = 0
    for l in data:
        for c in l:
            if not q:
                q.append(c)
            elif c in open:
                q.append(c)
            elif c == close[q[-1]]:
                q.pop()
            else:
                o += d[c]
                break
        q = []

    print(o)
    pc.copy(o)

main()
