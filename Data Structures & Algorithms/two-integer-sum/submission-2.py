class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i,n in enumerate(nums):
            comp = target - n 
            if comp not in compliments:
                compliments[n] = i 
            else: 
                return [compliments[comp],i]
        return []


