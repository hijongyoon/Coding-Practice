import sys
from collections import Counter # 최빈값을 구할 때 사용하는 모듈.


def main():
    numbers = []
    many=int(sys.stdin.readline())
    for i in range(many):
        numbers.append(int(sys.stdin.readline()))
    numbers.sort()
    print(int(round(sum(numbers)/many,0)))
    print(numbers[many//2])
    if many != 1:
        cnt=Counter(numbers).most_common(2)
        if cnt[0][1] != cnt[1][1]: print(cnt[0][0])
        else: print(cnt[1][0])
    else: print(numbers[0])
    print(numbers[-1]-numbers[0])





main()