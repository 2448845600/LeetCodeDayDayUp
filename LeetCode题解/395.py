class Solution:
    # 超时
    def longestSubstring1(self, s: str, k: int) -> int:
        n = len(s)
        # dp = [[[0] * 26] * n] * n
        # dp[0][0][0] = dp[0][0][0] + 1 # 其实，这样做是不对的，因为[0] * 5是一个一维数组的对象，* 3的话只是把对象的引用复制了3次，比如，我修改multi[0][0]：

        dp = [[[0 for _ in range(26)] for _ in range(n)] for _ in range(n)]

        for t in range(n):
            id = ord(s[t]) - ord('a')
            for i in range(0, t + 1):
                for j in range(t, n):
                    dp[i][j][id] = dp[i][j][id] + 1
                pass

        max_len = 0
        for i in range(n):
            for j in range(n):
                flag = True
                count = 0
                for id in range(26):
                    if dp[i][j][id] > 0 and dp[i][j][id] < k:
                        flag = False
                        break
                    count += dp[i][j][id]
                flag = flag * count
                if flag:
                    max_len = max(max_len, j - i + 1)
        return max_len

    # 通过，不够优雅
    def longestSubstring(self, s: str, k: int) -> int:
        def divide(s: str, k: int):
            if len(s) < k:
                return 0
            min_existed_char = min(set(s), key=s.count)
            if s.count(min_existed_char) >= k:
                return len(s)
            else:
                return max(divide(_, k) for _ in s.split(min_existed_char))

        return divide(s, k)

    # 优雅
    def longestSubstring_short(self, s: str, k: int) -> int:
        # https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/pythonsi-xing-gao-ding-di-gui-xie-fa-by-godcat/
        for c in set(s):
            if s.count(c) < k:
                # 满足分割条件，进行分割
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == '__main__':
    solu = Solution()
    r = solu.longestSubstring(s="ababbc", k=2)
    print(r)
