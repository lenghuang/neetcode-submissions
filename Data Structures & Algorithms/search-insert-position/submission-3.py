class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r, = 0, len(nums)
        while l < r: # r is not to be considered as a valid answer
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                # answer is on left side
                r = mid # r is excluded in the guard, so don't need to - 1
            else:
                # answer is on the right side
                l = mid + 1 # l needs to exceed mid/r and make progress
        
        # at this point l == r
        return l
