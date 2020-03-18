class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = [[0 for _ in range(3)] for _ in range(n)]

        for k in range(1, 3):
            prof = dp[0][k - 1] - prices[0]
            for i in range(1, n):
                prof = max(prof, dp[i][k - 1] - prices[i])
                dp[i][k] = max(dp[i - 1][k], prices[i] + prof)
        return max(dp[-1][1], dp[-1][2])


if __name__ == '__main__':
    s = Solution()
    # print(s.maxProfit([2, 1, 2, 0, 1]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
