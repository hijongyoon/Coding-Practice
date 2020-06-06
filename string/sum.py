import sys


def main():
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().rstrip()))  # 여기서 split()을 사용하면 오류 발생->empty separate.
    print(sum(l))


main()
