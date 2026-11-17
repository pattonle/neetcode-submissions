class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        final = []
        while strs:
            s = strs.pop()
            sorteds = "".join(sorted(s))
            if sorteds not in anagrams:
                anagrams[sorteds] = [s]
            else: 
                anagrams[sorteds].append(s)
        for value in anagrams.values():
            final.append(value)
        return final