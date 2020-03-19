import sys

lines = sys.stdin.readlines()
l, r = map(int, lines[0].strip().split())

def get_three(i):
    if i % 3 == 0:
        return (i // 3) * 2
    else:
        return (i // 3) * 2 + (i % 3 == 2)

res = get_three(r) - get_three(l - 1)
print(res)

# 编译器选择 "Python3(3.5.2)"，"pypy3(3.6.1)"有问题