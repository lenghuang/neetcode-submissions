'''
row i takes i coins

keep summing until acc < n: no longer holds

return iterations


'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = 0
        rows = 0
        while coins + rows < n:
            rows += 1
            coins += rows
        
        return rows
