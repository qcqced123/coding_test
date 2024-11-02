import sys
from collections import defaultdict


def solution(begin, target, words):
    """ 한 번에 철자 한개, 바꾼게 words 안에 있어야 함
    idea: backtracking
        - 바꿀 수 있는 철자 사전 구하기
            - 자리별로 바꿀 수 있는 철자가 다름
    """
    # get dictionary for changing each position
    size = len(begin)
    vocab = defaultdict(set)
    for word in words:
        for j in range(size):
            vocab[j].add(word[j])

    # backtracking
    visited = set()
    answer = sys.maxsize
    sys.setrecursionlimit(10 ** 6)

    def backtracking(curr: str, count: int) -> None:
        nonlocal answer
        if curr == target:
            answer = min(answer, count)
            return

        for i in range(len(begin)):  # 자리값 완전 탐색용
            for j in vocab[i]:
                new = curr[:i] + j + curr[i + 1:]
                if new in words and new not in visited:  # words도 사전 하나 만들자, 그래야 탐색 속도 줄이지
                    visited.add(new)
                    backtracking(
                        new,
                        count + 1,
                    )
                    visited.remove(new)
        return

    backtracking(begin, 0)
    return 0 if answer == sys.maxsize else answer


if __name__ == '__main__':
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
