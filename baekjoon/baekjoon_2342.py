import sys


def solution():
    """ 펌프 게임, 두 발은 서로 다른 지점 위치
    발 동시 못 움직임: 이터레이션 한 번에 발 하나만
    이전 위치에 따라서 다음 위치로 가는 에너지가 달라짐: 이동에 가중치
        1) 중앙 to 나머지: 2
        2) 인접 to 인접:
        3) 반대편: 4
        4) 같은 지점: 1

    100,000,000 (NlogN)
    idea: Dynamic Programming (3차원 배열)

    inputs:
        1 2 2 4 0
    """
    def cal_weight(t: int, x: int) -> int:
        """
        Args:
            t (int): target value
            x (int): before value s
        """
        result = 0
        if not x:
            if t: result += 2

        elif not t-x:
            result += 1

        elif abs(t-x) == 2:
            result += 4

        else:
            result += 3

        return result

    *arr, _ = list(map(int, sys.stdin.readline().split()))
    if not len(arr):
        print(0)
        exit()

    cache = [[[sys.maxsize]*5 for _ in range(5)] for _ in range(len(arr)+1)]
    cache[-1][0][0] = 0

    for i in range(len(arr)):
        # move the left foot
        t_pos = arr[i]
        for j in range(5):  # right foot's position
            for k in range(5):  # left foot's position
                l_weight = cal_weight(t_pos, k)
                cache[i][t_pos][j] = min(
                    cache[i][t_pos][j],
                    cache[i-1][k][j] + l_weight  # 여기 때문에 배열 초기화를 저렇게 했구나
                )
        # move the right foot
        for v in range(5):  # left foot's position
            for z in range(5):  # right foot's position
                r_weight = cal_weight(t_pos, z)
                cache[i][v][t_pos] = min(
                    cache[i][v][t_pos],
                    cache[i-1][v][z] + r_weight
                )
    result = sys.maxsize
    for l in range(5):
        for r in range(5):
            result = min(result, cache[-2][l][r])
    print(result)


if __name__ == "__main__":
    solution()
