from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for char in s:
            if s_count[char]:
                s_count[char] += 1
            else:
                s_count[char] = 1

        for char in t:
            if t_count[char]:
                t_count[char] +=1
            else:
                t_count[char] = 1

        return s_count == t_count

        