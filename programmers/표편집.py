from typing import Tuple, List


def my_solution(n, k, cmd):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/81303

    summary:
       1) 행 선택, 삭제, 복구
         - 파란칸: 행 선택, 한 칸씩
             - U X: 현재 선택칸에서 x칸 위의 행 선택
             - D X: 현재 선택칸에서 x칸 아래의 행 선택
             - C: 삭제, 바로 아래 칸 선택
             - Z: 최근 삭제 칸 복구
    Args:
        n: 처음 행 개수
        k: 처음 선택된 행번호

    implementation:
        O(N**2) 절대 안된다
        1) 입력 명령어를 코드로 바꿔주는 함수
            - 길이에 따라서 명령 구분
        2) 인덱스, 배열값 모두 스택에 넣자
        => 시간 초과 나기도 하고, 에러도 나니까 직접 삭제하고 추가하지 말고 값을 바꾸는 방식으로 가자
        => 슬라이싱 방식이 더 느림
    """
    stack = []
    table = [i for i in range(n)]

    def cmd_convert(c: str, pointer: int):
        """
        return:
            pointer: 현재 위치
        """
        cmd_len, cmd_type, move = len(c), c[0], 0
        if cmd_len == 3:
            dy = {'U': -1, 'D': 1}
            ny = int(c[2]) * dy[cmd_type] + pointer
            return ny

        elif c == 'C':
            stack.append([pointer, table[pointer]])
            table.pop(pointer)
            if pointer == len(table):
                pointer -= 1
            return pointer

        elif c == 'Z':
            vk, v = stack.pop()
            table.insert(vk, v)
            if pointer >= vk:
                pointer += 1
            return pointer

    for command in cmd:
        k = cmd_convert(command, k)

    answer = ['X'] * n
    for i in table:
        answer[i] = 'O'

    answer = ''.join(answer)
    return answer


def solution(n, k, cmd):
    """
    Args:
        n: 처음 행 개수
        k: 처음 선택된 행번호

    implementation:
        배열을 직접 추가하고 삭제하는 것은 런타임 에러 발생 가능성 높음, 인덱싱만으로 삭제 & 추가한 효과 내기
        1) 상대 위치 배열 만들기
            - 아까 인덱싱만으로 구현하는 것을 포기했던 이유가 삭제나 추가할 때 없는 것처럼 만드는게 너무 어려울 것 같아서
            - 이렇게하면, linked-list처럼 양끝 인덱스 연결했다가 끊었다가하면 똑같이 구현할 수 있다.
    """
    stack = []
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]

    k += 1
    for cmd_i in cmd:
        if cmd_i.startswith("C"):
            stack.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]  # 마지막 인덱스 배열 삭제하는 경우 처리

        elif cmd_i.startswith("Z"):
            vk = stack.pop()
            down[up[vk]] = vk
            up[down[vk]] = vk

        else:
            action, num = cmd_i.split()
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]

    answer = ['O'] * n
    for i in stack:
        answer[i - 1] = 'X'

    answer = ''.join(answer)
    return answer