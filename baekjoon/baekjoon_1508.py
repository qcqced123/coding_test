import sys


def solution():
    """
    idea: parametric search
        - 최적화 대상/범위: 심판 사이의 거리, 1, to 10**7
        - 최적화 기준: mid를 최소값으로 유지 하는데 필요한 심판 숫자

    question:
        - 정답이 여러개 되는 경우, 그 중에서 한 개는 찾겠는데, 사전순으로 정렬해서 가장 뒤에꺼 출력하려면, 모든 경우의 다 계산 하라는 거자나,,,
        - K 값이 엄청 작은거 보니까, 백트래킹이나 조합 사용해서 만들어야 하는 것 같은데, 어떻게 코드를 작성할지 감이 안온다
        - 그 숫자 구슬 문제랑 똑같음
        => 이게 되네ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        => 근데 답지 보자, 솔직히 거의 찍어서 맞은거랑 다를바가 없음

    """
    # get input data
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    positions = list(map(int, input().split()))

    # do parametric search
    answer = 0
    ans_seq = ""
    l, r = 1, 10**7
    while l <= r:
        mid = (l+r) // 2
        prev, referee, cache = positions[0], 1, ["1"]
        for pos in positions[1:]:
            cnt = pos - prev
            if cnt < mid:
                cache.append("0")

            else:
                prev = pos
                referee += 1
                cache.append("1")

            if referee >= M:
                break

        if referee >= M:
            l = mid + 1
            answer = mid
            ans_seq = cache

        else:
            r = mid - 1

    result = "".join(ans_seq)
    print(result + ("0"*(K-len(result))) if len(result) != K else result)


if __name__ == "__main__":
    solution()
