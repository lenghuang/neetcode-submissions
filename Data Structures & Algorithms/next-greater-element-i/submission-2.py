'''
strawman, 

build a map of nums2 val to nums2 index

for each thing in nums1, find the equal one in nums2, then loop to find next greatest

O(nums1 * nums2)
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {v: k for k, v in enumerate(nums2)}
        res = []
        for n in nums1:
            j = map[n] # nums1 is a subset of nums2
            next_greatest = -1
            for m in nums2[j+1::]:
                if m > n:
                    next_greatest = m
                    break
            res.append(next_greatest)
        return res