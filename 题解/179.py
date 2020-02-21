class Solution:
    def largestNumber(self, nums) -> str:
        from functools import cmp_to_key

        def func(x, y):
            if x + y < y + x:
                return 1
            elif x + y == y + x:
                return 0
            else:
                return -1

        nums = [str(num) for num in nums]
        nums = sorted(nums, key=cmp_to_key(func))
        res = ''.join(nums)

        return '0' if res[0] == '0' else res


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([3, 30, 34, 5, 9]))
