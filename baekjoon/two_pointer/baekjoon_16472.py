import sys


def solution():
    """ 고양이 번역기: 최대 N개의 종류의 알파벳을 가진 '연속된' 문자열 인식, 인식 가능한 최대 길이 리턴, NlogN
    이건 왜 골드4?? 사람들이 안풀어서 그런듯??
    a b b c a c c b a
    l r
    l   r
      l   r
          l r
          l  r
          l    r (이 떄 최대)

    idea: two pointer with dictionary
        1) 포인터 초기화:
            - 포인터 위치: 나란히
            - 포인터 방향: forward
            - 포인터 이동 조건:
                - <= N: right forward
                - > N: left forward
        2) 캐시용 사전 정의
    """
    def is_valid() -> int:
        count = 0
        for i in cache.values():
            if i:
                count += 1

        return 1 if count <= N else 0

    N = int(input())
    sequence = sys.stdin.readline().rstrip()

    result = 0
    l, r = 0, 0
    cache = {k: 0 for k in set(sequence)}
    cache[sequence[l]] += 1

    while r < len(sequence) - 1:
        next_char = sequence[r+1]
        cache[next_char] += 1
        if not is_valid():
            while not is_valid():
                out = sequence[l]
                cache[out] -= 1
                l += 1
        r += 1
        result = max(result, r - l + 1)

    print(result)


if __name__ == "__main__":
    solution()
