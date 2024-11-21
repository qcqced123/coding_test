import sys


def solution():
    """ 읽을 수 있는 단어 최대값
    idea: backtracking
        - 입력이 작고, 모든 경우의 수 고려할 필요가 있음
        - a, t, n, i, c 는 반드시 K개의 철자에 들어가야 한다
            - 따라서 K가 5 이하, 무조건 0
    question:
        - 5% 시간초과
        - 다른 사람들 풀이 확인하자

    optimization point:
        1) 애초에 공통 문자열 빼고 백트래킹
        2) 스택 내부, 슬라이싱 하는 부분 죄다 빼기
        3) 루프 대신 집합 연산으로 vocab 커버 여부 확인
        => 이래도 5% 초과

    feedback:
        - 세트 대신에, 배열 + 인덱싱으로 로직 변경

    """
    # backtracking func
    sys.setrecursionlimit(10**6)
    def backtracking(idx: int, vocab: set, count: int) -> None:
        nonlocal answer
        i = idx
        while i < N:
            new_vocab = vocab
            cache = new_arr[i].difference(new_vocab)
            if len(new_vocab) + len(cache) <= K:
                new_vocab = new_vocab.union(cache)
                backtracking(i+1, new_vocab, count + 1)

            i += 1

        answer = max(answer, count)

    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    vocab = {"a", "t", "n", "i", "c"}
    new_arr = [set(s[4:-4]) for s in arr]

    # edge handling
    if K < 5:
        print(0)
        return

    elif K >= 26:
        print(N)
        return

    # do backtracking
    answer = 0
    backtracking(0, vocab, 0)
    print(answer)


def solution2():
    # backtracking func
    sys.setrecursionlimit(10**6)
    def backtracking(idx: int, nums: int, count: int) -> None:
        nonlocal answer
        i = idx
        while i < N:
            cache = []
            for cnt in new_arr[i]:
                if not vocab[ord(cnt) - ord("a")]:
                    cache.append(cnt)

            if len(cache) + nums <= K:
                for cnt in cache:
                    vocab[ord(cnt) - ord("a")] = 1
                backtracking(i+1, nums+len(cache), count+1)

                for cnt in cache:
                    vocab[ord(cnt) - ord("a")] = 0
            i += 1

        answer = max(answer, count)

    input = sys.stdin.readline
    N, K = map(int, input().split())
    vocab = [0]*26
    arr = [input().rstrip() for _ in range(N)]
    new_arr = [set(s[4:-4]) for s in arr]
    for c in ["a", "t", "n", "i", "c"]:
        vocab[ord(c) - ord("a")] = 1

    # edge handling
    if K < 5:
        print(0)
        return

    elif K == 26:
        print(N)
        return

    # do backtracking
    answer = 0
    backtracking(0, 5, 0)
    print(answer)


if __name__ == "__main__":
    solution2()
