import sys


def check(num1, num2, num3):
    if num2<=num1<=num3:
        return True
    else: return False


def main():
    num = int(sys.stdin.readline())
    i = 2
    num1 = 0
    num2 = 1
    if num==1:
        print(num)
        return
    while True:
        if check(num, num1, num2):
            print(i)
            break
        elif num1 == 0:#처음의 경우 1개에서 5개만 증가하므로 다른 case 로 분류.
            num1 = num2
            num2 += 6#최대의 범위.
        else:
            num1 = num2#num1은 최소의 범위를 의미.
            num2 += (6 * i)#갯수가 6개,12개,18개 즉 6의 배수로 늘어남.
            i += 1


main()
