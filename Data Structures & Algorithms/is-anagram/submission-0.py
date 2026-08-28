class Solution:
    def getAsciiIndex(self, s: str):
        if len(s) != 1:
            return -1
        else:
            return ord(s) - ord("a")
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0 for _ in range(26)]
        
        for x in s:
            letters[self.getAsciiIndex(x)] += 1

        for y in t:
            letters[self.getAsciiIndex(y)] -= 1

        for l in letters:
            if l != 0:
                return False

        return True