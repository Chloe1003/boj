import sys
input = sys.stdin.readline
n, m = map(int, input().split())
p_dict = {}
for i in range(1, n+1):
    p = input().rstrip()
    p_dict[p] = i
    p_dict[i] = p
for _ in range(m):
    name = input().rstrip()
    if name.isdigit():
        print(p_dict[int(name)])
    else:
        print(p_dict[name])