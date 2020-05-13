def fibonacci(n):
    if n==0:
        return [1,0]
    elif n==1:
        return [0,1]
    elif n==2:
        return [1,1]
    num1=1
    num2=1
    result=0
    for i in range(3,n+1):
       result=num1+num2
       num1=num2
       num2=result
    return [num1,result]

def main():
    n=int(input())
    for i in range(n):
        num=int(input())
        zero,one=fibonacci(num)
        print('{} {}'.format(zero,one))

main()