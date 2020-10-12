import sys


def main():
    n = int(sys.stdin.readline())
    li = []
    for i in range(n):
        m = sys.stdin.readline().rstrip().split(" ")
        li.append([int(m[0]),m[1]])
    li.sort(key=lambda x:x[0])
    for i in range(n):
        print(li[i][0], li[i][1])


main()
