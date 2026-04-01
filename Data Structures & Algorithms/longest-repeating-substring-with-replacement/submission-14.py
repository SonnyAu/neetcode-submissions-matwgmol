class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        chars = sorted(list(set(s)))
        print(chars)
        ans = 0
        for c in chars:
            l = 0
            count = 0

            for r in range(len(s)):
                if s[r] != c:
                    count += 1
                while count > k:
                    if s[l] != c:
                        count -= 1

                    l += 1
            
                ans = max(ans, r - l + 1)
        return ans