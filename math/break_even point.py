import sys

# 이 문제는 손익 분기점을 구하는 문제인데 단순하게 반복문으로 접근하면 시간 초과가 된다. 최악의 경우 반복의 횟수가 21억번 까지 늘어나기 때문이다.
# 하지만 원가와 판매가 사이의 규칙을 파악한다면 O(1) 시간 복잡도로 이 문제를 해결할 수 있다.


def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if b >= c:
        print("-1")
    else:
        result = int((a / (c - b)) + 1)
        print(result)


main()
