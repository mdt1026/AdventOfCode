from input import input; import re; import pyperclip as pc; from collections import Counter

def main():
    d = input()
    for i in range(80):
        ud = d.copy()
        for i in range(8):
            ud[i] = d[i+1]
        ud[6] += d[0]
        ud[8] = d[0]
        d = ud

    c = 0
    for i in range(9):
        c += d[i]
    pc.copy(c)
    print(c)

main()
