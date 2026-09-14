'''
minimum number of boats

[5,1,4,2], each boat can carry 6 weight

so boat 1 is 5 and 1, boat 2 is 4 and 2

sort it first

[1,2,4,5]

and then keep adding from heavy / lowest combo
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boats = 0

        lo = 0
        hi = len(people) - 1

        people = sorted(people)

        while lo <= hi:
            if lo != hi and people[lo] + people[hi] <= limit:
                # print(f"trying {lo=} {people[lo]=}, {hi=} {people[hi]=}, adding both")
                # Add both
                lo += 1
                hi -= 1
                boats += 1
                
            else:
                # print(f"trying {lo=} {people[lo]=}, {hi=} {people[hi]=}, adding heavy")
                # Add just one heavier
                boats += 1
                hi -= 1

        return boats

'''
[1,2,2,3,3]

[just add 3, just add 3, add 2/1, add 2] = 4
'''
            
        