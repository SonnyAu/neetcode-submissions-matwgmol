class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        biggest = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            biggest = max(biggest, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1 

        return biggest
        