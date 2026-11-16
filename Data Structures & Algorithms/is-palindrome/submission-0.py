class Solution:
    def isPalindrome(self, s: str) -> bool:
        l= 0 
        flag = True
        string = ("".join(filter(str.isalnum, s))).lower()


        r = len(string)-1


        while l < r:
            if string[l] != string[r]:
                return False
            l+=1
            r-=1
        return flag
        