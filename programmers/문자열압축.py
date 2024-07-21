def solution(s):
    """
    implementation
        1) 압축 문자열 최대 길이: len(s) // 2
        2) 어떤 문자열로 압축할거야??
        3) 선택한 문자열은 전체 문자열 어디에 있을까?
        4) 압축한 문자열들 비교
    """
    answer = len(s)  # 압축 못하면 원본 길이 리턴하도록
    for x in range(1, answer//2 +1):  # 선택 문자열 길이
        comp_len = 0  # compare var
        comp = ''
        cnt = 1
        for i in range(0, len(s)+1, x):  # 전체 문자열에서 선택 문자 찾기, 마지막 문자열 결과도 처리해야하니까 +1 해줘야겠네
            curr = s[i:i+x]
            if curr == comp:
                cnt += 1
            else:
                comp_len += len(curr)
                if cnt > 1:
                    comp_len += len(str(cnt))  # 두자리수 이상 압축 문자열이 등장하는 경우 때문에, 길이 측정해서 더해야 한다
                cnt = 1
                comp = curr
        answer = min(answer, comp_len)
    return answer
