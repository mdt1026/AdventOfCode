from input import input; import re; import pyperclip as pc; from collections import Counter; import math; import statistics

def main():
    data = input()
    data.sort()
    fl,fh = 0,0
    avg = statistics.mean(data)
    av1,av2 = math.floor(avg),math.ceil(avg)
    for h in data:
        fl,fh = fl + sum(range(1,abs(h-av1)+1)), fh + sum(range(1,abs(h-av2)+1))
    print(min(fl,fh))

main()
