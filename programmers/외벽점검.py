from itertools import permutations


def solution(n, weak, dist):
    """
    Implementation:
        1) 1시간 이동 거리처리
        2) 이동 방향
        3) 친구들 배치 순서
    """
    length = len(weak)
    answer = len(dist) + 1

    def extend_arr(arr):
        return arr[:] + [i + n for i in arr]

    arr = extend_arr(weak)
    for i in range(length):
        for case in permutations(dist, len(dist)):
            src = 1
            position = arr[i] + case[src - 1]
            for j in range(i, i + length):
                if position < arr[j]:
                    src += 1
                    if src > len(dist):
                        break
                    position = arr[j] + case[src - 1]

            answer = min(answer, src)

    return answer if answer <= len(dist) else -1

