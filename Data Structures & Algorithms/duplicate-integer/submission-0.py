class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            if n in freq:
                return True
            else:
                freq[n] = 1
        return False 