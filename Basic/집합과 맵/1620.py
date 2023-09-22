n, m = map(int, input().split())
p_dict = {}
for i in range(1, n+1):
    p_dict[input()] = i
p_dict_reverse = {val:key for key, val in p_dict.items()}
for _ in range(m):
    name = input()
    print(p_dict.get(name) if name in p_dict else p_dict_reverse.get(name))