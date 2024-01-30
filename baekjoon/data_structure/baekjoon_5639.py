import sys
from collections import defaultdict


sys.setrecursionlimit(10**6)
nodes, tree = [], defaultdict(list)
while True:
    try: nodes.append(int(sys.stdin.readline()))
    except: break

nodes.sort()

