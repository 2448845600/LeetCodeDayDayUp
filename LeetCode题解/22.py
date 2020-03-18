class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(left, right, s):
            if left == n:
                if right == n:
                    res.append(s)
                    return s
                else:
                    dfs(left, right + 1, s + ')')
            elif left > right:
                dfs(left, right + 1, s + ')')
                dfs(left + 1, right, s + '(')
            else:
                dfs(left + 1, right, s + '(')

        dfs(1, 0, "(")
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
