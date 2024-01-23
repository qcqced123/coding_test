import sys
from collections import defaultdict


class Node:
    def __init__(self, x: int):
        self.x = x
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def set_root(self, x: int):
        self.root = Node(x)

    def insert(self, x: int):
        if self.root is None:
            self.set_root(x)
        else:
            return self.insert_node(self.root, x)

    def insert_node(self, curr, x: int):
        if x < curr.x:
            if curr.left is None:
                curr.left = Node(x)
            else:
                self.insert_node(curr.left, x)

        elif x > curr.x:
            if curr.right is None:
                curr.right = Node(x)
            else:
                self.insert_node(curr.right, x)

    def postorder(self, x):
        if x is not None:
            self.postorder(x.left)
            self.postorder(x.right)
            print(x.x, end='\n')


sys.setrecursionlimit(10**6)
nodes, tree = [], defaultdict(list)
while True:
    try: nodes.append(int(sys.stdin.readline()))
    except: break

bst = BST()
for i, node in enumerate(nodes):
    if not i:
        bst.set_root(node)
        continue
    bst.insert(node)

bst.postorder(bst.root)



