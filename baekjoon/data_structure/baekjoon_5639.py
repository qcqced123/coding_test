import sys


def solution():
    sys.setrecursionlimit(10**6)
    nodes = []
    while True:
        try: nodes.append(int(sys.stdin.readline()))
        except: break

    def postorder(src, end):
        if src > end:
            return

        root = nodes[src]
        new_end = end + 1
        for i in range(src+1, end+1):
            if nodes[i] > root:
                new_end = i
                break
        postorder(src+1, new_end-1)
        postorder(new_end, end)
        print(root)

    postorder(0, len(nodes)-1)


if __name__ == '__main__':
    solution()

