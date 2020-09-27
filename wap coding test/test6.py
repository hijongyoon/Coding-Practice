import sys

n = int(sys.stdin.readline())
if n // 10 == 0 or n // 100 == 0:
    print(n)
else:
    m = 0
    for i in range(100, n + 1):
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            m += 1
    print(m + 99)
