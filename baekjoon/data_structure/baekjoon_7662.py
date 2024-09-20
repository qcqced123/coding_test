import sys
import heapq


def solution():
    """
    idea:
        1) double priority queue (max, min)
        2) shared memory for sync of two different queue (dictionary)
    """
    def add_vocab(v):
        try: vocab[v] += 1
        except: vocab[v] = 1

    def delete_func(h, state):
        while h:
            pv = state*heapq.heappop(h)
            if vocab[pv]:
                vocab[pv] -= 1
                break

    T = int(sys.stdin.readline())
    for t in range(T):
        vocab = {}
        max_h, min_h = [], []
        elements = int(sys.stdin.readline())

        for element in range(elements):
            ops, number = sys.stdin.readline().rstrip().split(' ')  # convert number's dtype
            number = int(number)

            if ops == "I":
                add_vocab(number)
                heapq.heappush(min_h, number)
                heapq.heappush(max_h, -number)

            elif number == 1 and max_h:
                delete_func(max_h, -1)

            elif number == -1 and min_h:
                delete_func(min_h, 1)

        result = sorted([k for k, v in vocab.items() if v])
        print("EMPTY") if not result else print(f"{result[-1]} {result[0]}")


if __name__ == "__main__":
    solution()
