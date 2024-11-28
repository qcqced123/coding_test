import sys


def solution():
    """ 정해진 그리드에 "최소" 가로선을 추가
    자료 구조를 뭘 써야되냐
    idea: backtracking
        - 인접 그래프 비슷하게 생각하면 될 것 같은데
    feedback:
        - 자료구조: 2D array
            - [[0]*N for _ in range(H)]
    """
    # init data structure
    input = sys.stdin.readline
    N, M, H = map(int, input().split())


if __name__ == "__main__":
    solution()
