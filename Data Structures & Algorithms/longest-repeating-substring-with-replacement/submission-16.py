class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        chars = set(s)
        ans = 0
        for c in chars:
            l = count = 0

            for r in range(len(s)):
                if s[r] != c:
                    count += 1
                while count > k:
                    if s[l] != c:
                        count -= 1
                    l += 1

                ans = max(ans, r - l + 1)
                

        return ans