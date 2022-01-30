from input import input; import re; import pyperclip as pc; from collections import Counter
def main():
    data = input()
    c=0
    for l in data:
        for n in l[1]:
            c = c + (1 if (len(n) in range(2,5) or len(n) == 7) else 0)
    print(c)
    pc.copy(c)

main()
