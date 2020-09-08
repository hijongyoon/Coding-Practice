import sys


def main():
    pivot = 666
    i = 0
    n = int(sys.stdin.readline()) - 1
    flag = True
    while i < n:
        pivot += 1000
        if str(pivot).count('6') > 3 and str(pivot).count('6666') >= 1:
            pre_pivot = pivot
            i -= 1
            pivot -= 7
            if str(pivot+1).count('666') == 0 : break
            for j in range(11):
                i += 1
                if i >= n:
                    flag = False
                    break
                pivot += 1
            if flag: pivot = pre_pivot+1000
        i += 1
    print(pivot)

# def main():
#     n=int(sys.stdin.readline())-1
#     pivot=666
#     i= 0
#     while i < n:
#         pivot += 1
#         if str(pivot).count('666') != 0:
#             i+=1
#     print(pivot)
#
#
# main()
