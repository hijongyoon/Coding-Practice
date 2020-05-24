import sys
# 코드를 아무래도 새로 짜야함. 17이 반례임.


def main():
    num = int(sys.stdin.readline())
    if num % 5 == 0:
        print(num // 5)
    elif (num % 5) == 3:
        print((num // 5) + 1)
    elif (num % 5) != 3 and (num // 5) != 0:
        x = (num // 5) - 1
        y = (num % 5) + 5
        if y % 3 == 0:
            print(x + (y // 3))
        else:
            if num % 3 == 0:
                print(num // 3)
            else:
                print("-1")
    elif (num % 5) != 3 and (num // 5) == 0:
        print("-1")


main()
