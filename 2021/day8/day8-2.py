from input import input; import re; import pyperclip as pc; from collections import Counter
def main():
    data = input()
    c=0
    for l in data:
        d = dict()
        q = []
        for n in l[0]:
            if len(n) == 2:
                d[1] = n
            elif len(n) == 3:
                d[7] = n
            elif len(n) == 4:
                d[4] = n
            elif len(n) == 7:
                d[8] = n
            else: q.append(n)
        t = [c for c in d[7] if c not in d[1]][0]
        n = list(t + d[4])
        d[9] = [i for i in q if all(False for j in n if j not in i)][0]
        q.remove(d[9])
        b = [c for c in d[9] if c not in list(t+d[4])][0]
        d[0] = [i for i in q if len(i) == 6 and all(False for j in d[7] if j not in i)][0]
        q.remove(d[0])
        d[6] = [i for i in q if len(i) == 6][0]
        q.remove(d[6])
        d[3] = [i for i in q if all(False for j in d[7] if j not in i)][0]
        q.remove(d[3])
        d[5] = [i for i in q if all(False for j in i if j not in d[6])][0]
        q.remove(d[5])
        d[2] = q.pop(0)
        d = dict((v,k) for k,v in d.items())
        o = ""
        for n in l[1]:
            o += str(d[n])
        c += int(o)

    print(c)
    pc.copy(c)

main()
