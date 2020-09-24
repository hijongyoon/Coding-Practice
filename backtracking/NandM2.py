import sys
import itertools


def main():
    n, m = map(int, sys.stdin.readline().split())
    per = list(itertools.permutations([x + 1 for x in range(n)], m))
    per = [tuple(sorted(per[i])) for i in range(len(per))]
    per = list(set(per)) # list 는 hash 를 지원하지 않아서 set 이 안되지만 tuple 은 hash 지원.
    per.sort()
    for i in range(len(per)):
        for j in range(m):
            print(per[i][j],end=' ')
        print()


main()
