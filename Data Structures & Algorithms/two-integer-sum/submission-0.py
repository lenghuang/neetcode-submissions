class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, n in enumerate(nums):
            leftover = target - n
            if leftover in num_to_index:
                return [num_to_index[leftover], i]
            
            num_to_index[n] = i
        
        return [-1, -1]
                