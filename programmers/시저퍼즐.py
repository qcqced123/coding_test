def solution(s, n):
    """
    implementation:
        1) char2int
          - 소문자: 97 ~ 122
          - 대문자: 65 ~ 90
    """
    answer = list(s)
    for i in range(len(answer)):
        if answer[i] == ' ': continue
        ref = 97 if answer[i].islower() else 65
        new = ref + (ord(answer[i]) - ref + n) % 26
        answer[i] = chr(new)

    return ''.join(answer)
