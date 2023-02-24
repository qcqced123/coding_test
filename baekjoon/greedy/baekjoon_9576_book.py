import sys
"""
[핵심 아이디어]
1) 학생들이 입력한 책 인덱스 순서를 끝쪽 기준으로 오름차순 정렬
==> 그럼 계단 형태의 모양이 생기기 때문에 최대한 많은 학생에게 책을 줄 수 있음
==> 13904번 숙제 문제랑 유사한 개념인 듯 
"""
# Input
G = int(sys.stdin.readline())
result_list = []
for i in range(G):
    N, M = map(int, sys.stdin.readline().split())
    book, student, result = [False] * (N+1), [], 0 # Index 주의, 인덱스 맞추려고 N+1로 했구나ㄴ

    for _ in range(M):
        student.append(list(map(int, sys.stdin.readline().split())))
    # student.sort(key=lambda x: x[1])
    student = sorted(student, key=lambda x: x[1])
    print(student)

    for a, b in student:
        for idx in range(a, b+1):
            if not book[idx]:
                result += 1
                book[idx] = True
                break
    print(result)
