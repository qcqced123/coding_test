from collections import defaultdict


def solution(skill, skill_trees):
    """ 뒤쪽 스킬이 나오려면, 앞쪽꺼도 나와 있어야 함
    idea: hash
        - key: 현재 스킬
        - value: 키의 선행 스킬

    feedback:
        - 특정 순서를 지켜야 하는 조건이 있기 때문에, 주어진 배열에서 특정한 시점을 찾는 것과 동일해짐
        - 그래서 스택이나 큐를 사용하면 훨씬 쉽게 풀 수 있음
        - 그렇네 이렇게 뻘짓 할 필요가 없었음
    """
    # make the hash
    answer = 0
    size = len(skill)

    cache = defaultdict(list)
    idx_cache = defaultdict(int)
    idx_cache[skill[0]] = 0
    for i in range(1, size):
        cnt = skill[i]
        cache[cnt].extend(list(skill[:i]))
        idx_cache[cnt] = i

    # searching for each element
    for skill_tree in skill_trees:
        flag = 0
        visited = [0] * size

        # searching for each char
        for s in skill_tree:
            if cache[s]:
                for c in cache[s]:
                    if not visited[idx_cache[c]]:
                        flag += 1
                        break
                else:
                    visited[idx_cache[s]] = 1

            elif s == skill[0]:
                visited[idx_cache[s]] = 1

            if flag:
                break
        else:
            answer += 1

    return answer


def solution2(skill, skill_trees):
    from collections import deque

    answer = 0
    for skills in skill_trees:
        q = deque(skill[:])
        for s in skills:
            if s in skill and q.popleft() != s:
                break
        else:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution2("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))