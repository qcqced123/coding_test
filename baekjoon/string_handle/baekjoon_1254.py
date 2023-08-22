import sys

"""
[풀이 시간]
1) 17:00 ~ 17:30

[요약]
1) 규완이가 적어놓고 간 문자열 S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬을 만들려고 한다.
    - 가능한 짧은 문자열을 추가해 펠린드롬을 만들고 싶음
[전략]
1) 그냥 무식 단순 루프 돌리기
"""
text = sys.stdin.readline().rstrip()
result, slicer = 99999, 1

# input is palindrome
if text == text[::-1]:
    result = len(text)
else:
    for i in range(1, len(text)):
        tmp_text = text + text[0:i][::-1]
        if tmp_text == tmp_text[::-1]:
            result = len(tmp_text)
            break
print(result)


