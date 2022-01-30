def main():
    def input():
        lines = []
        with open("input.txt") as f:
            L = f.read().splitlines()
            for line in L:
                lines.append(line.split(" "))
            return lines

    data = input()
    depth = 0
    horizontal = 0
    aim = 0

    for pair in data:
        if pair[0][0] == "f":
            horizontal += int(pair[1])
            depth += aim * int(pair[1])
        elif pair[0][0] == "d":
            aim += int(pair[1])
        elif pair[0][0] == "u":
            aim -= int(pair[1])

    print(depth)
    print(horizontal)
    print(aim)
    print(depth * horizontal)

main()
