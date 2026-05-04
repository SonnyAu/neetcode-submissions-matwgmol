class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
# i don't understand the point of using the memoization
        def dfs(i, t):
            if i >= len(nums):
                return False
            if t < 0:
                return False
            if t == 0:
                return True

            return dfs(i + 1, t - nums[i]) or dfs(i + 1, t)
        return dfs(0, target // 2)


        