import bisect


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        close_tuples = [0, 1, 2]
        close_sum = nums[0] + nums[1] + nums[2]
        for i in range(n):
            L = i + 1
            R = n - 1
            while L < R:
                cur_sum = nums[i] + nums[L] + nums[R]
                if abs(cur_sum - target) < abs(close_sum - target):
                    close_tuples = [i, L, R]
                    close_sum = cur_sum

                if cur_sum > target:
                    R -= 1
                elif cur_sum < target:
                    L += 1
                else:
                    return sum(nums[id] for id in close_tuples)

        return sum(nums[id] for id in close_tuples)

    def threeSumClosestPlus(self, nums, target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        close_tuples = [0, 1, 2]
        close_sum = nums[0] + nums[1] + nums[2]
        for i in range(n):
            R = n - 1
            L = max(i + 1, bisect.bisect_left(nums, target - nums[i] - nums[R], i + 1, R) - 1)

            while L < R:
                cur_sum = nums[i] + nums[L] + nums[R]
                if abs(cur_sum - target) < abs(close_sum - target):
                    close_tuples = [i, L, R]
                    close_sum = cur_sum

                if cur_sum > target:
                    R -= 1
                elif cur_sum < target:
                    L += 1
                else:
                    return sum(nums[id] for id in close_tuples)

        return sum(nums[id] for id in close_tuples)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.threeSumClosest([-1, 2, 1, -4], 1))
    print(solution.threeSumClosestPlus([-3, -2, -5, 3, -4], -1))
    print(solution.threeSumClosestPlus([1, 1, 1, 0], 100))
