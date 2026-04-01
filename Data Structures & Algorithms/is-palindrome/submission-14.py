class Solution:
    def isPalindrome(self, s: str) -> bool:


        s = s.strip()
        s = s.replace(" ", "")
        l = 0
        r = len(s) - 1
        print(s)

        while l < r:
            left = s[l].lower()
            right = s[r].lower()
            if not left.isalnum():
                l += 1
                continue
            if not right.isalnum():
                r -= 1
                continue
            elif left != right:
                return False
            l += 1
            r -= 1
        return True

            
        