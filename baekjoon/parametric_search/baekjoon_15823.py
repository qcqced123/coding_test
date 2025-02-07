import sys


def solution():
    """ <= NlogN
    idea: parametric search with two pointer
        [two pointer]
        - 포인터 위치:
        - 포인터 방향:
        - 포인터 이동 방향:

        [parametric search]
        - 최적화 대상/범위: 카드팩을 구성하는 최대 카드 개수, 1 to int(N//M)
        - 최적화 기준: 현재 카드팩 개수 vs M

        [hash]
        - 단일 카드팩의 데이터 유일성 검사용

    feedback:
        - 현재 탐색에 실패 했을 떄, 다음 탐색을 시작할 위치를 미리 캐싱할 변수를 두는 방식으로 해결
        - 나도 해시에 인덱스를 기록할 생각까지 했었는데, 차이가 났던 부분은, 애초에 루프 길이를 mid 만큼만 돌리게 하면, 인덱스 업데이트 문제에서 자유로울 수 있다는걸 간과함
          - 나 같은 경우는 전체 배열 길이만큼 루피 길이를 설정했었고, 그럼 해시 내부 인덱스 업데이트가 일괄적으로 일어나야 하는데, 그게 선형 시간을 잡아먹기 때문에, 솔루션 만들기를 포기했었
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 카드 개수, 반드시 사야 되는 카드팩 개수
    arr = list(map(int, input().split()))

    # do parametric search with two-pointer algorithm
    answer = 0
    l, r = 1, int(N//M)
    while l <= r:
        mid = (l+r) // 2  # current standard value
        cnt, cache = 0, 0  # current value of card pack, next starting point
        while mid + cache <= N:
            pack = dict()
            for i in range(cache, cache+mid):  # 애초에 mid 개만 판정 가능하게 루프 길이를 mid로 한정, 그럼
                curr = arr[i]
                if curr not in pack:
                    pack[curr] = i

                else:
                    cache = pack[curr] + 1
                    break
            else:
                cnt += 1
                cache += mid

        if cnt >= M:
            answer = mid
            l = mid + 1
        else:
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution()
