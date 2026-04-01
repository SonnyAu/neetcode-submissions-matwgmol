class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            index = nums.index(num)
            for i in range(index + 1, len(nums)):
                if nums[i] + num == target:
                    return [index, i]

        