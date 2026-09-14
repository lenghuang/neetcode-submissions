class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g = sorted(g)
        s = sorted(s)
        i = 0
        j = 0
        happy = 0
        
        while i < len(g) and j < len(s):

            # Cookie s[j] big enough for child g[i]
            if s[j] >= g[i]:
                happy += 1
                j += 1
                i += 1
            
            # Cookie not big enough, try bigger cookie
            else:
                j += 1

        return happy