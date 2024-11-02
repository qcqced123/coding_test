from bisect import bisect_left
from collections import defaultdict


def solution(info, query):
    """
    idea: hash + binary search
        - hash:
            - 쿼리에서 던지는 지원자 조건에 부합하는 지원자를 찾으려면, N*K가 되고, 5만*10만이 되어 터진다
            - 그래서 쿼리에 대응하기 위해, 지원자 데이터를 가지고 미리, 가능한 경우의 수를 해시 자료로 만들자
            - 데이터 하나당 16개의 파생 데이터를 미리 만들 수 있음
            - 데이터를 키 값으로 세팅, 해당 키에 대한 벨류는 리스트, 리스트에는 지원자의 점수를 넣음
            - 그럼 쿼리를 키로 사용해 해시에서, 쿼리의 조건에 맞는 지원자들의 점수 배열을 상수 시간만에 얻을 수 있음

        - binary search:
            - 해시를 통해 얻은, 지원자들의 점수 배열과 컷오프 점수를 이용해 bisect
            - bisect 결과를 이용해, 쿼리에 맞는 지원자 숫자를 도출
    """
    def make_candidate(a, b, c, d):
        """ no mutable for dictionary key, must be immutable """
        return [
            [a, b, c, d],
            ["-", b, c, d],
            [a, "-", c, d],
            [a, b, "-", d],
            [a, b, c, "-"],
            ["-", "-", c, d],
            ["-", b, "-", d],
            ["-", b, c, "-"],
            [a, "-", "-", d],
            [a, "-", c, "-"],
            [a, b, "-", "-"],
            ["-", "-", "-", d],
            ["-", "-", c, "-"],
            ["-", b, "-",  "-"],
            [a, "-", "-", "-"],
            ["-", "-", "-", "-"],
        ]

    # make the candidate hash
    answer = []
    candidate = defaultdict(list)
    for data in info:
        l, p, e, f, s = data.split(" ")
        for extra in make_candidate(l, p, e, f):
            candidate[tuple(extra)].append(int(s))

    # sorted by score
    for k in candidate:
        candidate[k].sort()

    # get score array from each candidate, hashed from each input query
    for q in query:
        ql, qp, qe, temp = q.split(" and ")
        qf, qs = temp.split(" ")

        arr = candidate[(ql, qp, qe, qf)]  # hashed by query
        answer.append(len(arr) - bisect_left(arr, int(qs)))

    return answer


if __name__ == '__main__':
    print(
        solution(
            ["java backend junior pizza 150", "python frontend senior chicken 210",
             "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80",
             "python backend senior chicken 50"],
            ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
             "- and - and - and chicken 100", "- and - and - and - 150"]
        )
    )
