'''
[3,4,5,6,1,2]

brute force is just O(n) greedy
key insight: sorted, try binary search?

[3, 4, 5, 6, 1, 2]
 lo    mid      hi

comparing (3, 5, 2)

normal binary search if mid is bigger than target, go to smaller half
in here, target is min
if mid is bigger than min, go to lesser half
but how do we know if mid is bigger than min?

lo is 3, mid is 5, hi is 2

intuitively, smaller number is on the right side since 2 < 3, so prob go to the right

[3, 4, 5, 6, 1, 2]
       lo mid     hi

comparing (5, 6, 2)

not sure if i reuse 5 or not <-- come back to this

still keep going to the right side

and we get to 1, and everything is next to each other, so we settle on one

what about other example?

[4,5,0,1,2,3]

comparing (4, 0, 3)

intuitively, smaller number is on the right, since mid is smaller than both so go to smaller side


so what are our general rules

given (x, y, z)

if x < y and y < z, go to the left (ex: 1,2,3)
if x < y and y > z, 
- and x <= z go to the left (ex: 1,4,3)
- and x > z go to the right (ex: 3,4,1)
if x > y and y > z, not possible bc rotated + sorted? (ex: 3,2,1)
if x > y and y < z
- and x > z, go to the right (ex: 4,0,3)
- and x <= z, go to the right (ex: 3,0,4) -> not possible bc  x <= z > y < x

maybe, generically, for x, y, z, go to the side that the smallest number is on?

for x, y, z, one of these numbers is the smallest

go to the side that the smallest is on

but if y is the smallest

(9, -2, 3) -> go left

(3, -2, 9) -> go right
'''

class Solution:
        
    def findMin(self, nums: List[int]) -> int:

        def getLeft(lo, mid, hi):
            new_hi = mid
            # print("going left, new params lo:", lo, "hi:", new_hi)
            return new_hi

        def getRight(lo, mid, hi):
            new_lo = mid
            # print("going right, new params lo:", new_lo, "hi:", hi)
            return mid

        # while lo != hi
        # compute mid
        # run the rules
        # update lo/hi
        # return nums[mid]
        lo, mid, hi = 0, 0, len(nums) - 1
        attempts = 0
        while lo < hi and attempts < 30:
            attempts += 1
            mid = (lo + hi) // 2 # potential infinite loop / off by one
            x, y, z = nums[lo], nums[mid], nums[hi]
            print("Evaluating", x, y, z)
            smallest = min(x, y, z)
            if x == y or y == z:
                return smallest
            elif smallest == y and x <= z:
                lo = getRight(lo, mid, hi)
            elif smallest == y and x > z:
                hi = getLeft(lo, mid, hi)  
            elif smallest == x:
                hi = getLeft(lo, mid, hi)
            elif smallest == z:
                lo = getRight(lo, mid, hi)
            else:
                raise Exception("incorrect assumption about sort order")
        return nums[mid]

        
        