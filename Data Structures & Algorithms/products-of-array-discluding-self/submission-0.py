'''

[1, 1, 2, 8, 48, 1] defined as everything multiplied by the left up to i

[1, 6, 24, 48, 48, 1] defined as everything by the right up to i 

so to get the prod of array except self, i want left up to i - 1, and then right after i + 1

nums[i] = left[i - 1] * right[i + 1]

'''

class Solution:

    def buildProductArray(self, nums: List[int]) -> List[int]:
        array = [1] # pad with 1's
        product = 1
        for n in nums:
            product *= n
            array.append(product)
        
        array.append(1) # pad with 1's
        return array


    def productExceptSelf(self, nums: List[int]) -> List[int]:

        fromLeft = self.buildProductArray(nums)
        fromRight = list(reversed(self.buildProductArray(reversed(nums))))

        array = []
        n = len(nums)
        for i in range(1, n + 1):
            array.append(fromLeft[i - 1] * fromRight[i + 1])
        
        return array
        

        