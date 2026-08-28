'''
Recall our valid parantheses from 15-251:
- () in L
- (x) in L if x in L
- xy in L for x,y in L

Recall that we had a way to iteratively think about this:
- We have equal number of open and close
- At any point in time, we have more opens than closes
    - Intuition is that as we scan from left to right, as we see more opens, we'll be able to close it later
    - If we have more closes, then that means we closed something that was never open, which is invalid
    
All that's left now is to turn that into code. Keep adding opens while a condition is true, otherwise add closes. In other words, we can always add opens since it will be still valid (if o > 0), add. However, we can only add a close if we have more opens than closes (c > o, since we are subtracting the number of things). In other words c = n - # of closes, and o = n - # of opens.
'''

class Solution:
        
    def recurse(self, o, c, acc, res):
        if(o == 0 and c == 0):
            res.append(acc)
        if(o > 0):
            self.recurse(o - 1, c, acc + "(", res)
        if(c > o):
            self.recurse(o, c - 1, acc + ")", res)


    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.recurse(n, n, "", res)
        return res

        