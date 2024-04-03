def solution(phone_book):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42577

    summary:
        1) 한 번호가 다른 번호의 접두어인 경우 확인

    solution:
        1) O(NlogN)
          - A 가 B의 접두어인지 판정
            - 앞에 숫자가 같다는 것
            - 숫자 기준 정렬
              - 자연스럽게 길이별로도 정렬되게 된다
            - 그리고 앞 뒤 단어 판정
    """
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        curr_num, next_num = phone_book[i], phone_book[i + 1]
        if next_num.startswith(curr_num):  # in 연산은 처음 시작이 아니라, 내부에 있기만 하면 True, 함정에 낚일 수 있음
            answer = False
            break
    return answer

