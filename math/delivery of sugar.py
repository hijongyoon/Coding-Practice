import sys
# 코드를 아무래도 새로 짜야함. 17이 반례임.


def main():
    num = int(sys.stdin.readline())
    if num%5==0: print(num//5) # 5로 완전히 나눠지는 것이 가장 좋으므로 바로 출력.
    elif (num%5)==3: print((num//5)+1) # 5로 나누고 나머지가 3이라면 몫에서 1을 더함.
    else:
        num5=num//5
        rest=num%5
        while rest%3!=0 and num5>=0: # 나머지에 5를 더하면서 몫은 1씩 뺌. 동시에 나머지가 3에 나눠지거나 몫이 0보다 작아지면 탈출.
            rest+=5
            num5-=1
        if rest%3!=0 or rest>num: print("-1") # 3과 5로 절대 표현할수 없는 수는 위의 반복문을 거치면 나머지가 원래 수 보다 커짐.
        else: print(num5+rest//3)


main()
