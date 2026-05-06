class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False

        def dfs(i, target):
            if i >= len(nums):
                return False
            if target < 0:
                return False
            if target == 0:
                return True
            return dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
        return dfs(0, target // 2)

        