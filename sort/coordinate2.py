import sys


def main():
    n = int(sys.stdin.readline())
    numbers = []
    for i in range(n):
        x, y = map(int,sys.stdin.readline().split())
        num=(y,x)
        numbers.append(num)
    numbers.sort()
    for i in range(n):
        print(numbers[i][1], numbers[i][0])


main()