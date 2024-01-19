import sys


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
tree = {}

for i in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

for func in [preorder. inorder, postorder]:
    print(func('A'), end='\n')