def solution(answers):
    """
    Problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42840

    O(N) 풀이
    1) answer 길이 측정
    2) 1)의 길이만큼, 1,2,3번 플레이어 정답 생성
        - 슬라이싱 & 나머지 연산
        => 그냥 나머지 연산 사용하면, 굳이 생성 필요 x
    """
    arr = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    answer = [0, 0, 0]
    for i, k in enumerate(answers):
        for j, v in enumerate(arr):
            if k == v[i % len(v)]:  # 나머지 연산 사용: 굳이 개별 플레이어 전체 배열을 생성할 필요가 없다
                answer[j] += 1

    max_value = max(answer)
    result = []
    for i in range(3):
        if answer[i] == max_value:
            result.append(i + 1)

    return result