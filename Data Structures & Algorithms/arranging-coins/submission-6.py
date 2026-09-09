class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        res = 0
        for i in range(1, n + 1):
            
            coins = i * (i + 1) / 2
            if coins <= n:
                res = i
            else:
                break
        
        return res
        
        