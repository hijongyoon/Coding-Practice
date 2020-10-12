import sys
#보류. 문제자체를 잘못이해하고 있고, 이해 하지 못함.


def check(num):
    i = 0
    n = 1
    if num==1: return 1
    elif num==2: return 2
    while True:
        if i + n >= num: return i+2
        i += 1
        n = i + n
        if i + n + 1 == num: return i + 2


def main():
    for i in range(int(sys.stdin.readline())):
        x, y = map(int, sys.stdin.readline().split())
        print(check(y-x))


main()