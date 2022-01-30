from aocd.models import Puzzle; import re; import pyperclip as pc; from collections import Counter, defaultdict; import numpy as np
def dfs(graph, curr, p):
    if curr == "end":
        return 1
    out = 0
    for node in graph[curr]:
        smalls = [c for c in p if c.islower()]
        #print(node,p)
        if node.isupper() or node not in p or max(Counter(smalls).values()) == 1:
        #    print("  valid")
            out += dfs(graph, node, p + [node])
    return out

def main():
    puzzle = Puzzle(year=2021, day=12)
    data = [l for l in puzzle.input_data.splitlines()]
    G = defaultdict(list)
    for p in data:
        p = p.split('-')
        if p[1] != "start" and p[0] != "end": G[p[0]].append(p[1])
        if p[0] != "start" and p[1] != "end": G[p[1]].append(p[0])
    o = dfs(G, "start", [])
    print(o)
    pc.copy(o)
    puzzle.answer_b = o

main()
