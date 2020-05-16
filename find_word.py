import sys


def make_dict(st1):
    di = {}
    for i in st1:
        di[i] = di.setdefault(i, 0) + 1  # 코드의 간결을 위해 setdefault 메소드 사용.
    return di


def main():
    st1 = sys.stdin.readline().rstrip().upper()
    di = make_dict(st1)  # 단어(키) 단어의 나온 횟수(값)으로 하는 딕셔너리 생성.
    l1 = list(di.keys())  # 키만 가지고 있는 리스트.
    l2 = list(di.values())  # 값만 가지고 있는 리스트.
    num = l2.count(max(l2))  # max(l2)를 통해 가장 큰 값을 찾고 그것이 몇번 나오는지를 num 에 저장.
    if num == 1:  # 한 번이라면 가장 많은 것이 여러개가 아니다는 것을 의미.
        print(l1[l2.index(max(l2))])  # l2에서 가장 큰 값을 가지는 것의 인덱스를 찾아 l1의 인덱스로 전달.
    else:
        print("?")


main()
