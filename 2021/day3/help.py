def help(temp, i, f=""):
    while len(temp) != 1:
        c = 0
        for item in temp:
            c += 1 if item[i] == "1" else -1
        F = lambda c,fl: c<0 if fl=="<" else c>=0
        temp, i = list(filter(lambda s: s[i] == ("1" if F(c,f) else "0"),temp)), i + 1
    return temp[0]
def input():
    lines = []
    with open("input.txt") as f:
        L = f.read().splitlines()
        for line in L:
            lines.append(line)
        return lines
