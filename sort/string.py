import sys


def main():
    n = int(sys.stdin.readline())
    s = set()
    for i in range(n):
        s.add(sys.stdin.readline().rstrip())
    l = sorted(s)
    l.sort(key=len)
    for i in range(len(l)): print(l[i])


main()
