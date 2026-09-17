'''
sort the array

let target = 0 ?

assume you have def twoSum()

for n in nums:
    i == twoSum(of it) ? 

sort nums

[-4,-1,-1,0,1,2]

looking at -4, i need two numbers that sum to 4 -> none
look at -1, i need two numbers that sum to 1, start low, and hi, meet in middle?

-1 2, works 
0,1, works

add both
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        i = 0
        res = []

        while i < len(nums):         
            j = i + 1
            k = len(nums) - 1
            x = nums[i]
            while j < k:
                y, z = nums[j], nums[k]
                if x + y + z == 0: 
                    res.append([x,y,z])
                    while k > 0 and nums[k] == z:
                        k -= 1
                    while j < len(nums) and nums[j] == y:
                        j += 1
                elif x + y + z > 0:
                    k -= 1
                else:
                    j += 1
                
            while i < len(nums) and nums[i] == x:
                i += 1

        return res
                

        