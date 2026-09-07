class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        dp = [0 for _ in range(n)]
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[i] >= temperatures[j]: # not warmer
                if dp[j] == 0: # no prev answer
                    break
                # jump to prev answer, let loop guard eval
                j += dp[j]
            
            # if warmer
            if temperatures[i] < temperatures[j]:
                dp[i] = j - i

        return dp