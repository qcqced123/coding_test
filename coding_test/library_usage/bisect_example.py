from bisect import bisect_left, bisect_right

"""

1) 정렬된 리스트 내부 원소 중, 지정 범위에 해당 되는 값의 개수 반환

"""

def count_by_range(list_a, left_value, right_value):
    right_value = bisect_right(list_a, right_value)
    left_value = bisect_left(list_a, left_value)
    print(right_value, left_value)

    return right_value - left_value

list_a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(list_a, 0, 3))