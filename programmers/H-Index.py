from bisect import bisect_left


def solution(citations):
    """
    idea: sorting with bisect
        1) 배열 정렬
        2) 배열에서 최대값 찾기
        3) 최대값 기준으로 선형 탐색
            - citations 배열에 루프 리턴값을 이진 탐색 수행

    ** 배열값을 기준으로 찾으면 안됨
    ** 예제는 우연히 배열값이 상황에 맞아 떨어져서 풀림
    """
    answer = 0
    citations.sort()
    size = len(citations)

    for i in range(citations[-1]):
        idx = bisect_left(citations, i)
        if i <= size - idx:
            answer = max(answer, i)

    return answer


if __name__ == '__main__':
    solution([3, 0, 6, 1, 5])
