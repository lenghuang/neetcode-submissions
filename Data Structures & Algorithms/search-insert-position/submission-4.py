class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Pattern 1 "Closed" interval
        # l, r can both be in the answer
        l = 0
        r = len(nums) - 1 # r can be answer, so - 1
        while l <= r:
            # choose to round down
            mid = (l + r) // 2 
            # look for answer in the interval
            if nums[mid] == target:
                return mid
            # answer is bigger, move up.mid already considered, so mid + 1
            elif nums[mid] < target:
                l = mid + 1
            # answer is smaller, move down. mid already considered, so mid - 1
            else:
                r = mid - 1
        # now, l > r. return l if u want insert point after
        return l