class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            a, b = divmod(num, 2)
            if b == 1:
                num = num - 1
            else:
                num = a
            count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSteps(123))
