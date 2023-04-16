import sys

X, Y, W, H = map(int, sys.stdin.readline().split())

# Step 1. 가로 축 길이 비교
x_length = W - X
if x_length > X:
    x_length = X

# Step 2. 세로 축 길이 비교
y_length = H - Y
if y_length > Y:
    y_length = Y

# Step 3. 최종 길이 비교
result = x_length
if x_length > y_length:
    result = y_length

# Step 4. 결과 반환
print(f'{result}')

sorted()