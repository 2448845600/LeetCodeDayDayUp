import sys


def insort(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            lo = mid + 1
        else:
            hi = mid
    a.insert(lo, x)


def get_hindex(T, A):
    sorted_list = []
    pos = 0
    hindex = []
    for i in range(T):
        insort(sorted_list, A[i])
        if sorted_list[pos] >= pos + 1:
            pos += 1
        hindex.append(pos)
    return hindex


f = open("1.txt")
lines = f.readlines()
# lines = sys.stdin.readlines()
N = int(lines[0].strip())
for i in range(N):
    T = int(lines[2 * i + 1].strip())
    A = list(map(int, lines[2 * i + 2].strip().split()))
    print(get_hindex(T, A))
