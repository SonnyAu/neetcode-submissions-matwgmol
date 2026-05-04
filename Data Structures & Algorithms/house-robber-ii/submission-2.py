class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]

        def helper(nums):
            
            memo = [-1] * len(nums) 

            def dfs(i):
                if i >= len(nums):
                    return 0
                if memo[i] != -1:
                    return memo[i]
                memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
                return memo[i]
            return dfs(0)
        
        no_first = nums[1:]
        no_last = nums[:-1]

        return max(helper(no_first), helper(no_last))


        