import sys
n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(sys.stdin.readline())
num = 0
for _ in range(m):
    num += 1 if sys.stdin.readline() in s else 0
print(num)