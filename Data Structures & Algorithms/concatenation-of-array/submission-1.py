class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        newArr = [0] * len(nums) * 2
        for i in range(len(nums)):
            newArr[i] = nums[i]
            newArr[len(nums) + i] = nums[i]

        return newArr


        