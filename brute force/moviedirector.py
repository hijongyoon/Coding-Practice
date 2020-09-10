import sys


def main():
    n = int(sys.stdin.readline()) - 1
    pivot = 666
    i = 0
    while i < n:
        pivot += 1
        if str(pivot).count('666') != 0:
            i += 1
    print(pivot)


main()
# N = int(input())
# if N == 1:
#     print(666)
# else:
#     count = 1
#     for i in range(2, N + 1):
#         base_title = "{0}666".format(i - 1)
#         num_of_extra_six_in_row = 0
#         for k in range(len(base_title) - 3):
#             if base_title[-4 - k] == '6':
#                 num_of_extra_six_in_row += 1
#             else:
#                 break
#         count += int(10 ** num_of_extra_six_in_row)
#         print(10 ** num_of_extra_six_in_row, count,base_title)
#
#         if count >= N:
#             break
#
#     if num_of_extra_six_in_row > 0:
#         print("-------------")
#         base = int(10 ** num_of_extra_six_in_row)
#         count -= base
#         print(base_title, int(base_title)%base , end =' ')
#         base_title = int(base_title) - int(base_title) % base + (N - count - 1)
#         print(base, count, N-count-1)
#
#     print(base_title)
