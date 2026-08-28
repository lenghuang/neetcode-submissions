class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        lo = 0
        hi = len(heights) - 1
        while (lo < hi):
            h = min(heights[lo], heights[hi]) 
            w = hi - lo
            res = max(res, h * w)
            
            if (heights[lo] < heights[hi]):
                lo += 1
            else: 
                hi -= 1

        return res
