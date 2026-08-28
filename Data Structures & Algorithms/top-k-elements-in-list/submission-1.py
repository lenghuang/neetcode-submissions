class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        buckets = [[] for _ in range(len(nums))]
        
        for num, occurrences in freq.items():
            buckets[occurrences - 1].append(num)
        
        elem_count = 0
        res = []
        
        for bucket in reversed(buckets):
            for num in bucket:
                if (elem_count == k):
                    return res
                res.append(num)
                elem_count += 1

        return res
                
            