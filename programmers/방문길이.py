from typing import List


def my_solution(dirs: str):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/49994

    [요약]
    1) 이동 명령 배열에 따라 이동
        - 이동하면서, 처음 걸어본 길의 길이 구하기
        - 좌표 경계 넘어가는 명령은 무시
    [풀이]
    1) visit 배열 만들기
        - 시작2끝, 끝2시작 모두 만들기
    => O(N*K) (K는 세트 자료형 길이)
    => 그리드 사이즈가 고정되어 있기 떄문에, 시간 복잡도를 신경 쓸 필요가 없다
    => 생각해보면, 굳이 현재 좌표가 있는지 없는지 검사할 필요가 없음, 어차피 세트는 무조건 중복을 없애기 때문에
    """
    visit = set()
    moves = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    answer = 0
    y, x = 0, 0
    for dir in dirs:
        vd = moves[dir]
        ny, nx = dy[vd] + y, dx[vd] + x
        if -6 < ny < 6 and -6 < nx < 6:
            if (y, x, ny, nx) not in visit and (ny, nx, y, x) not in visit:
                visit.add((y, x, ny, nx)), visit.add((ny, nx, y, x))
                answer += 1
            y, x = ny, nx

    return answer


def solution(dirs: str):
    """ 세트는 중복 허용 X인 점을 최대한 이용
    1) 굳이 세트 안에 현재 좌표가 들어 있는지 찾을 필요 없음

    [결과]
    1) 역시 이렇게 푸는게, 불필요한 선형 탐색이 사라져서 훨씬 빠르다
    """
    visit = set()
    moves = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    y, x = 0, 0
    for dir in dirs:
        vd = moves[dir]
        ny, nx = dy[vd] + y, dx[vd] + x
        if -6 < ny < 6 and -6 < nx < 6:
            visit.add((y, x, ny, nx)), visit.add((ny, nx, y, x))
            y, x = ny, nx
    return len(visit) // 2
