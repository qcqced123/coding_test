def solution(s):
    """
    implementation:
        O(N log N) 이하
        0) 양쪽 괄호 없애기
        1) 한 개짜리 찾기
        2) q제일 긴거 찾기
    """
    curr = s[2:-2].split('},{')
    curr.sort(key=lambda x: len(x))  # 길이 기준으로 정렬

    ans = []
    for text in curr:
        cnt = map(int, text.split(','))
        for value in cnt:
            if value not in ans:
                ans.append(value)

    return ans


def solution(s):
    """
    implementation:ㅌㅋ
        O(N log N) 이하
        0) 양쪽 괄호 없애기
        1) 한 개짜리 찾기
        2) 제일 긴거 찾기
    """
    curr = s[2:-2].split('},{')
    curr.sort(key=lambda x: len(x))  # 길이 기준으로 정렬

    ans = {}  # ordered dict
    for text in curr:
        cnt = map(int, text.split(','))
        for value in cnt:
            ans[value] = 0  # 중복검사할 때는 in 연산보다, 사전, 세트 자료형을 사용해보자
    return list(ans)
