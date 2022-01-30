def main():
    def input():
        lines = []
        with open("input.txt") as f:
            L = f.read().splitlines()
            for line in L:
                lines.append(line)
            return lines

    data, i = input(), 0
    temp = data.copy()
    while len(temp) != 1:
        c = 0
        for item in temp:
            c += 1 if item[i] == "1" else -1
        temp, i = list(filter(lambda s: s[i] == ("1" if c>=0 else "0"),temp)), i + 1

    og, temp, i = temp[0], data.copy(), 0
    while len(temp) != 1:
        c = 0
        for item in temp:
            c += 1 if item[i] == "1" else -1
        temp, i = list(filter(lambda s: s[i] == ("1" if c<0 else "0"),temp)), i + 1
    cs = temp[0]
    print(og, cs, int(og,2) * int(cs,2))
    
main()
