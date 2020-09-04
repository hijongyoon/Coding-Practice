import sys

countList = []


def main():
    n, m = map(int, sys.stdin.readline().split())
    chess = []
    inputChess(chess, n, m)


def inputChess(chess, n, m):
    for i in range(n):
        chessRow = list(map(str, sys.stdin.readline().split()))
        chess.append(chessRow)


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
            if pivot != chess[n1][n2]: count += 1
            n2 += 2
        n2 = num2
        while n1 < limit1:
            if pivot != chess[n1][n2]: count += 1
            n1 += 2
        n1 = num1
        n2 = num2 + 1
        while n2 < limit2:
            if pivot == chess[n1][n2]: count += 1
            n2 += 2
        n2 = num2
        n1 = num1 + 1
        while n1 < limit1:
            if pivot == chess[n1][n2]: count += 1
            n1 += 2
        if pivot != chess[num1+1][num2+1]:
            chess[num1+1][num2+1] = pivot
            count += 1
            num1 += 1
            num2 += 1

main()
