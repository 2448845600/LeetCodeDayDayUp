def hIndex(citations) -> int:
    def bi_search(a):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] >= mid + 1:
                lo = mid
            else:
                hi = mid + 1
            print("{}-{}".format(lo, hi))
        return lo

    return bi_search(citations[::-1])


print(hIndex([0, 1, 3, 5, 6]))
