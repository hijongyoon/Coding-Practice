import sys


def main():
    while True:
        try:
            n1, n2 = map(int, sys.stdin.readline().split())
        except ValueError:
            break
        print(n1 + n2)


main()
