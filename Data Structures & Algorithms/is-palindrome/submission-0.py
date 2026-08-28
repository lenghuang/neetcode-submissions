class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            # Skip numbers
            if not s[lo].isalnum():
                lo += 1
                continue
            if not s[hi].isalnum():
                hi -= 1
                continue

            # Compare left and right, but lowercase
            if (s[lo].lower() != s[hi].lower()):
                return False

            # Keep looking
            lo += 1
            hi -= 1
                
        return True