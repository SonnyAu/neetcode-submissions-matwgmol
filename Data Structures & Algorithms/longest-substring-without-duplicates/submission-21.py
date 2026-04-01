class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        if s == "":
            return 0
        curr = ''

        for right in range(len(s)):
            if s[right] not in curr:
                curr += s[right]
                ans = max(ans, len(curr))
            else:
                left += curr.index(s[right]) + 1
                curr = s[left:right+1]
        return ans
        