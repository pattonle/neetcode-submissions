class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        curr = 1
        num = [1] * len(nums)
        for i in range(length):
            num[i] = curr
            curr *= nums[i]
        curr = 1
        for i in range(length-1,-1,-1):
            num[i] *= curr
            curr *= nums[i]
        return num