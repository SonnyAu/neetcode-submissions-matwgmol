from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for s in strs:
            anagram = "".join(sorted(s))
            anagrams[anagram].append(s)

        group_anagrams = list(anagrams.values())

        return group_anagrams


        