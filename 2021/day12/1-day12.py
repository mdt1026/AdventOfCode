from aocd.models import Puzzle; import re; import pyperclip as pc; from collections import Counter, defaultdict; import numpy as np
def dfs(visited, graph, node, count, s):
    if node == "end":
        return count+1
    if node not in visited:
        print (s+node)
        if node.islower() or node == "start": visited.add(node)
        for neighbour in graph[node]:
            count = dfs(visited.copy(), graph, neighbour, count, s+" ")
    return count

def main():
    puzzle = Puzzle(year=2021, day=12)
    data = [l for l in puzzle.input_data.splitlines()]
    G = defaultdict(list)
    for p in data:
        p = p.split('-')
        G[p[0]].append(p[1])
        G[p[1]].append(p[0])
    Q, V = ["start"], set()
    o = dfs(V, G, "start", 0, "")

    print(o)
    pc.copy(o)
    puzzle.answer_a = o

main()
