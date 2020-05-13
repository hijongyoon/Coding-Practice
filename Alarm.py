def main():
    h, m = map(int, input().split())
    h,m=change_time(h, m)
    print(h,m)


def change_time(h, m):
    if h==0:
        if m<45:
            h=23
            m=60+m-45
        else: m-=45
    else:
        if m<45:
            h-=1
            m=60+m-45
        else: m-=45
    return [h,m]

main()