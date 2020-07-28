"""
快速排序

https://www.jianshu.com/p/2b2f1f79984e
"""


def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)


def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L


def Partition(L, left, right):
    """
    选取 L[left] 作为基准 pivot_value，耗费额外一个空间保存；
    从右到左，找大于 pivot_value 的值，换掉L[left], 现在，L[right]就空余了；
    从左往右，找小于 pivot_value 的值，换掉 L[right]，现在，L[left]就空余了：
    ......
    知道left >= right
    此时，left 是空余的，把 pivot_value 放在这

    """
    pivot_value = L[left]

    while left < right:
        while left < right and L[right] >= pivot_value:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] < pivot_value:
            left += 1
        L[right] = L[left]
    L[left] = pivot_value
    return left


if __name__ == '__main__':
    L = [1, 3, 0, 5, 7, 9, 8, 6, 4, 2]
    ans = quick_sort(L)
    print(ans)
