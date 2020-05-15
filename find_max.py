import sys


def main():
    n = int(sys.stdin.readline())
    li =list(map(int,sys.stdin.readline().split()))
    print(min(li),max(li))


main()
