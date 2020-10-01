import sys

num = int(sys.stdin.readline())
if num % 5 == 0:
    print(num // 5)
elif (num % 5) == 3:
    print((num // 5) + 1)
else:
    num5 = num // 5
    rest = num % 5
    while rest % 3 != 0 and num5 >= 0:
        rest += 5
        num5 -= 1
    if rest % 3 != 0 or rest > num:
        print("-1")
    else:
        print(num5 + rest // 3)
