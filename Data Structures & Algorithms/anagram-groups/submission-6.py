from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            anagram = "".join(sorted(list(s)))
           
            anagrams[anagram].append(s)

        return list(anagrams.values())

        
        