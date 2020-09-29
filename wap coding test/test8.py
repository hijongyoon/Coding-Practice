import sys

sys.setrecursionlimit(10 ** 6 + 1)


def main():
    n = int(sys.stdin.readline())
    if n == 1:
        print(0)
        return
    li = [-1] * (n + 1)
    print(mem(n, li))


def mem(n, li):
    if n == 1:
        return 0
    elif li[n] != -1:
        return li[n]
    else:
        if n % 3 == 0 and n % 2 == 0:
            li[n] = min(mem(n // 3, li) + 1, mem(n // 2, li) + 1)
        elif n % 3 == 0:
            li[n] = min(mem(n // 3, li) + 1, mem(n - 1, li) + 1)
        elif n % 2 == 0:
            li[n] = min(mem(n // 2, li) + 1, mem(n - 1, li) + 1)
        elif n % 2 != 0 and n % 3 != 0:
            li[n] = mem(n - 1, li) + 1
        return li[n]


main()