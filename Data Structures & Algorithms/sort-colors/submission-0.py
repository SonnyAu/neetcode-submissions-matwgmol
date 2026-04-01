class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for n in nums:
            colors[n] += 1
        print(colors)
        for n in range(0, colors[0]):
            nums[n] = 0
        for n in range(colors[0], colors[0] + colors[1]):
            nums[n] = 1
        for n in range(colors[0] + colors[1], colors[0] + colors[1] + colors[2]):
            nums[n] = 2
        return nums