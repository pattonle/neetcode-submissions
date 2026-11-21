class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        best = 0
        while L < R:
            currheight = min(heights[L],heights[R])
            curr = currheight * (R-L)
            best = max(best,curr)
            if heights[L] > heights[R]:
                R-=1
            else:
                L+=1
        return best

        