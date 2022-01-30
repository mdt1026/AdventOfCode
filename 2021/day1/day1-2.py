
def main():
    def input():
        L = []
        with open("input.txt") as f:
            lines = f.read().splitlines()
            for i in lines:
                L.append(int(i))
        return L


    lines = input()
    depths = lines

    prev1 = depths[2]
    prev2 = depths[1]
    prevSum = depths[0] + prev1 + prev2
    count = 0
    for depth in depths[3:]:
        print(prev2, prev1, depth)
        newSum = depth + prev1 + prev2
        if newSum > prevSum:
            count += 1
        prev2 = prev1
        prev1 = depth
        prevSum = newSum
    print(count)

main()
