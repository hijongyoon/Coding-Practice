import sys

def check(li,num):
    max=0
    for i in range(len(li)-2):
        for j in range(i+1,len(li)-1):
            for k in range(j+1,len(li)):
                if li[i]+li[j]+li[k]==num: return num
                elif max<li[i]+li[j]+li[k] <num: max=li[i]+li[j]+li[k]
    return max

def main():
    li=[]
    n,m=map(int,sys.stdin.readline().split())
    li.extend(list(map(int,sys.stdin.readline().split())))
    print(check(li,m))

main()