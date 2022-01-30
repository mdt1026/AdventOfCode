from input import input; import re
def main():
    data,mx,my = input()
    c = 0
    grid = []
    for i in range(my+1):
        grid.append([0]*(mx+1))
    for l in data:
        Mx,mx = max(l[1][0],l[2][0]),min(l[1][0],l[2][0])
        My,my = max(l[1][1],l[2][1]),min(l[1][1],l[2][1])
        if l[0] == 1:
            for i in range(Mx-mx+1):
                grid[My][mx+i] += 1
        elif l[0] == 2:
            for i in range(My-my+1):
                grid[i+my][Mx] += 1
    for r in grid:
        for n in r:
            if n > 1:
                c+=1
    for r in grid:
        print(r)
    print(c)
main()
