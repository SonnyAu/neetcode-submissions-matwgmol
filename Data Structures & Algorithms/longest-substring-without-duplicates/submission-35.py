class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            while c in seen:
                if s[l] in seen:
                    seen.remove(s[l])
                l += 1
            seen.add(c)
            ans = max(ans, r - l + 1)
        return ans

                

        