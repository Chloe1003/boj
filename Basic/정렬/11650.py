import sys
num = []
for _ in range(int(input())):
    num.append(list(map(int, input().split())))
num.sort()
for i in num:
    print(*i)