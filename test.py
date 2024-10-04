from collections import deque

i = "R"
dummy = 1000000
vx = 1234

tmp = deque(list(str(dummy + vx))[-4:])
rv = -1 if i == "L" else 1
tmp.rotate(rv)
print(int("".join(tmp)))