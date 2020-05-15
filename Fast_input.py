import sys

def sum():
    n1,n2=map(int,sys.stdin.readline().split())
    return n1+n2

def main():
    num=int(sys.stdin.readline()) # input 이 아니라 sys.stdin.readline() 으로 입력을 받으면 속도적 측면에서 더 나은 성능을 보임.
    for i in range(num):          # input 처럼 문자열로 인식을 하는 동시에 readline() 으로 마무리하면 개행이 붙는다. 개행을 없애려면 .rstrip() 추가.
        print(sum())

main()