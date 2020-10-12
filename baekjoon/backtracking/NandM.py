import sys

per_li = []


def main():
    n, m = map(int, sys.stdin.readline().split())
    check = []
    for i in range(n + 1): check.append(False)
    permutation(1, n, m, check)


def permutation(start, n, m, check):
    global per_li
    if start > m:
        for i in range(m):
            print(per_li[i], end=' ')
        print()
        return
    for i in range(1, n + 1):
        if not check[i]:
            check[i] = True
            per_li.append(i)
            permutation(start + 1, n, m, check)
            check[i] = False
            per_li.remove(i)


main()

# import sys
# import itertools
# n, m = map(int, sys.stdin.readline().split())
# li = [str(x+1) for x in range(n)]
# print("\n".join(list(map(' '.join,itertools.permutations(li,m)))))


# join 은 리스트에서 문자열로 바꿔주는 함수.
# "\n".join 의 경우는 리스트의 요소를 "\n"을 기준으로 문자열화 한다는 의미. permutations 를 사용하면 순열을 쉽게 구할 수 있음. 두번째 인자로 전달하는 것은
# 순열을 몇개의 구성으로 이룰지 정하는 인자.

