import sys


def main():
    pivot = 666
    i = 0
    n = int(sys.stdin.readline())-1
    while i < n:
        pivot += 1000
        if str(pivot).count('6') > 3 and str(pivot).count('666') >= 1:
            i -= 1
            pivot -= 7
            for j in range(9):
                i += 1
                if i >= n: break
                pivot += 1
        i += 1
    print(pivot)

main()