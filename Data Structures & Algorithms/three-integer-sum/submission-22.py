class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        #[-4, -1, -1, 0, 1, 2]
        for i, a in enumerate(nums):
            if nums[i] == nums[i - 1] and i > 0:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans
        
        