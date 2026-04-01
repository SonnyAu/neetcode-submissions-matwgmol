class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ans = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            max_water = base * height
            ans = max(ans, max_water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans
        