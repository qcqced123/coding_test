import sys
from bisect import bisect_left


def solution():
    """ 연속된 조각으로 판매, 조각의 합이 주문 크기랑 같아야!!
    모든 경우의 수 카운트
    idea: bisect
        - dp로 풀려면, 제약 조건인 피자의 크기가 최대 몇인가를 봐야함
        - 보니까 최대 200만... 이거 못해 못해, 피자 조각 개수가 1000개라면 20억이 되어 메모리 터짐

    1) 피자 배열 두배로 만들기
        - 원형 큐 형태로 만들기 위해
        - 연속된 피자 조각만 선택 가능
    2)  탐색 대상/범위: 피자 조각수, 0 to 2000
        탐색 조건: 현재 조각들의 크기 합이 기준값은 넘는가?
            조각 숫자가 많아질수록, 크기의 합은 커지기 때문
            현재 기준 조각 개수를 이제 a,b에 할당(이중 루프 돌려서 찾자)
            - S >= size: r = mid-1, answer record
            - S < size: l = mid+1
    question:
        - 시간 초과....ㅠ
    """
    # init data structure
    input = sys.stdin.readline
    size = int(input())  # size of ordered pizza
    a_size, b_size = map(int, input().split())  # save size cache
    pizza_a = [int(input()) for _ in range(a_size)]
    pizza_b = [int(input()) for _ in range(b_size)]

    # make circular queue
    pizza_a += pizza_a[:-1]
    pizza_b += pizza_b[:-1]

    # do bisect
    answer = 0
    l, r = 1, a_size + b_size
    while l <= r:
        maxi = 0
        case = 0
        mid = (l+r) // 2  # A+B 합산 숫자
        for i in range(mid+1):
            cnt_a = i  # number of A
            cnt_b = mid-i  # number of B
            if cnt_a > a_size or cnt_b > b_size:
                continue

            # count the correct case
            result_a, result_b = [], []
            if cnt_a:
                for j in range(a_size):
                    result_a.append(sum(pizza_a[j:j+cnt_a]))
            if cnt_b:
                for j in range(b_size):
                    result_b.append(sum(pizza_b[j:j+cnt_b]))

            if not result_a: result_a = [0]*len(result_b)
            if not result_b: result_b = [0]*len(result_a)

            # let's sum
            for y in result_a:
                for x in result_b:
                    maxi = max(maxi, y+x)  # 요게 좀.. 걸리는데
                    if y+x == size:
                        case += 1
        if maxi >= size:
            answer = case
            r = mid - 1
        else:
            l = mid + 1

    print(answer)


def solution2():
    """
    idea:
    """
    # init data structure
    input = sys.stdin.readline
    size = int(input())  # size of ordered pizza
    a_size, b_size = map(int, input().split())  # save size cache

    pizza_a = [int(input()) for _ in range(a_size)]
    pizza_b = [int(input()) for _ in range(b_size)]

    # make circular queue
    pizza_a += pizza_a[:-2]
    pizza_b += pizza_b[:-2]

    # make the sub seq sum array for each pizza type
    # 모든 경우의 수를 카운트해야 해서 세트 쓰면 안된다
    subseq_a, subseq_b = [], []
    for i in range(a_size):
        for j in range(1, a_size+1):
            if i == a_size-1 and j == a_size:
                continue

            subseq_a.append(sum(pizza_a[i:i+j]))

    for i in range(b_size):
        for j in range(1, b_size+1):
            if i == b_size-1 and j == b_size:
                continue

            subseq_b.append(sum(pizza_b[i:i+j]))

    subseq_a.sort()
    subseq_b.sort()

    answer = subseq_a.count(size) + subseq_b.count(size)
    for i in subseq_a:
        cnt = size - i
        idx = bisect_left(subseq_b, cnt)
        if idx < len(subseq_b):
            curr = subseq_b[idx]
            if curr == cnt:
                answer += 1

    print(answer)


if __name__ == "__main__":
    solution2()
