class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        s = sorted(nums)
       
        for i in range(len(nums)-2):
            if i > 0 and s[i] == s[i-1]:
                 continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if (s[l] + s[r]) > -s[i]:
                    r-=1
                elif (s[l] + s[r]) < -s[i]:
                    l+=1
                elif (s[l] + s[r]) == -s[i]:
                    final.append([s[i],s[l],s[r]])
                    l+=1
                    r-=1

                    while l < r and s[l] == s[l-1]:
                        l += 1

                    while l < r and s[r] == s[r+1]:
                        r -= 1
        return final




