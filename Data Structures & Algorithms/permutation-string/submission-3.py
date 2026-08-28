'''


does s2 contain s1?

get the counts from s1

then check counts on a sliding window for s2, fora. window of size len(s1)


s1 = { a : 1, b : 1, c : 1 }

s2 window of 3 is

"lec", "eca", "cab", "abe", bee"

and "cab" has the same counts

but do you need to do an equality check on the dict every time? that's O(s1) * O(s2) then

i guess technically O(s1) * O(s2) / O(s1) so is fine?

just do equality for now

what if you start with, 

{ a : 1, b : 1, c : 1 },

then 'l,e,c' gets you { a : 1, b : 1, c : 0 },
then 'e,c,a' gets you { a : 0, b : 1, c : 0 },
then 'c,a,b' gets you { a : 0, b : 0, c : 0 }, and they're all 0!

though a "zero" count is still the same, just more memory efficient? 

no need freq map for init still

then 'a,b,e' gets you { a : 0, b : 0, c : 1 }, and they're all 0!
'''

class Solution:
    
    def debug(self, *args):
        # print(*args)
        return

    def getFreqMap(self, s: str) -> dict:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        self.debug('~~ getFreqMap', freq)
        return freq

    def allValuesZero(self, freq: dict) -> bool:
        self.debug('~~ allValuesZero', freq)
        for v in freq.values():
            if v != 0:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = self.getFreqMap(s1)
        for j in range(len(s2)):
            i = j - len(s1) + 1
            self.debug("evaluating string", s2[max(i,0):j+1])
            if s2[j] in freq: 
                self.debug("- decrementing s2[j]", s2[j], "at index", j)
                freq[s2[j]] -= 1
            if self.allValuesZero(freq):
                return True
            if i >= 0 and s2[i] in freq:
                self.debug("+ incrementing s2[i]", s2[i], "at index", i)
                freq[s2[i]] += 1
        
        return self.allValuesZero(freq)

        
        