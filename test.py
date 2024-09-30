import time

arr = [i for i in range(1000000)]

src = time.time()
print(1 if 1000000 in arr else 0)
end = time.time()

print(f"Python pure List in ops linear searching time is: {end-src}")

vocab = set(i for i in range(1000000))

src1 = time.time()
print(1 if 1000000 in vocab else 0)
end1 = time.time()

print(f"Python pure set in ops linear searching time is: {end1-src1}")

