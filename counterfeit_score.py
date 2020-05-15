import sys


def input_score():
    return list(map(int, sys.stdin.readline().split()))


def main():
    int(sys.stdin.readline())
    l = input_score()
    m=max(l)
    l=[(x/m)*100for x in l]
    print(sum(l)/len(l))

main()