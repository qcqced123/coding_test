import sys
from collections import defaultdict
from bisect import insort_left, bisect_left


def solution():
    """ 두 수의 오차가 K이하 == key로 인정, NlogN, DB CRUD 기능 만들기
    idea: bisect with hash structure
        - data structure: hash
        - sort the key array by ascending
        - answering the question with bisect
        - CRUD:
            - create: use bisect, insert() or make the new arr
            - update:
            - search: use bisect

    feedback:
        - 정렬된 상태의 리스트 원소 삽입: bisect.insort()

    """
    # helper func
    def create(k,v):
        db[k] = v
        insort_left(keys, k)
        return

    def update(k,v) -> None:
        nk = search(k)

        return

    def search(k: int):
        idx = bisect_left(keys, k)
        prev, cnt = idx - 1, idx
        if 0 < idx < len(keys):
            prev_ = abs(k - keys[prev])
            cnt_ = abs(k - keys[cnt])
            if prev_ < cnt_ and prev_ <= L:
                return prev

            elif prev_ == cnt_:
                return None

            elif cnt_ < prev_ and cnt_ <= L:
                return cnt

            else:
                return -1

        elif not cnt and abs(k - keys[cnt]) <= L:
            return cnt
        elif cnt == len(keys) and abs(k - keys[prev]) <= L:
            return prev

        return - 1

    # get input data
    input = sys.stdin.readline
    N, M, L = map(int, input().split())

    # init db (hash)
    db = defaultdict(int)
    for _ in range(N):
        key, value = map(int, input().split())
        db[key] = value

    # sort by ascending for using bisect
    keys = sorted(list(db.keys()))

    # answering the question
    for _ in range(M):
        command_type, *cnt = map(int, input().split())
        if command_type == 1: create(*cnt)
        elif command_type == 2: update(*cnt)
        else:
            pass

def solution2():
    """
    idea:
    """
    return


if __name__ == "__main__":
    solution2()
