def solution(numbers):
    """
    Problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/68644

    O(N**2) 풀이
    - 1) 서로 다른 인덱스의 두 개 원소 뽑아 더하기
    - 2) 새로운 배열에 담고, 오름차순 정렬
        - 중복없게, 세트 활용

    최적화 불가능할까??
    """
    answer = []
    length = len(numbers)
    for i in range(length - 1):
        for j in range(i + 1, length):
            answer.append(numbers[i] + numbers[j])

    answer = sorted(set(answer))  # sorted => return list
    return answer

