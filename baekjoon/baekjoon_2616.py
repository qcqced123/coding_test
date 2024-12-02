import sys


def solution():
    """ 소형 기관차: 최대 N대의 객차, 최대한 많은 손님 태우기, 객차 번호 연속, NlogN
    idea: 부분합
        - 연속 부분 수열의 합이 최대가 되도록
        - total 값에서 현재 limit 으로는 가져갈 수 없는 객차의 승객수를 빼고, 거기서 최대값을 찾는 방식
        - x = N - limit*3
            - x: 데려가지 못하는 객차의 개수
            - 그럼 크기가 x인 부분합을 구하면 되는데, 저걸 어떻게 구하냐고....

    feedback:
        - 그럼 크기가 x인 부분합을 구하면 되는데, 저걸 어떻게 구하냐고.... 이 의문을 이제 dp로 캐싱하면서 해결
        - dp[i][j]: i개의 기관차를 선택하고, j번째 객차까지 고려했을 떄, 최대 승객
            - i: 현재 사용한 소형 기관차 개수
            - j: j번째 객차
    """
    # get the input
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    limit = int(input())

    total = sum(arr)



if __name__ == "__main__":
    solution()
