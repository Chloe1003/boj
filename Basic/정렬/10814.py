import sys
member = []
for _ in range(int(input())):
    member.append(sys.stdin.readline().rstrip())
print(*sorted(member, key=lambda x: (x[:2], member.index(x))), sep='\n')