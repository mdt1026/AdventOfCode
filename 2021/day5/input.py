import re
def input():
    L = []
    with open("input.txt") as f:
        lines = f.read().splitlines()
        max_x,max_y = 0,0
        for i in lines:
            temp = i.split(" -> ")
            temp = (temp[0].split(","), temp[1].split(","))
            temp = [[int(s) for s in p] for p in temp]
            max_x = temp[0][0] if temp[0][0] > max_x else max_x
            max_y = temp[0][1] if temp[0][1] > max_y else max_y
            max_x = temp[1][0] if temp[1][0] > max_x else max_x
            max_y = temp[1][1] if temp[1][1] > max_y else max_y
            if (temp[0][0] == temp[1][0]):
                L.append((2,temp[0],temp[1]))
            elif (temp[0][1] == temp[1][1]):
                L.append((1,temp[0],temp[1]))
            else: L.append((0,temp[0],temp[1]))

    return L,max_x,max_y
