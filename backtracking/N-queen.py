import sys

count = 0


def promising(level, cols): # 같은 열이거나 같은 대각선인지 검사하는 것.
    for i in range(level):
        if cols[i] == cols[level]: # 같은 열인가?
            return False
        elif level - i == abs(cols[level] - cols[i]): # 같은 대각선 인가?
            return False
    return True


def queen(level, n, cols):
    global count
    if not promising(level, cols):
        return False
    elif level == n - 1:
        count += 1
        return True
    for i in range(n):
        cols[level + 1] = i
        queen(level + 1, n, cols)
    return False


def main():
    global count
    n = int(sys.stdin.readline())
    cols = [-1] * n
    queen(-1,n,cols)
    print(count)


main()