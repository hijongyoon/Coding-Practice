import sys


def divide(n):
    return n + sum(list(map(int, str(n))))


def main():
    num = int(sys.stdin.readline())
    n = num - 9 * len(str(num)) if num>=18 else 0 # 여기서 9를 길이에 곱한 이유는 무조건 적으로 생성자의 합은 생성자의 길이*9를 뺀 것에서
                                                  # 클수 밖에 없음. 왜냐하면 예를 들어 생성자가 198 이라 하자. 그러면 1+9+8 이
                                                  # 나옴. 그러므로 최소한의 범위로 9+9+9를 빼는 것.
    while True:
        result = divide(n)
        if result == num: break
        if n > num:
            print("0")
            return
        n = n + 1
    print(n)


main()
