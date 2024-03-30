from typing import Tuple, List


def my_solution(record: List[str]) -> List[str]:
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42888

    summary:
        1) 관리자 창 만들기
            - 들어오기, 나가기. 닉네임 변경
            - 닉네임 중복 허용
            - 식별자: 유저 아이디
        => 모든 기록이 처리 된 이후, 결과 리턴
    args:

    solution:
        1) O(NlogN)이하
          - key: value = 유저 아이디: 닉네임
          - 첫 단어에 맞춰서 동작 수행
            1) enter: 사전에 키-벨류 추가
            2) change: 벨류 수정
            3) leave: 키-벨류 제거
                - 굳이 삭제할 필요 없음, 괜히 런타임 에러만 난다
          - 출력 문자열은 f-string 사용
    """
    answer = []
    user_dict = {}

    for stream in record:
        if stream.startswith('E') or stream.startswith('C'):
            _, uid, nick = stream.split()
            user_dict[uid] = nick

    for stream in record:
        if stream.startswith('E'):
            _, uid, _ = stream.split()
            answer.append(f"{user_dict[uid]}님이 들어왔습니다.")

        elif stream.startswith('L'):
            _, uid = stream.split()
            answer.append(f"{user_dict[uid]}님이 나갔습니다.")

    return answer

