import sys


def main():
    a, b, v = map(int, sys.stdin.readline().split())
    print((v - a) // (a - b) + 1 if (v-a)%(a-b)==0 else (v-a)//(a-b)+2)
    # 3항 연산자의 경우 먼저 if 앞에 결과가 있고 그 다음 if 조건문이 있음. 하지만 else 는 else 다음 바로 결과가 있음.

main()


