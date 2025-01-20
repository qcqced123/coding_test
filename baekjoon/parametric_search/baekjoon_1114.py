import sys


def solution():
    """
    idea: parametric search
        - 최적화 대상/범위: 가장 긴 조각의 최소값, 0 to L
        - 최적화 기준: 탐색 알고리즘 짜는 것부터 험난함...

    question:
        - 예전에도 비슷하게, 조각 개수를 만들어 내는 문제에서, 최적화 기준 알고리즘 세우다가 엄청 고생했는데, 이번에도 잘모르겠음
            - 식 쓰라고 하면 하기야 하겠는데, 깔끔하게 못 세우겠으니, 이번 기회에 답지를 보자

    feedback:
        - 통나무 뒤쪽부터 자르기, 합을 기준으로 자를지 말지 결정
            - 나 같은 경우는 앞쪽부터 가면서, 길이가 기준값보다 길어지면 자를 생각을 했음
            - 뒤집어서 접근하는게, 더 깔끔
        => 달달 외워도 될정도로 깔끔한 코드라고 생각함

    reference:
        - https://velog.io/@hyungraelee/Python-%EB%B0%B1%EC%A4%80-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-1114%EB%B2%88
    """
    # helper func
    def is_valid(limit: int):
        if longest > limit:
            return 10001, 0

        cnt, count = 0, 0
        for piece in pieces[::-1]:
            cnt += piece
            if cnt > limit:
                cnt = piece
                count += 1
        return count, cnt if count == C else pieces[0]

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    L, K, C = map(int, input().split())
    arr = [0, *sorted(list(map(int, input().split()))), L]
    pieces = [arr[i+1] - arr[i] for i in range(K+1)]
    longest = max(pieces)

    # do parametric search
    answer = INF
    answer_front = INF
    l, r = 0, L
    while l <= r:
        mid = (l+r) // 2
        count, prev = is_valid(mid)
        if count <= C:
            r = mid - 1
            answer = mid
            answer_front = prev

        else:
            l = mid + 1

    print(answer, answer_front)


if __name__ == "__main__":
    solution()
