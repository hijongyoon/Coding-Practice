import sys


def main():
    n = int(sys.stdin.readline())
    numbers = []
    for i in range(n):
        num = tuple(map(int, sys.stdin.readline().split()))
        numbers.append(num)
    numbers.sort()
    for i in range(n):
        print(numbers[i][0], numbers[i][1])


main()
