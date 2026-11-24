class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        final = 0 
        for r in range(len(prices)):
            if prices[r] >= prices[l]:
                final = max(final, prices[r]-prices[l])
            else:
                l=r
        return final
            

            

            

