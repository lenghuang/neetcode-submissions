'''

The amount of rain water it can trap is

its own height ---> its own height, or something taller

so in the first example

[0,2,0,3]

we can trap 2 at point 0 

maybe, given any two points, we can compute the area between them?

given h1, h2

if h1 == h2, then its their indexes subtracted * heights - whatever heights are in between

if h1 < h2, then same but h1

so we'll have to recompute stuff with heights in between a lot 

let's brute force this first

- compute all possible areas and pick the max
- look at all pairs of heights (O(n^2))
  - for each pair, check if theirs something equal or taller in between
  - if so, area = 0
  - else, do area - whatever heights in between are (O(n))

this is an O(n^3) algo

where can I improve?
- am doing a lot of checking if there's something equal or taller in between, can i improve that?
   - list of max height so far or something at each point? 
   - from left: [0,2,2,3,3,3,3,3,3,3]
   - from right: [3,3,3,3,3,3,3,3,2,1]
   - this gets me tallest thing from left and from right
   - so if lo = 0, hi = 9, then I know i am comparing [0,1]... hm but idk if i learned anyything from that.-.

- am checking a lot of "whatever heights are in between", how can avoid doing that? 
- max amount of water in that specific column? 

so at index 5, tallest thing to left is 3, tallest thing to right is 3, height is 0, can store 3 waters there
at index 4, its' 2 waters

at index 0, its 0 waters, index 3, it's 2 waters

so using that "tallest thing to the left" and "tallest thing to the right" get a list of waters at each index

left  [0,2,2,3,3,3,3,3,3,3]
right [1,2,3,3,3,3,3,3,3,3]

i = 5, tallest things are both 3, but height is 0, so 3
i = 4, tallest things are both 3, but height is 1, so 2
i = 3, tallest things are both 3, but height is 3, so 0
i = 2, tallest things are 2,3, so min is 2, height is 0, so 2

so now i can build this up to be 

heights = [0,0,2,0,2,3,2,0,0,0]

i got pretty close! i got [0, 0, 2, 0, 2, 3, 2, 0, 1, 2]

right now, because 3 is the max so far, i am getting the 1, 2 at the end because its getting perceieved as height

at the last index, the tallest from the left is 3

but it also doesn't makes sense since the tallest from the right at this point should be 1, or at least 0 

should I be flipping my thing around? 

and pick the largest sum with sliding window or something

'''

class Solution:

    def heightsFromLeft(self, height: List[int]) -> List[int]:
        from_left = []
        n = len(height)
        for i in range(n):
            if i == 0:
                from_left.append(height[i])
            else:
                from_left.append(max(height[i], from_left[-1]))
        return from_left

    def heightsFromRight(self, height: List[int]) -> List[int]:
        from_right = []
        n = len(height)
        for i in reversed(range(n)):
            if i == n - 1:
                from_right.append(height[i])
            else:
                from_right.append(max(height[i], from_right[-1]))
        return list(reversed(from_right))

    def getWaterHeights(self, height: List[int], from_left: List[int], from_right: List[int]) -> List[int]:
        water_height = []
        for i, h in enumerate(height):
            side_height = min(from_left[i], from_right[i])
            leftover_height = max(side_height - h, 0)
            water_height.append(leftover_height)
        return water_height

    def getMaxTrap(self, water_height: List[int]) -> int:
        res = 0
        for h in water_height:
            res += h    
        return res

    def trap(self, height: List[int]) -> int:
        from_left = self.heightsFromLeft(height)  
        from_right = self.heightsFromRight(height) 
        water_height = self.getWaterHeights(height, from_left, from_right)
        
        return self.getMaxTrap(water_height)



