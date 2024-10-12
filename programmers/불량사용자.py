import sys


def solution(user_id, banned_id):
    """ 어뷰징 찾기, 마스킹, 마스킹 때문에 경우의 수 발생
    idea 1: BF (x)

    idea 2: back tracking
        1) 제제 리스트의 경우의 숫자를 세어야 해서
        2) 스택 초기화
            - 스택 종료 조건: current value == len(banned_id)
            - 다음 스택 호출 조건: 현재 banned_id, uid가 같을 때

    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/64064
    """
    def detect(bid: list, uid: list, curr: list, count):
        """
        Args:
            bi (int): index of banned_id
            count (int): value of answer
        """
        # end point of stack
        if count == len(banned_id):
            curr.sort()
            answer.add(tuple(curr))
            return

        for i in range(len(bid)):  # 마스킹 사전
            for j in range(len(uid)):  # 현재 남은 유저 리스트
                cnt_banned, cnt_uid = bid[i], uid[j]
                if len(cnt_banned) == len(cnt_uid):  # 스택 호출 조건 1: 길이 같을때
                    for k in range(len(cnt_banned)):
                        if (cnt_banned[k] != cnt_uid[k]) and cnt_banned[k] != "*":
                            break
                    else:
                        detect(
                            bid[:i] + bid[i + 1:],
                            uid[:j] + uid[j + 1:],
                            curr[:] + [cnt_uid],
                            count + 1
                        )
            return  # 현재 스택에서 더 이상 탐색할 필요가 없음

    answer = set()
    sys.setrecursionlimit(10 ** 4)
    detect(banned_id, user_id, [], 0)

    return len(answer)


if __name__ == '__main__':
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"]
    )
