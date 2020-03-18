class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        leftCanJump = n-1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= leftCanJump:
                leftCanJump = i
        return leftCanJump == 0
