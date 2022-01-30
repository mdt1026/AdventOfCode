from input import input; import re; import pyperclip as pc; from collections import Counter

def main():
    data = input()
    data.sort()
    fuel = 0
    mid = data[len(data)//2]
    for h in data:
        fuel += abs(h-mid)
    print(fuel)
    pc.copy(fuel)

main()
