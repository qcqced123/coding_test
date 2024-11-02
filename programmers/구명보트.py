def solution(people, limit):
    """ trade-off, 최대 2명, 무게제한, 최소 보트, NlogN
    idea: greedy with two-pointer
    """
    answer = 0
    people.sort()
    visited = [0] * len(people)

    l, r = 0, len(people) - 1
    while l < r:
        lp, rp = people[l], people[r]
        if lp + rp > limit:
            r -= 1

        else:
            answer += 1
            visited[l], visited[r] = 1, 1
            l += 1
            r -= 1
    answer += visited.count(0)

    return answer


if __name__ == '__main__':
    solution([60, 70, 60, 50, 40, 100, 70], 100)
