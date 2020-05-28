import sys


def check(num1, num2, num3):
    li = list(range(num2, num3 + 1))
    if li.count(num1) == 0:
        return False
    else:
        return True


def main():
    num = int(sys.stdin.readline())
    i = 2
    num1 = 0
    num2 = 1
    while True:
        if check(num, num1, num2):
            print(i)
            break
        elif num1 == 0:
            num1 = num2
            num2 += 6
        else:
            num1 = num2
            num2 += (6 * i)
            i += 1


main()
