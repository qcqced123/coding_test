import sys


def solution():
    """ 사정 거리 안쪽 동물 숫자, NlogN
    idea: binary search
        - 전체 사대 중에서, 한번이라도 잡을 수 있다면, 카운트
        - 동물별로 전체 사대에 대해서 잡을 수 있는지 설계를 해야함
        - 탐색 대상/범위: 현재 사정거리 값 배열, 0 to L
    question:
        - 사정거리랑 거리를 비교: 거리를 구하려면 사대별 & 동물 위치를 파악해야함, 이게 10만**2
        - 동물 숫자 배열을 이진 탐색해도, 어차피 10만**2를 피할 수 없음
        - 사대 위치에 대해서 탐색을 시키려고 해도... 그게 포인터 이동 조건 세팅이 안되서 힘듦

    feedback:
        - 탐색 대상/범위: 사로 배열 (사로 값이 아닌, 인덱스)
            - 인덱스를 포인터로 잡았으면, 쉽게 풀렸을텐데, 여태까지 죄다 원소값을 포인터로 잡는 문제만 풀어서 생각도 못함
            - 그래서 탐색 대상이 1억 이상이 안나오게 만들었구나, 인덱스를 탐색해야 하니까 배열을 직접 선언할 필요가 있어서
            - 1억 넘어가면 메모리 터지니까, 그래서 탐색 대상을 10만대로 제한한거였어... 이건 생각도 못했네

    """
    input = sys.stdin.readline
    M, N, L = map(int, input().split())  # 사대, 동물, 사저어리

    gun_pos = list(map(int, input().split()))
    gun_pos.sort()

    answer = 0
    animal_pos = [list(map(int, input().split())) for _ in range(N)]
    for x, y in animal_pos:
        l, r = 0, len(gun_pos) - 1
        mini = x + y - L  # 잡을 수 있는 사로의 최소값, L이 사정거리의 최대값이니까
        maxi = x - y + L  # 잡을 수 있는 사로의 최대값
        while l <= r:
            mid = (l+r) // 2
            cnt = gun_pos[mid]
            if mini <= cnt <= maxi:
                answer += 1
                break

            elif cnt > maxi:
                r = mid - 1

            else:  # if cnt < mini
                l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
