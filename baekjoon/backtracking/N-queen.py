import sys

count = 0
low_li = []


def promising(level, cols):  # 같은 열이거나 같은 대각선인지 검사하는 것.
    for i in range(level):
        # if cols[i] == cols[level]:  # 같은 열인가?
        #     return False
        if level - i == abs(cols[level] - cols[i]):  # 같은 대각선 인가?
            return False
    return True


def queen(level, n, cols, num):
    global count, low_li
    if not promising(level, cols):
        return False
    elif level == n - 1:
        count += 1
        return True
    for i in range(n):
        if level >= 0 and (cols[level] == i or i + 1 == cols[level] or i - 1 == cols[level] or i in low_li):
            continue
        if num != -1:
            low_li.append(num)
        cols[level + 1] = i
        queen(level + 1, n, cols, i)
        if num != -1:
            low_li.remove(num)
    return False


def main():
    global count
    n = int(sys.stdin.readline())
    cols = [-1] * n
    queen(-1, n, cols, -1)
    print(count)


main()
