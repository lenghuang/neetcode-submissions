class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        triplets = []
        for i, n in enumerate(nums_sorted):
        

            if i > 0 and n == nums_sorted[i - 1]:
                continue
                
            lo = i + 1
            hi = len(nums) - 1

            while lo < hi:
                res = nums_sorted[lo] + nums_sorted[hi] + n
                if res < 0:
                    lo += 1
                elif res > 0:
                    hi -= 1
                else:
                    triplets.append([nums_sorted[lo], nums_sorted[hi], n])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums_sorted[lo] == nums_sorted[lo - 1]:
                        lo += 1
            
        return triplets 
