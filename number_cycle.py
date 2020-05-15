import sys


def number_input():
    num = sys.stdin.readline().rstrip()
    if int(num) < 10:
        num = '0' + num
    return num


def cycle(str1):
    num = str(int(str1[0]) + int(str1[1]))
    return str1[1] + num[len(num) - 1]


def main():
    i = 0
    str1 = number_input()
    str2 = str1
    while True:
        str2 = cycle(str2)
        i += 1
        if str2 == str1:
            break
    print(i)


main()
