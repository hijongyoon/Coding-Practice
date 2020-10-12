import sys

countList = []


def main():
    n, m = map(int, sys.stdin.readline().split())
    chess = [list(sys.stdin.readline().split()[0]) for _ in range(n)]
    checkChess(chess, n, m)
    print(min(countList))


def checkChess(chess, n, m):
    global countList
    for i in range(n - 7):
        for j in range(m - 7):
            pivot = chess[i][j]
            result1 = checkArray1(chess, pivot, i, j)
            result2 = checkArray2(chess, pivot, i, j)
            countList.append(result1 if result1 < result2 else result2)


def checkArray1(chess, pivot, num1, num2):  # num1,num2는 pivot 의 좌표
    count = 0
    limit1 = num1 + 8
    limit2 = num2 + 8
    for i in range(8):
        n1 = num1
        n2 = num2
        while n2 < limit2:
            if n2 < limit2 and pivot != chess[n1][n2]:
                count += 1
            n2 += 2
        n2 = num2
        n1 = num1 + 2
        while n1 < limit1:
            if n1 < limit1 and pivot != chess[n1][n2]:
                count += 1
            n1 += 2
        n1 = num1
        n2 = num2 + 1
        while n2 < limit2:
            if n2 < limit2 and pivot == chess[n1][n2]:
                count += 1
            n2 += 2
        n2 = num2
        n1 = num1 + 1
        while n1 < limit1:
            if n1 < limit1 and pivot == chess[n1][n2]:
                count += 1
            n1 += 2
        num1 += 1
        num2 += 1
    return count


def checkArray2(chess, pivot, num1, num2):
    count = 0
    limit1 = num1 + 8
    limit2 = num2 + 8
    for i in range(8):
        n1 = num1
        n2 = num2
        while n2 < limit2:
            if n2 < limit2 and pivot == chess[n1][n2]:
                count += 1
            n2 += 2
        n2 = num2
        n1 = num1 + 2
        while n1 < limit1:
            if n1 < limit1 and pivot == chess[n1][n2]:
                count += 1
            n1 += 2
        n1 = num1
        n2 = num2 + 1
        while n2 < limit2:
            if n2 < limit2 and pivot != chess[n1][n2]:
                count += 1
            n2 += 2
        n2 = num2
        n1 = num1 + 1
        while n1 < limit1:
            if n1 < limit1 and pivot != chess[n1][n2]:
                count += 1
            n1 += 2
        num1 += 1
        num2 += 1
    return count


main()
