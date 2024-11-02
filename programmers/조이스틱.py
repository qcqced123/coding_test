def solution(name):
    """
    idea: greedy
        - 횡방향: 첫 선택 때, 결정한대로 쭉 가야함 (x)
        - 종방향: 원소마다 결정 (0)

    feedback:
        - 횡방향 선택 알고리즘을 잘못짬
    """

    def count_row(t: str):
        """종방향 결정"""
        up = ord(t) - ord("A")
        down = ord("Z") - ord(t) + 1
        return down if up > down else up

    def count_col():
        """횡방향 결정"""
        cnt = 0
        return cnt

    size = len(name)
    answer = 0
    answer += count_col() if size > 1 else 0

    for c in name:
        if c != "A":
            answer += count_row(c)

    return answer


def solution2(name):
    answer = 0
    size = len(name)
    min_move = size - 1  # 이건 어디다 쓰려고?

    # 글자 하나씩 탐색하도록 만드네
    def count_row(t: str):
        """종방향 결정"""
        up = ord(t) - ord("A")
        down = ord("Z") - ord(t) + 1
        return down if up > down else up

    for idx, char in enumerate(name):
        answer += count_row(char)  # 종방향 최적값

        next_idx = idx + 1  # A가 아니라, 바꿔야 하는 문자의 위치를 찾기 위함
        while next_idx < size and name[next_idx] == "A":
            next_idx += 1

        min_move = min(
            min_move,  # 현재 방향 그대로 가는거 (default: right)
            2*idx + size - next_idx,  # 왔던 방향에서 되돌아 가는거 (오른쪽으로 가다가 왼쪽으로 선회)
            idx + 2*(size-next_idx)  # 왼쪽으로 가다가 오른쪽으로 선회
        )
    answer += min_move
    return answer


if __name__ == '__main__':
    data = ["JEROEN", "JZAAAAAAADA"]
    for s in data:
        print(solution(s))
