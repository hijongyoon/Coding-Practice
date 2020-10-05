import sys
import itertools


def to_generate(per):
    for i in per:
        yield i


def main():
    n, m = map(int, sys.stdin.readline().split())
    per = list(itertools.product([x + 1 for x in range(n)], repeat=m))
    per = list(set([tuple(sorted(x)) for x in per]))
    per.sort()
    per = to_generate(per)
    for i in per:
        for j in range(m):
            print(i[j], end=' ')
        print()


main()

