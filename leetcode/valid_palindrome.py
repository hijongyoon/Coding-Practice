import sys


def main():
    s = sys.stdin.readline().lower().rstrip()
    s = [st for st in s if st.isalnum()]
    if s == s[::-1]:
        print("true")
    else:
        print("false")


main()