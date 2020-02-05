class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n < 4:
            return max(nums)

        def dfs(i, pre_sum, end):
            if i < end:
                return max(dfs(i + 2, pre_sum + nums[i], end), dfs(i + 1, pre_sum, end))
            return pre_sum

        return max(dfs(2, nums[0], n - 1), dfs(1, 0, n))

    def robPlus(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n < 4:
            return max(nums)

        max_sum = 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = nums[0]
        for i in range(1, n - 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        max_sum = max(dp[i][0], dp[i][1], max_sum)

        dp = [[0, 0] for _ in range(n)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        max_sum = max(dp[i][0], dp[i][1], max_sum)

        return max_sum

    def robPlusPlus(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n < 4:
            return max(nums)

        def main(nums):
            n = len(nums)
            pre = nums[0]
            cur = max(nums[0], nums[1])
            for i in range(2, n):
                temp = cur
                cur = max(pre + nums[i], cur)
                pre = temp
            return cur

        return max(main(nums[0:n - 1]), main(nums[1:]))


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 3, 2]))
    print(s.robPlus([]))
    print(s.robPlus([2, 3, 2]))
    print(s.robPlus([1, 2, 3, 1]))

    print(s.robPlusPlus([]))
    print(s.robPlusPlus([2, 3, 2]))
    print(s.robPlusPlus([1, 2, 3, 1]))
