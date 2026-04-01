class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = ans = 0
        r = len(heights) - 1

        while l < r:
            vol = min(heights[l], heights[r]) * (r - l)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1 

            ans = max(ans, vol)


        return ans
        

        