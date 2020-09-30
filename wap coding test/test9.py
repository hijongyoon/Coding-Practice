import sys

cro = ["c=", "c-", "dz=", "d-", "d-", "lj", "nj", "s=", "z="]
s = sys.stdin.readline().rstrip()
for i in cro:
    s = s.replace(i, ".")
print(len(s))
