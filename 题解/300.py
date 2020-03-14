class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        tmp = []
        for i in range(len(nums)):
            j = bisect.bisect_left(tmp, nums[i])
            if j >= len(tmp):
                tmp.append(nums[i])
            else:
                tmp[j] = nums[i]

        return len(tmp)


