class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dupes = set()
        l = ans = 0
        for r in range(len(s)):
            if s[r] in dupes:
                while s[r] in dupes:
                    dupes.remove(s[l])
                    l += 1
            dupes.add(s[r])
            ans = max(ans, r - l + 1)

        return ans



        