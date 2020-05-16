import sys

def main():
    st1=sys.stdin.readline().strip() # 만약 여기서 엔터키만 입력한다면.
    li=st1.split(" ") # 공백을 기준으로 자르면 리스트에는 "" 하나만 가진 길이가 1인 리스트가 생성.
    if li[0] != "":
        print(len(li))
    else: # 그럴 경우는 단어가 없기에 0이 출력되어야함.
        print("0")


main()