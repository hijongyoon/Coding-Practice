import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    chess = []
    inputChess(chess, n, m)



def inputChess(chess, n, m):
    for i in range(n):
        chessRow = list(map(str, sys.stdin.readline().split()))
        chess.append(chessRow)


def checkChess(chess,n,m):
    for i in range(n):
        for j in range(m):



def checkNum(i,j,n,m):
    if i < 0 or i > n: return False
    elif j < 0 or j > m: return False
    else : return True


main()
