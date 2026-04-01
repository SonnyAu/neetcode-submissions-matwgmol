class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        left = 0
        if len(s) > len(t) or len(t) > len(s):
            return False
        for i in t:
            if i != s[left]:
                print(i)
                print(s[left])
                return False
            left += 1
        return True

        