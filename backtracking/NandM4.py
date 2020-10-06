import sys


def per(start, m, s, li):
    if start >= m:
        print(" ".join(list(s)))
        return
    for i in range(len(li)):
        if int(s[start-1]) <= li[i]:
            per(start + 1, m, s + str(li[i]), li)


def main():
    n, m = map(int, sys.stdin.readline().split())
    li = list(range(1, n + 1))
    for i in range(len(li)):
        per(1, m, str(li[i]), li)


main()