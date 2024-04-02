def solution(n: int, a: int, b: int):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12985

    solution:
        1) 다음 라운드는 번호가 이전 라운드의 절반
          - A, B가 만났다면, 다음 라운드 숫자가 동일하다는 점을 이용
        => 이게 발상을 떠올리기 쉽지 않음
    """
    answer = 0
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        answer += 1

    return answer