import sys
from collections import defaultdict


class Node:
    def __init__(self, x: int):
        self.x = x
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def set_root(self, x: int):
        self.root = Node(x)

    def find(self, val, x):
        if val is None:
            return False
        elif x.x == val.x:
            return True
        elif x.x > val.x:
            self.find(val.right, x)
        else:
            self.find(val.left, x)

    def insert(self, x: int):
        if self.root is None:
            self.set_root(x)
        else:
            return self.insert_node(self.root, x)

    def insert_node(self, curr, x: int):
        if x < curr.x:
            if curr.left is None:
                curr.left = Node(x)
                curr.left.x.parent = curr
            else:
                self.insert_node(curr.left, x)

        elif x > curr.x:
            if curr.right is None:
                curr.right = Node(x)
                curr.right.x.parent = curr
            else:
                self.insert_node(curr.right, x)

    def delete(self, x):
        """ BST delete ops:
        1) zero child nodes: just delete
            - disconnect edge
            - del instance
        2) one child nodes: delete node and connect deleted node's child to parent node
        3) two child nodes:
            - find successor node (minimum node in right sub node)
                - must be most left node in sub tree
                - it must be no left child
            - copy successor to deleted node
            - delete successor node
            - if successor has no node -> 1)
            - if successor has one node -> 2)
        """
        def find_successor(x):
            if x.left is None:
                return x.left
            else:
                return find_successor(x.left)

        def no_child():
            if x.parent is x.parent.left:
                x.parent.left = None
            else:
                x.parent.right = None
            del x

        def one_child():
            child = x.left if x.left is not None else x.right
            if x.parent is x.parent.left:
                x.parent.left = child
            else:
                x.parent.right = child
            del x

    def preorder(self, x):
        if x is not None:
            print(x.x, end='\n')
            self.preorder(x.left)
            self.preorder(x.right)

    def inorder(self, x):
        if x is not None:
            self.inorder(x.left)
            print(x.x, end='\n')
            self.inorder(x.right)

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


