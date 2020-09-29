import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = 0
for i in nums:
    flag = True
    if i == 1:
        continue
    n = int(i ** 0.5)
    for j in range(1, n+1):
        if i % j == 0 and j != 1:
            flag = False
            break
    if flag:
        m += 1
print(m)
