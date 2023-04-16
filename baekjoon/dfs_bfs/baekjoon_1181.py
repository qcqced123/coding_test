import sys

input_length = int(input())
input_list = [input() for num in range(input_length)]
input_list = [(len(value), value) for value in input_list]
result_list = sorted(list(set(input_list)))


for value in result_list:
    print(value[1])
