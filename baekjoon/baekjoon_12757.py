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
    def create(k,v):
        db[k] = v
        idx = bisect_left(keys, k)
        if not idx:
            keys.appendleft(k)
            return None

        elif idx == len(keys):
            keys.append(k)
            return None
        else:
            new = deque(keys[:idx] + [k] + keys[idx:])  # 어차피 이 친구 때문에 시간 복잡도 터질듯, 답지 보자
            return new

    def update(k,v) -> None:
        idx = search(k)
        if idx is not None:
            db[keys[idx]] = v

    def search(k: int):
        idx = bisect_left(keys, k)
        prev, cnt = idx-1, idx
        if 0 < idx < len(keys):
            prev_ = abs(k-keys[prev])
            cnt_ = abs(k-keys[cnt])
            if prev_ < cnt_ and prev_ <= L: return prev
            elif prev_ == cnt_: return None
            elif cnt_ < prev_ and cnt_ <= L: return cnt
            else: return -1

        elif not idx and abs(k-keys[cnt]) <= L: return cnt
        elif idx == len(keys) and abs(k-keys[prev]) <= L: return prev

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
    keys = deque(sorted(list(db.keys())))

    # answering the question
    for _ in range(M):
        command_type, *cnt = map(int, input().split())
        if command_type == 1:
            curr = create(*cnt)
            if curr is not None:
                keys = curr

        elif command_type == 2:
            update(*cnt)

        else:
            result = search(*cnt)
            if result == -1: print(result)
            elif result is not None: print(db[keys[result]])
            else: print("?")


if __name__ == "__main__":
    solution()
