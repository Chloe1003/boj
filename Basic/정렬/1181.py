import sys
word = []
for _ in range(int(input())):
    word.append(sys.stdin.readline().strip())
print(*sorted(list(set(word)), key=lambda x: (len(x), x)), sep='\n')
