class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda x : x[1], reverse=True)

        return [num for num, freq in sorted_freq[:k]]