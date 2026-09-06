class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # pattern 1, closed, meaning l, r is a valid answer
        l, r = 0, len(nums) - 1
        # loop must keep running as long as there is valid element, and r is valid
        while l <= r:
            mid = (l + r) // 2 # same regardless
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                # target is on left side, r won't be considered
                r = mid - 1
            else:
                # target is on right side, l won't be considered
                l = mid + 1

        # at this point, l is greater than r
        # we want this bc it would be inserted there
        return l