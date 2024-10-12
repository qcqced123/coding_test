import sys


def solution(word):
    """ 길이 5이하 모든 단어 수록, A ~ UUUUU (A, E, I, O, U)
    주어진 단어가 사전에서 몇 번째??

    idea: recursive call
        1) 사전순 수열 만들기 문제랑 똑같음
            - 종료조건: 문자열 길이 5 되면
            - 탐색 조건: 다음 문자열

    A, AA, AAA, AAAA, AAAAA

    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/84512
    """
    strs = ["A", "E", "I", "O", "U"]
    sys.setrecursionlimit(10 ** 6)

    vocab = []

    def recursive(curr: str, p: int):
        cnt = 0
        vocab.append(curr)
        for i in range(5 - p):
            while cnt < 5:
                recursive(curr + strs[cnt], p + 1)
                cnt += 1
        return

    recursive("", 0)
    answer = vocab.index(word)
    return answer


if __name__ == '__main__':
    print(solution("UUUUU"))
