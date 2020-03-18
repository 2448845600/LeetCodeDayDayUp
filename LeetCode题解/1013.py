class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        def step_add(A):
            n = len(A)
            b = [0 for _ in range(n)]
            b[0] = A[0]
            for i in range(1, n):
                b[i] = b[i - 1] + A[i]

            return b

        n = len(A)

        all_sum = sum(A)
        left_sum = step_add(A)
        right_sum = step_add(A[::-1])

        print(all_sum)
        print(left_sum)
        print(right_sum)

        for i in range(n - 2):
            for j in range(n - 2 - i):
                if left_sum[i] == right_sum[j] and left_sum[i] == (all_sum - left_sum[i] - right_sum[j]):
                    return True
        return False

    def canThreePartsEqualSumPlus(self, A) -> bool:
        def step_add(A):
            n = len(A)
            b = [0 for _ in range(n)]
            b[0] = A[0]
            for i in range(1, n):
                b[i] = b[i - 1] + A[i]
            return b

        n = len(A)

        all_sum = sum(A)

        # 加速 1
        if all_sum % 3 != 0:
            return False

        one_three_sum = all_sum // 3
        left_sum = step_add(A)
        right_sum = step_add(A[::-1])

        for i in range(n - 2):
            # 加速 2
            if left_sum[i] == one_three_sum:
                for j in range(n - 2 - i):
                    if right_sum[j] == one_three_sum:
                        return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
