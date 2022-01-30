def main():
    def input():
        lines = []
        with open("input.txt") as f:
            L = f.read().splitlines()
            for line in L:
                lines.append(line)
            return lines
    data = input()
    c, g, e = [0]*12, "", ""
    for bits in data:
        i = 0
        for bit in bits:
            c[i],i = 1 if bit=="1" else -1, i+1
    for b in c:
        g, e = g + ("1" if b > 0 else "0"), e + ("0" if b > 0 else "1")
    print(g,e, int(g,2) * int(e,2))
main()
