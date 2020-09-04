import sys

countList = []


def main():
    n, m = map(int, sys.stdin.readline().split())
    chess = [list(sys.stdin.readline().split()[0]) for _ in range(n)]
    checkChess(chess, n, m)
    print(min(countList))


def checkChess(chess, n, m):
    for i in range(n - 7):
        for j in range(m - 7):
            pivot = chess[i][j]
            checkArray(chess, pivot, i, j)


def checkArray(chess, pivot, num1, num2):  # num1,num2는 pivot 의 좌표
    global countList
    count = 0
    limit1 = num1 + 8
    limit2 = num2 + 8
    for i in range(8):
        n1 = num1
        n2 = num2
        while n2 < limit2:
            #n2 += 2
            if n2 < limit2 and pivot != chess[n1][n2]:
                count += 1
            n2 += 2
        n2 = num2
        n1 = num1+2
        while n1 < limit1:
            #n1 += 2
            if n1 < limit1 and pivot != chess[n1][n2]:
                count += 1
            n1 += 2
        n1 = num1
        n2 = num2 + 1
        while n2 < limit2:
            #n2 += 2
            if n2 < limit2 and pivot == chess[n1][n2]:
                count += 1
            n2 += 2
        n2 = num2
        n1 = num1 + 1
        while n1 < limit1:
            #n1 += 2
            if n1 < limit1 and pivot == chess[n1][n2]:
                count += 1
            n1 += 2
        # if (num1 + 1 < limit1 and num2 + 1 < limit2) and pivot != chess[num1 + 1][num2 + 1]:
        #     count += 1
        num1 += 1
        num2 += 1
    countList.append(count)

main()
