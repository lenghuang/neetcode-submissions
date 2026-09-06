'''
[1,4,3,2], 9 hours to eat bananas

k = 2 ? 

1,2,3,4

minimum hours?

what determines minimum? 2 was not the smallest pile, but if we did 1, that would exceed 9

so we're searching for something here

how to compute "time it woudl take" ? 

1/1 = 1 hour
4/1 = 4 hours
3/1 = 3 hours

1/2 = 1 hour
4/2 = 2 hours
3/2 = 2 hour
2/2 = 1 hour

sum of (p/k for p in piles)

for each of the piles (n), find minimum time it takes to finish that pile (logm)

for pile 1, it takes 1 hour 
for pile 2, it takes 4 hour

nlogm is confusing

i feel like mlogn makes sense ? 

find how long it takes for to get hrough the largest pile?

largest pile is 4

so let's say all piles are 4

[4,4,4,4]

that means 16

k = 2

4*2 = 8 hours

or len(piles) * 9 / k = 4

k = 16 / 9 rounded up = 2? 

search from 1, 4

oh because the most it needs to eat per hour is the biggest pile

duh

so from 1, 4

what are we searching from 1, 4? 

Hint 1: it takes koko ceil(x / k) or (-1 * (-x // k)) bc round to zero hours to eat a pile of 
Hint 2: Upper bound for k, is max(piles)
Hint 3: m = max(piles), or 4

i see

so we search from 1, 4 but that can happen for really big

so if we have a def canEatPiles(piles, k): and call that O(logn) times, thats better than doing it linearlly
'''

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatPiles(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += -1 * (-p // k) # ceil(p / k)
            return hours <= h

        # Pattern 2, because no exact target, want to find smallest
        l = 1
        r = max(piles) # can't be h because rate and hours is different
        while l < r:
            k = (l + r) // 2
            canEat = canEatPiles(k)
            # print(f"Before {l=}, {r=}, {k=}, {canEat=}")
            if canEat:
                # can eat but may not be mid. go left
                r = k # exclude r
            else:
                l = k + 1
            # print(f"After  {l=}, {r=}, {k=}, {canEat=}")
        # l greater than r at this point
        return l

        
        