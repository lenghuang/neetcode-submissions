class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0 for _ in temperatures]
        # iterations = 0
        # print("range", list(range(len(temperatures) - 1, -1, -1)))
        for i in range(len(temperatures) - 1, -1, -1):
            j = i + 1
            # print(f"\nnow evaluating {i=}")
            while j < len(temperatures):
                # iterations += 1
                if temperatures[j] > temperatures[i]:
                    # j is warmer than current, and its j - i days away
                    dp[i] = j - i
                    # print(f"setting dp[{i}]=j-i, {j}-{i}={dp[i]=} because {temperatures[j]=} > {temperatures[i]=}")
                    break
                elif dp[j] > 0:
                    # j is not warmer, but it has the answer to someone who does
                    # we know j + dp[j] is warmer than j, is it warmer than i? 
                    if temperatures[j + dp[j]] > temperatures[i]:
                        dp[i] = dp[j] + j - i
                        # print(f"jumping dp[{i}]= dp[j] + j - i, {dp[j]}+{j}-{i}={dp[i]=}")
                        break
                    else:
                        # print(f"{j=}, for {temperatures[j + dp[j]]=} is colder than {temperatures[i]=}")
                        j += dp[j] # let's try again based on dp[j]
                else:
                    # print(f"moving on and dp[{j}] was zero")
                    # Just move on without setting anything
                    break

        # print(f"{iterations=}")
        return dp
