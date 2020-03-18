class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums = sorted(nums)
        res = []

        for i in range(n):
            for j in range(i + 1, n):
                cur_sum = nums[i] + nums[j]
                for k in range(j + 1, n):
                    if cur_sum + nums[k] == 0:
                        existed = False
                        for a, b, c in res:
                            if a == nums[i] and b == nums[j]:
                                existed = True
                                break
                        if not existed:
                            res.append([nums[i], nums[j], nums[k]])
        return res

    def threeSum2(self, nums):
        n = len(nums)
        nums = sorted(nums)
        res = []

        for i in range(n - 1):
            if nums[i] <= 0:
                # 去重
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                # 将暴力解法的后两次循环o(n^2)换成了双指针o(n)，总时间复杂度从o(n^3) -> o(n^2)
                left = i + 1
                right = n - 1
                while (right > left):
                    if nums[i] + nums[left] + nums[right] == 0:
                        res.append([nums[i], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1

                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum2(nums=[-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum2(nums=[0, 0, 0]))
