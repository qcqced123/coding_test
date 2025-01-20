import sys
from bisect import bisect_left
from collections import deque, defaultdict



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
    """
    # helper func
    def create(arr, k, v) -> None:
        db[k] = v
        idx = bisect_left(arr, k)
        if not idx: arr.appendleft(k)
        elif idx == len(arr): arr.append(k)
        else: arr.insert(idx, k)

    def update(k, v) -> None:
        result, nk = search(k)
        if result == 1:
            db[nk] = v

    def search(x: int):
        lower, upper = x-L, x+L
        lx, ux = bisect_left(keys, lower), bisect_left(keys, upper)
        if not ux-lx and not db[keys[lx]]:
            return -1, None

        if (not ux-lx and db[keys[lx]]) or ux-lx == 1:
            return 1, keys[lx]

        if ux-lx > 1:
            return "?", None

    # get input data
    input = sys.stdin.readline
    N, M, L = map(int, input().split())

    # init db (hash)
    db = defaultdict(int)
    for _ in range(N):
        key, value = map(int, input().split())
        db[key] = value

    # sort by ascending for using bisect
    keys = list(db.keys())
    keys.sort()

    # answering the question
    for _ in range(M):
        command_type, *cnt = map(int, input().split())
        # create the new data instance
        if command_type == 1: create(keys, *cnt)

        # update the current data instance in db
        elif command_type == 2: update(*cnt)

        # search the current data instance in db
        else:
            answer, nv = search(*cnt)
            if answer == -1 or answer == "?":
                print(answer)
            elif answer == 1:
                print(db[nv])


if __name__ == "__main__":
    solution()
