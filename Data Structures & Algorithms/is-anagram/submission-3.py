class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = {}
        string2 = {}
        for c in s: 
            if c not in string1:
                string1[c] = 1
            if c in string1:
                string1[c] += 1
        
        for c in t:
            if c not in string2:
                string2[c] = 1
            if c in string2:
                string2[c] += 1
        return string1 == string2
        

            

