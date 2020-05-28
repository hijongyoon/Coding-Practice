import sys


def main():
    li=list(range(1,10000))
    num=int(sys.stdin.readline())
    start=0
    end=len(li)-1
    while start<=end:
        mid=(start+end)//2
        if li[mid]==num:
            print("Find")
            break
        elif li[mid]<num: start=mid+1
        else: end=mid-1

main()