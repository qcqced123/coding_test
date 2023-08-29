import sys

"""
[시간]
1) 14:20 ~ 14:45

[요약]
1) 유사회문: 한 문자를 삭제하여 회문으로 만들 수 있는 문자열
    => 유사회문인지 아닌지 판단하는 프로그램 작성
2) 주어진 문자열의 길이는 10만, 문자열 개수는 최대 30개
    => 제한 시간이 1초라서 O(n)의 알고리즘을 설계 필요, Counter 사용 불가
[전략]
1) 슬라이싱 이용해서 원본과 뒤집은 문자열을 비교하는 과정에서 걸러내기 (루프 하나만 쓰게 만들 수 있음)
    - 각 자리를 대조하면 가장 처음 다른 문자가 등장하는 지점을 찾아재 해당 문자를 제거함.
    - 제거하는 것도 두가지 케이스가 발생, 둘 중 하나만 만족해도 유사 팰린드롬으로 판정
        => 원본의 문자 제거
        => 역본의 문자 제거

"""
for _ in range(int(sys.stdin.readline())):
    checker1, checker2 = '', ''
    text = sys.stdin.readline().rstrip()
    tmp_pal = text[::-1]
    # pure palindrome
    if text == tmp_pal:
        print(0)
        continue
    # similar palindrome or not
    for i in range(len(text)):
        if text[i] != tmp_pal[i]:
            checker1 = checker1 + text[i+1:]
            checker2 = checker2 + tmp_pal[i+1:]
            break
        checker1 += text[i]
        checker2 += tmp_pal[i]
    if checker1 == checker1[::-1] or checker2 == checker2[::-1]:
        print(1)
    else:
        print(2)




