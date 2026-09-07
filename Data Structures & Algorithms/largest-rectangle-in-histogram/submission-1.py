from collections import namedtuple

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # compute next shortest left height
        # monostack is always increasing until we find something shorter
        mono = []
        # n sentinel bc n is furthest to left
        shortest_left = [n for _ in heights] 
        for i, h in enumerate(heights):
            # print(f"evaluating {h=}, with {mono=}, {shortest_left=}")
            while len(mono) > 0 and mono[-1][0] > h:
                h_prev = mono.pop()
                # print(f"found {h=}, the next shortest for {h_prev=}")
                shortest_left[h_prev[1]] = i # next shortest found
            # we want the index at which h exists
            mono.append((h,i))
        # print(f"evaluating {h=}, with {mono=}, {shortest_left=}")

        # repeat for the other way around. 
        # sentintel this time is -1, out of range towards the start
        mono = []
        shortest_right = [-1 for _ in heights] 
        for i in range(n - 1, -1, -1):
            h = heights[i]
            # print(f"evaluating {h=}, with {mono=}, {shortest_right=}")
            while len(mono) > 0 and mono[-1][0] > h:
                h_prev = mono.pop()
                # print(f"found {h=}, the next shortest for {h_prev=}")
                shortest_right[h_prev[1]] = i
            mono.append((h,i))

        # print(f'Done building\n   {shortest_left=}\n   {shortest_right=}')

        # now that we have our boundaries, we can compute the area

        largest = 0
        for i in range(n):
            hi = shortest_left[i]
            lo = shortest_right[i]
            width = hi - lo - 1 # -1 bc excluding these
            largest = max(largest, width * heights[i])
        
        return largest

                
                
            
        