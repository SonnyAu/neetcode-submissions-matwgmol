from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_map = Counter(s1)
        window_map = Counter(s2[:len(s1)])

        if s1_map == window_map:
            return True

        for i in range(len(s1), len(s2)):
            left_char = s2[i-len(s1)]
            right_char = s2[i]

            window_map[left_char] -= 1
            window_map[right_char] += 1

            if window_map[left_char] == 0:
                del window_map[left_char]

            if window_map == s1_map:
                return True
        return False