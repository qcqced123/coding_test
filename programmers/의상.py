from collections import defaultdict


def solution(clothes):
    """ 어제 코디 캐싱 필요, 종류별 최대 1개씩, 최소 1개 옷 입어야, 조합이 중요
    일단 종류별로 모아야 되니까, 해시 사용, 시간 복잡도는 상관 없는듯

    idea: hash
        - 경우의 수 계산:
    """
    # make the hash
    cache = defaultdict(list)
    for cloth in clothes:
        name, types = cloth
        cache[types].append(name)

    answer = 1
    for k in cache.keys():
        answer *= len(cache[k]) + 1
    return answer - 1


if __name__ == '__main__':
    solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
