import sys

# Step 1. Input Range Numbers
M, N = map(int, sys.stdin.readline().split())

# Step 2. Root Square Method
num_list = [num for num in range(M, N+1, 1)]
for value in num_list:
    # i = 2 # 여기를 리스트로 바꾸자
    divisor_list = [num for num in range(2, int(value**(1/2)), 1)]
    classifier = True
    while i * i <= value:

        # Case 1) 합성수
        if value % i == 0:
            classifier = False
            break

        # Case 2) 나눗셈 안되는 경우
        else:
            classifier = True
            i += 1 # 여기를 1씩 다 늘려서 문제가 되는구나 그래서 느리네 여기를

    if classifier:
        print(value)


