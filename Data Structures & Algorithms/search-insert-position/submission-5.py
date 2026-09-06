class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Pattern 2, "Half-Open" Interval
        # l can be in the answer, r cannot
        l = 0
        r = len(nums) # r is not a valid answer
        while l < r:
            # choose to round down
            mid = (l + r) // 2
            # answer is bigger, move up. mid rounds down, so + 1
            if nums[mid] < target:
                l = mid + 1
            # r is not part of loop, so set to mid
            else:
                r = mid
        # now l == r, return
        return l
