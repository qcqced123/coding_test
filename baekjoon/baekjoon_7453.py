import sys
import bisect
from collections import Counter
from collections import defaultdict



def solution():
    """ 배열 크기 동일 (인덱스 동일)
    합이 0인 쌍의 개수, 입력이 세로네
    (쌍 카운트 기준: 인덱스)

    idea 1: N**2 + N**2 + N**2
        1) A & B 합의 쌍
        2) 1에서 구한 쌍이랑 C랑 쌍 구하기
        3) 2에서 구한 쌍이랑 D랑 쌍 구하기
            - 합이 0이면 카운트
        => 이렇게 하면 중간에 16,000,000*4,000 이 되고, 시간 터짐
        => 버려,,,,
    """
    input = sys.stdin.readline
    N = int(input())

    A, B, C, D = [], [], [], []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a), B.append(b), C.append(c), D.append(d)

    sum_vocab = defaultdict(lambda: 0)  # convert to dict
    for i in range(N):
        for j in range(N):
            cnt = A[i] + B[j]
            sum_vocab[cnt] += 1

    # 애초에 이렇게 구하면 터지네
    # 여기 안터지게 못함?
    first_arr = list(sum_vocab.keys())
    for i in range(len(first_arr)):  # 합이 하나도 안겹치면 여기가 16,000,000
        for j in range(N):  # 여기 4000
            cnt = first_arr[i] + C[j]
            sum_vocab[cnt] += 1

    result = 0
    for i in range(N):
        cnt = D[i]
        if sum_vocab[0-cnt] > 0:
            result += sum_vocab[0-cnt]

    print(result)


def solution2():
    """
    idea 2: N**2 + N**2
        1) A, B, C, D의 길이가 모두 동일한 특징 살리기
             - A & B, C & D 묶기
             - 왼쪽 배열의 합, 오른쪽 배열의 합 사전
        2) defaultdict 특징 이용
            - 왼쪽 배열의 합을 겉 루프, 왼쪽 배열에서 리턴되는 키값이 오른쪽 배열에 있는지 없는지 검사
            - 오른쪽 배열 역시 해시 구조라서, in 연산 대신 defaultdict 이용해서 key 값 여부 찾으면, 이론상 상수 시간 복잡도

    => 이것도 시간 초과
    """
    input = sys.stdin.readline
    N = int(input())

    left_arr, right_arr = [], []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        left_arr.append((a, b)), right_arr.append((c, d))

    # N**2 iteration
    # initialize the default dict for each array
    left_dict, right_dict = defaultdict(lambda: 0), defaultdict(lambda: 0)
    for i in range(N):
        for j in range(N):
            cnt_left = left_arr[i][0] + left_arr[j][1]
            cnt_right = right_arr[i][0] + right_arr[j][1]

            left_dict[cnt_left] += 1
            right_dict[cnt_right] += 1

    result = 0
    for k, v in left_dict.items():
        if right_dict[-k] > 0:
            result += right_dict[-k]

    print(result)
    return


def solution3():
    """
    idea 3:
        1) make two different sum array
        2) sorting by ascending
        3) count the number by bisect_right - bisect_left
    """
    input = sys.stdin.readline
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    left_arr, right_arr = [], []
    for i in range(N):  # N**2
        for j in range(N):
            cnt_left, cnt_right = arr[i][0] + arr[j][1], arr[i][2] + arr[j][3]
            left_arr.append(cnt_left), right_arr.append(cnt_right)

    result = 0
    left_arr.sort(), right_arr.sort()
    for i in range(len(left_arr)):  # N**2
        l, r = bisect.bisect_left(right_arr, -left_arr[i]), bisect.bisect_right(right_arr, -left_arr[i])  # N
        result += r-l

    print(result)


def solution4():
    input = sys.stdin.readline
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    left_arr, right_arr = [], []
    for i in range(N):  # N**2
        for j in range(N):
            cnt_left, cnt_right = arr[i][0] + arr[j][1], arr[i][2] + arr[j][3]
            left_arr.append(cnt_left), right_arr.append(cnt_right)

    # 카운터 사전에 없는게 키 값으로 들어오면, defaultdict과 마찬가지로, 0으로 바로 초기화 되기 때문에
    # 아래와 같은 로직으로 처리가 가능함
    # N**2
    result = 0
    counter = Counter(right_arr)
    for i in left_arr:
        result += counter[-i]

    print(result)


def solution5():
    input = sys.stdin.readline
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    left_arr, right_arr = [], []
    for i in range(N):  # N**2
        for j in range(N):
            cnt_left, cnt_right = arr[i][0] + arr[j][1], arr[i][2] + arr[j][3]
            left_arr.append(cnt_left), right_arr.append(cnt_right)

    result = 0
    l, r = 0, len(right_arr)-1
    left_arr.sort(), right_arr.sort()
    while l < len(left_arr) and r > -1:
        cnt = left_arr[l] + right_arr[r]
        if cnt > 0:
            r -= 1

        elif cnt < 0:
            l += 1

        else:
            next_l = l + 1
            next_r = r - 1
            # 여기서 그냥 넘어가면, 합이 같은게 여러개 케이스를 못잡음
            # 합이 같은게 여러개 케이스를 잡기 위해서, 같은게 나올 때 까지 루프 반복
            while next_l < len(left_arr) and left_arr[next_l] == left_arr[l]:
                next_l += 1

            while next_r > -1 and right_arr[next_r] == right_arr[r]:
                next_r -= 1

            result += (next_l-l)*(r-next_r)
            l = next_l
            r = next_r

    print(result)


if __name__ == "__main__":
    solution5()
