class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lookup = {}
        for n in nums:
            if not n in lookup:
                lookup[n] = True

        starters = []
        for n in lookup.keys():
            if not n - 1 in lookup:
                starters.append(n)

        res = 0
        for start in starters:
            k = start
            k_len = 0
            while k in lookup:
                k += 1
                k_len += 1
            res = max(res, k_len)

        return res


'''

since order doesn't matter, can I keep track of a hash set?

this way, I only need to see what numbers exist?

Example 1: { 2, 3, 4, 5, 10, 20 }
Example 2: { 0, 1, 2, 3, 4, 5, 6 }

I mean, I'd still like to sort that, but that's still worst case n log n...

In O(n), I can find the min of the list?

I find 0, and keep adding +1 until I've "marked" the entire list

After that, I find the min of what's not marked

This sounds like O(n^2), but since I'm marking things, it's not since

I will consider every element at most once

Hm but I still don't know where to start 



'''