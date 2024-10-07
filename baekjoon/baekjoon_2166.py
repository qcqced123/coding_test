import sys


def solution():
    """
    idea: 신발끈 공식
        1) 시계, 반시계 방향 좌표 정렬
            - 다각형을 이루는 순서대로 좌표를 준다고 나와있구나
        2) 신발끈 공식 이용
            - 반드시 좌표는 다각형을 이루는 순서대로 정렬되어 있어야 한다
            - 예를 들어 시계방향, 반시계 방향
            - 반드시 arr의 마지막에 첫번째 좌표를 다시 넣어줘야 한다
    """
    input = sys.stdin.readline
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.append(arr[0])

    l, r = 0, 0
    for i in range(len(arr)-1):
        l += arr[i][0]*arr[i+1][1]
        r -= arr[i+1][0]*arr[i][1]

    print(round(1/2*abs(l+r), 1))


if __name__ == "__main__":
    solution()
