import sys

f = open("s1.txt")
lines = f.readlines()
# lines = sys.stdin.readlines()
N, L = map(int, lines[0].strip().split())

for i in range(L, 101):
    if i % 2 == 0:
        if L % i == 0:
            continue
        else:
            for j in range(i):
                print(L - i // 2 + j)
            break
    else:
        if L % i == 0:
            for j in range(i):
                print(L - i // 2 + j)
            break
        else:
            continue
print("No")
