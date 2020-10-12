import sys


def input_score(li, n):
    for i in range(n):
        li[i] = list(map(int, sys.stdin.readline().split()))
    return li


def compare_average(average, li):
    result = []
    n = 0
    for i in li:
        l = []
        for j in range(1, len(i)):
            if i[j] > average[n]:
                l.append(i[j])
        result.append(l)
        n += 1
    return result


def check_sum(result, li):
    check = []
    n = 0
    for i in li:
        check.append((len(result[n]) / i[0]) * 100)
        n += 1
    return check


def print_check(result):
    for i in result:
        print('{0:.3f}{1}'.format(round(i,3),"%"))

def main():
    n = int(sys.stdin.readline())
    make_list = lambda num: [[] for i in range(num)]#점수를 넣을 리스트를 만듦.
    li = make_list(n)
    li = input_score(li, n)#점수를 리스트에다 삽입.
    calculate_average = lambda l: [(sum(i) - i[0]) / i[0] for i in l]#평균 리스트을 만듦.
    average = calculate_average(li)
    result = compare_average(average, li)#평균보다 큰 점수를 가진 것들의 리스트를 생성.
    result = check_sum(result, li)#최종적으로 확률에대한 리스트를 생성.
    print_check(result)


main()
