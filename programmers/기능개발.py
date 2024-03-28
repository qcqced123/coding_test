import math
from collections import deque


def my_solution(progresses, speeds):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42586

    summary:
        1) 기능 개발 순서
          - 개발 완료 순서는 다른데, 배포는 순서대로 해야함
    Args:
        progresses: 현재 진도
        speeds: speed per day

    solution:
        시간 복잡도 신경 안써도 될 듯
        1) progresses 자체를 큐로 생각

    result:
        통과

    point:
        1) 입력 리스트 자체를 큐로 생각하면 쉽게 풀림
        2) 다만, iterable 객체는 슬라이싱의 경우에 없는 번호를 넣어도 에러가 발생하지 않는 것이지, 인덱싱의 경우는 인덱싱 에러가 발생한다
    """
    answer = []
    progress_q, speed_q = deque(progresses), deque(speeds)
    while progress_q:
        for i in range(len(progress_q)):
            progress_q[i] += speed_q[i]

        cnt = 0
        while progress_q and progress_q[0] >= 100:  # 조건을 이렇게 붙여야 하는구나, 슬라이싱이 에러가 안나는거지 인덱싱은 없는 인덱스 찾으면 인덱싱 에러가 발생한다
            progress_q.popleft(), speed_q.popleft()
            cnt += 1

        if cnt:
            answer.append(cnt)

    return answer


def solution(progresses, speeds):
    """ 애초에 베포 가능일 미리 계산
    1) 개별 기능마다 베포 가능일 계산
    2) 가장 처음 배포 날짜를 기준, 베포 가능일 배열을 순회
        - 이 방식이 큐 동작이랑 뭔 상관인지 잘 모르겠음
    """
    answer = []
    n = len(progresses)
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

    count = 0
    max_days = days_left[0]  # 첫 베포 시작일
    for i in range(n):
        if days_left[i] <= max_days:
            count += 1

        else:
            answer.append(count)
            count = 1
            max_days = days_left[i]

    answer.append(count)
    return answer


if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))