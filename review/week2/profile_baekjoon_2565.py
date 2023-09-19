import sys
try:
    profile
except NameError:
    profile = lambda x: x


@profile
def main():
    N = int(sys.stdin.readline())
    lines = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
    graph = [0] * N

    # 현재와 이전 것을 반복적으로 비교
    for i in range(N):
        tmp_result = 0
        for j in range(i):
            if lines[i][1] > lines[j][1]:
                if tmp_result < graph[j]:
                    tmp_result = graph[j]
        graph[i] = tmp_result + 1
    print(N - max(graph))


if __name__ == "__main__":
    main()
