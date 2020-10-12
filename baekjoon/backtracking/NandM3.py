import sys
import itertools


def main():
    n, m = map(int, sys.stdin.readline().split())
    print("\n".join(list(map(' '.join, itertools.product([str(x + 1) for x in range(n)], repeat=m)))))
    # product 는 중복 순열을 의미. 뒤에 repeat 는 몇개로 구성할지를 정할 때 사용하는데 반드시 repeat 를 써야함.


main()

# li = []
#
#
# def main():
#     n, m = map(int, sys.stdin.readline().split())
#     product(1, n, m)
#
#
# def product(start, n, m):
#     global li
#     if start > m:
#         for i in range(m):
#             print(li[i], end=' ')
#         print()
#         return
#     for i in range(1, n + 1):
#         li.append(i)
#         product(start + 1, n, m)
#         li.reverse() # 뒤에서 부터 삭제 해야하므로 reverse 함.
#         li.remove(i)
#         li.reverse()
#
#
# main()
