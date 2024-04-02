def my_solution(enroll, referral, seller, amount):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/77486

    summary:
        1) 루트 노드: 민호
          - 다단계 조직: 칫솔 판매 이익 10% 부모에게 전달
            - 수수료도 부모한테 전달하네 ㄹㅇ
        => 개별 구성언의 이익금 리턴

    solution:
        1) O(N*M) 이하
          - 이진 트리가 아님
          - 사전 자료형, 트리 배열 만들기
            - 인덱스: 자기 자신, 배열값: 부모
          - 상납금 & 판매금액 합쳐서 계산하기
    result:
        땡
    """
    enrollment = {v: k + 1 for k, v in enumerate(enroll)}
    enrollment['center'] = 0

    arr = [0] * (len(enroll) + 1)  # 자신의 부모 인덱스 가리킴
    for i, j in enumerate(referral):
        if j == '-':
            arr[i] = 0
            continue
        arr[i + 1] = enrollment[j]

    answer = [0] * (len(enroll) + 1)  # 개별 판매원의 판매 금액 합산
    keys = sorted(enrollment, key=lambda x: enrollment[x], reverse=True)

    selling_book = {}
    for i, j in zip(seller, amount):
        if i in selling_book:
            selling_book[i] += j
        selling_book[i] = j

    for key in keys:
        selling = answer[enrollment[key]]
        if key in selling_book:
            selling += selling_book[key] * 100

        answer[arr[enrollment[key]]] += int(selling * 0.1)
        selling -= int(selling * 0.1)
        answer[enrollment[key]] = selling

    return answer[1:]


def my_solution2(enroll, referral, seller, amount):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/77486

    summary:
        1) 루트 노드: 민호
          - 다단계 조직: 칫솔 판매 이익 10% 부모에게 전달
            - 수수료도 부모한테 전달하네 ㄹㅇ
        => 개별 구성언의 이익금 리턴

    solution:
        1) O(N*M) 이하
          - 이진 트리가 아님
          - 사전 자료형, 트리 배열 만들기
            - 인덱스: 자기 자신, 배열값: 부모
          - 상납금 & 판매금액 합쳐서 계산하기
    """
    relations = dict(zip(enroll, referral))  # 이미 순서가 보장되어 있다
    total = {name: 0 for name in enroll}

    selling_book = {}
    for i, j in zip(seller, amount):
        if i in selling_book.keys():
            selling_book[i] += j
        selling_book[i] = j

    while enroll:
        key = enroll.pop()
        if key in selling_book.keys():
            total[key] += selling_book[key] * 100

        enforce = int(total[key] * (0.1));
        total[key] -= enforce
        if relations[key] != '-':
            parent = relations[key]
            total[parent] += enforce
    answer = list(total.values())
    return answer


def solution(enroll, referral, seller, amount):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/77486

    summary:
        1) 루트 노드: 민호
          - 다단계 조직: 칫솔 판매 이익 10% 부모에게 전달
            - 수수료도 부모한테 전달하네 ㄹㅇ
        => 개별 구성언의 이익금 리턴

    solution:
        1) O(N*M) 이하
          - 이진 트리가 아님
          - 사전 자료형, 트리 배열 만들기
            - 인덱스: 자기 자신, 배열값: 부모
          - 상납금 & 판매금액 합쳐서 계산하기
    """
    relations = dict(zip(enroll, referral))  # 이미 순서가 보장되어 있다
    total = {name: 0 for name in enroll}

    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]

        while money > 0 and cur_name != '-':
            total[cur_name] += money - money // 10
            cur_name = relations[cur_name]
            money //= 10
    return [total[name] for name in enroll]
