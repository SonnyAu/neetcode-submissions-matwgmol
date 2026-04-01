class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        anagrams = {}

        for string in strs:
            key = tuple(sorted(string))
            if key not in anagrams:
                anagrams[key] = []
        
        
        for key in anagrams:
            for string in strs:
                if tuple(sorted(string)) == key:
        
                    anagrams[key].append(string)
        
        return list(anagrams.values())
        