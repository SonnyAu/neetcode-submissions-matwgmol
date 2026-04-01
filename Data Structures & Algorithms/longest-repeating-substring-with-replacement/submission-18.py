class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        chars = set(s)
        for c in chars:
            l = 0
            flipped = 0
            for r in range(len(s)):
                if s[r] != c:
                    flipped += 1
                while flipped > k:
                    if s[l] != c:
                        flipped -= 1
                    l += 1
                length = max(length, r - l + 1)
        return length
        