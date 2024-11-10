import sys


def solution():
    """ 연속 구간, NlogN
    idea: two-pointer, binary search
        - 탐색 대상/범위: MaxHP, 1 to 입력의 최대
        - 탐색 조건: 현재 MaxP로 N번째 방까지 클리어 가능?
            - 가능하다면, left forward
            - 불가능하다면, right backward
    question:
        - 41%에서 시간초과
    """
    MONSTER, POTION = 1, 2
    input = sys.stdin.readline
    N, ATTACK = map(int, input().split())  # 방의 개수, 용사 공격력
    rooms = [list(map(int, input().split())) for _ in range(N)]  # 1: 몬스터, 2: 포션

    answer = 0
    l, r = 1, 1000000000000*N
    while l <= r:
        mid = (l+r) // 2
        max_hp, hp, attack = mid, mid, ATTACK
        for room in rooms:
            info, alpha, beta = room  # room information, about attack, about hp
            if info == MONSTER:  # need to while loop
                while hp > 0 and beta > 0:
                    beta -= attack
                    if beta > 0:
                        hp -= alpha

                if not hp > 0:
                    break

            elif info == POTION:
                attack += alpha
                hp += beta
                if hp > max_hp:
                    hp = max_hp

        if not hp > 0:
            l = mid + 1

        else:
            answer = mid
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution()
