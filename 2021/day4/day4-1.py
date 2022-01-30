from input import input; import re
def markNum(b,n):
    for r in range(len(b)):
        for c in range(len(b[r])):
            if b[r][c]==n:
                b[r][c]="X"
                return

def isWin(b):
    for r in b:
        if all(n=="X" for n in r):
            return True
    for i in range(5):
        L = []
        for j in range(5):
            L.append(b[j][i])
        if all(n=="X" for n in L): return True

def output(b,n):
    for i in range(5):
        L = []
        for j in range(5):
            L.append(b[j][i])
    s = 0
    for r in b:
        for c in r:
            if c != "X":
                s += c
    print(n*s)

def main():
    data = input()
    nums = list(map(int,data[0].split(",")))
    bl = []
    for b in data[1:]:
        L = []
        for r in b.split("\n"):
            L.append(list(map(int,re.split(' +',r.strip()))))
        bl.append(L)
    for n in nums:
        for b in bl:
            markNum(b,n)
            if isWin(b):
                output(b,n)
                return

main()
