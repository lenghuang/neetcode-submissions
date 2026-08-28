class Solution:

    def findLongestSubstring(self, s: str) -> str:
        # Debugging printer
        def myPrint(*args):
            if False:
                print(*args)

        def maxSubstr(s1, s2):
            if len(s1) > len(s2):
                myPrint("longest substr", s1)
                return s1
            else:
                myPrint("longest substr", s2)
                return s2

        i = 0
        longest = ""
        substr = ""

        c_so_far = {}
        for c in s:
            c_so_far[c] = False

        lo = 0
        hi = 0
        while hi < len(s):
            c = s[hi]
            myPrint("looking at char", c, "and dict", c_so_far, "and substr", substr)
            # if the next char is the same, skip
            if c_so_far[c]:
                myPrint("duplicate")
                longest = maxSubstr(longest, substr)
                c_so_far[s[lo]] = False
                lo += 1
                substr = s[lo:hi]
            # else add it to substr
            else:
                myPrint("increment")
                substr += c
                c_so_far[c] = True
                hi += 1


        # Check again
        longest = maxSubstr(longest, substr)

        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        return len(self.findLongestSubstring(s))