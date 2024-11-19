import sys


def solution():
    """ 이게 무슨 문제야 도대체..?
    근데 뭘 탐색 시키냐..? 상자 번호라도 찍어야 되나?
    아무튼 주어진 상자 개수에 가진 도토리 죄다 넣어야 되는거고
    아 최소 공배수

    idea: binary search
        - 근거 1: 입력이 너무 커서 누가 봐도 이분 탐색

    """
    # init data structure
    input = sys.stdin.readline
    N, K, D = map(int, input().split())  # 상자, 규칙, 도토리


if __name__ == "__main__":
    solution()
