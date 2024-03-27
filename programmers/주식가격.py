def solution(prices):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42584

    summary:
        1) 초단위 주식가격 배열
          - 가격이 떨어지지 않은 기간 구하기

    implementation:
        모르겠는데?? 어떻게 푸냐 이거
        O(NlogN) 이하
        1) stack 활용
          - 인덱스를 넣는 경우도 생각해두자
          - 주식 가격이 떨어진 경우가 서로 곧장 붙어 있지 않은 경우도 있기 때문에 정확한 길이를 정해주려면 인덱스끼리 빼야한다
    """
    stack = []
    total = len(prices) - 1
    answer = [0] * len(prices)
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            vd = stack.pop()
            answer[vd] = i - vd

        stack.append(i)

    while stack:
        vt = stack.pop()
        answer[vt] = total - vt

    return answer