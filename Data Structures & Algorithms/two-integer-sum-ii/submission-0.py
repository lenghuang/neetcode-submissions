class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            if numbers[lo] + numbers[hi] < target:
                lo += 1
            elif numbers[lo] + numbers[hi] > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]
        
        return [lo + 1, hi + 1]

'''
How would i do this with o(n) space?

[1,2,3,4]
[2,1,0,-1] (difference with target)

How can I leverage the fact that it's sorted?

Two pointers?

[1,2,4,6,8,12,21,42], t = 18

[1,42]
[1,21]
[1,12]
[2,12]
[4,12]
[6,12]

Observe
- sorted
- only one valid solution

so there will only ever be one nums[i] + nums[j] == target and we just have to find it 

but what if we look too far past i? 
or look too far past j?

we won't because sorted, so nums[i] < nums[j] always true

so 

if nums[i] + nums[j] < target, we make the number bigger by increasing lo
else, we make the number smaller by dereasing hi

and only one number where nums[i] + num[j] == target true
'''        