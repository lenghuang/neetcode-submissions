class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def myprint(self, *args):
            debug = False
            if debug:
                print(*args)
        
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            myprint("lo, mid, hi", lo, mid, hi)
            myprint("looking at nums[mid], nums[", mid, "] = ", nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                myprint("mid is lower")
                lo = mid + 1
            else:
                myprint("mid is higher")
                hi = mid - 1
        
        return -1
            