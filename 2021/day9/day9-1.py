from input import input; import re; import pyperclip as pc; from collections import Counter
def main():
    data = input()
    rl = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            L = list((data[i-1][j], data[i][j-1], data[i+1][j], data[i][j+1]))
            rl = rl + (data[i][j]+1 if all(True if data[i][j] < n else False for n in L) else 0)

    print(rl)
    pc.copy(rl)

main()
