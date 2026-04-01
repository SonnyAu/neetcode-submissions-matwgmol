class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = curr = left = 0

        for right in range(len(s)):
            while s[right] in s[left:right]:
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        