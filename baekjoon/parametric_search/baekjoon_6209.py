import sys


def solution():
    """
    idea: parametric search
        - 탐색 대상/범위: 점프 최소 거리 배열, 1 to d
        - 탐색 기준: mid 값을 현재 경우의 수에서 거리의 최소로 만들기 위해서 몇 개의 돌을 빼야 하는가

    question:
        - 기존 파라매트릭 서치랑 똑같이 풀되, 뺀 돌의 개수가 정확히 m이랑 같을 때만, 정답값을 업데이트 하도록 했는데, 왜 틀릴까..ㅠ

    feedback:
        - 저격 당해버렸구나,,,,, ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        - 반드시 모든 돌을 밟아야 한다는 조건 때문에, 제거한 돌의 개수가 조건과 같을 때만, 정답을 업데이트 하도록 해서 틀림
        - 왜일까...? 왜 작거나 같은 경우도 정답을 업데이트 하도록 만들어야
        - 도대체 왜... 덜 뺀 것도 정답을 업데이트 하도록 만들어야, 맞는걸까...?
        - 하긴 그냥 일반 파라매트릭 서치처럼 풀고, 돌 개수를 기준보다 적게 빼도, 그냥 아무거나 빼버렸다고 가정하면 되겠구나
        - 내가 저 조건 넣을때 걱정했던 것도, 빼먹는 경우가 생길 수도 있어서 였으니까!
        - 그냥 일반 파라매트릭 서치처럼 풀고, 돌을 아무거나 빼버렸다고 가정하면 되니까!, 굳이 정확히 돌 개수를 맞출 필요가 없음
    """
    # get input data
    input = sys.stdin.readline
    d, n, m = map(int, input().split())
    stones = [int(input()) for _ in range(n)] + [d]
    stones.sort()

    # do parametric search
    answer = 0
    l, r = 0, d
    while l <= r:
        mid = (l+r) // 2
        prev, del_stones = 0, 0
        for stone in stones:
            cnt = stone-prev
            if cnt < mid:
                del_stones += 1
            else:
                prev = stone

            if del_stones > m:
                break

        if del_stones > m:
            r = mid - 1

        else:
            answer = mid  # 빼야 되는 돌 개수보다 작아도, 그냥 아무거나 뺐다고 간주해버리면 되기 때문에, 작은 경우도 답을 업데이트 해야함
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
