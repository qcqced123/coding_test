def my_solution(s):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12973

    [요약]
    1) 소문자 문자열
        - 같은 알파벳 2개 붙어 있는 짝 찾기
        - 제거
        - 앞뒤 이어 붙이기
        - 완벽히 다 없애면 1, 아니면 0
    [결과]
    1) 통과
        - 같은 알파벳 2개만 제거, pop() 이용
        - pop() 안 쓰고, 리스트 슬라이싱 & 복사해서 처음에 시간초과 났음
    """
    stack = []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
            continue
        stack.pop()
    answer = 1 if not stack else 0
    return answer
