import sys

many = 0


def check_word(word):
    global many
    fake = sorted(word) # 단어를 정렬.
    for i in range(len(word)):
        num = fake.count(word[i]) # 한 문자가 총 몇개있는지 헤아림.
        if num == 1: continue # 하나라면 한번 나온 것이므로 그냥 무시.
        st = word[i] * num # 중복이라면 연속적으로 있어야 하므로 나온 갯수만큼 늘림.
        if word.find(st) == -1: # 늘린 문자를 찾아서 -1이 나오면 없는 것.
            many -= 1
            break


def main():
    global many
    many = num = int(sys.stdin.readline())
    for i in range(num):
        words = sys.stdin.readline().strip()
        check_word(words)
    print(many)


main()
