import sys


def solution(k, room_number):
    """ 방 배정, 신청한 순서, N 이하
    rule:
        1) 비어있으면, 바로 배정
        2) 차있으면, 빈 방 중에서 가장 번호가 작은거

    idea 1: hash
        1) 입력을 해시로 변환해 충돌 나는지 확인

    idea 2: hash + bisect (실패)

    idea 3: hash + recursive call
        - 사전: 본인과 겹치는게 들어오면, 어떤 방을 예약해야 하는지 알려주는 용도 (겹치는 애가 다음 방이 어딘지를 알려주는 용도로 사전 사용)
        - 리스트: 정답 출력

    review point:
        - 나는 첨에 해시의 벨류값을 허튼곳에 썼지만, 답지는 벨류 역시 버리지 않고 아껴서 썼구나

    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/64063
    """

    def reserve(x: int):
        if x not in room:
            room[x] = x + 1
            return x

        empty = reserve(room[x])
        room[x] = empty + 1
        return empty

    sys.setrecursionlimit(10**6)
    # init data structure
    room = {}
    answer = []
    for num in room_number:
        result = reserve(num)
        answer.append(result)
    return answer


if __name__ == '__main__':
    print(solution(10, [1, 3, 4, 1, 3, 1]))