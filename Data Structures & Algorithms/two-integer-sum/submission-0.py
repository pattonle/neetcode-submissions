class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i, n in enumerate(nums): 
            compliment = target - n
            if compliment in compliments:
                return [compliments[compliment],i]
            compliments[n]=i
            
