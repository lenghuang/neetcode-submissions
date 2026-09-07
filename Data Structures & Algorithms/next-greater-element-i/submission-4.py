'''
strawman, 

build a map of nums2 val to nums2 index

for each thing in nums1, find the equal one in nums2, then loop to find next greatest

O(nums1 * nums2)

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

Now, can we make the computation of next greatest with a monotonic stack?

If the thing is less, add to the stack
If the thing is greater, pop from the stack, and set the value of the thing its greater for

[] look at 1, nothing greater than it
[1] look at 3, it's greater than 1. pop 1 and set that value's next greatest to 3
[3] look at 4, it's greater than 3. pop 3 and set that value's next greatest to 4
[4] look at 2, it's not greater than set that to -1

so 1 -> 3
so 4 -> doesn't get popped
so 2 -> not greater

'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) == 0:
            return []
        
        map_1 = {v: k for k, v in enumerate(nums1)}
        
        res = [-1] * len(map_1)
        stack = []

        for m in nums2:
            if len(stack) == 0:
                stack.append(m)
            else:
                while m > stack[-1]: # next greatest found
                    n = stack.pop()
                    if n in map_1:
                        i = map_1[n]
                        res[i] = m
                    if len(stack) == 0:
                        break
                # now it is not greater than anything else in the stack, add it back
                stack.append(m)
        
        # at this point everything else not greater is just left with -1
        return res
            
