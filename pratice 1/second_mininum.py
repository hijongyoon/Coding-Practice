import sys


def main():
    l = []
    l += map(int, sys.stdin.readline().split())
    l.sort()
    print(l[1])


main()
