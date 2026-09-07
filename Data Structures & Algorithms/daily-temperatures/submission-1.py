'''
monostack maintain that the stuff in the stack always is becoming cooler (less hot)
and so once we come across something hotter, we can say that's the next day it's hotter
(left to right)

stack = []
temp  = [30,38,30,36,35,40,28], for i = 0 -> 30
res   = [0, 0, 0, 0, 0, 0, 0 ]

stack = [(30,day=0)]
temp  = [30,38,30,36,35,40,28], for i = 1 -> 38
res   = [1, 0, 0, 0, 0, 0, 0 ]
it's greater so pop 30 off, day1-day0, set 30 to 1

stack = [(38,day=1)]
temp  = [30,38,30,36,35,40,28], for i = 2 -> 30
res   = [1, 0, 0, 0, 0, 0, 0 ]
not greater, add it to the stack

stack = [(38,day=1),(30,day=2)]
temp  = [30,38,30,36,35,40,28], for i = 3 -> 36
res   = [1, 0, 0, 0, 0, 0, 0 ]
36 is greater, so pop 30 off, 1 day difference then add it

stack = [(38,day=1),(36,day=3)]
temp  = [30,38,30,36,35,40,28], for i = 4 -> 35
res   = [1, 0, 1, 0, 0, 0, 0 ]
not greater, add it

stack = [(38,day=1),(36,day=3),(35,day=4)]
temp  = [30,38,30,36,35,40,28], for i = 5 -> 40
res   = [1, 4, 1, 2, 1, 0, 0 ]
greater than everything, empty the full stack and compute the diff
35 becomes a 1 day diff, 36 a 2 day diff, 38 a 4 day diff

stack = [(40,day=5)]
temp  = [30,38,30,36,35,40,28], for i = 6 -> 28
res   = [1, 4, 1, 2, 1, 0, 0 ]
not greater, we have our answer
'''

class MyTemp:
    temp: int
    day: int
    
    def __init__(self, temp=-1, day=-1):
        self.temp = temp
        self.day = day

    def __repr__(self):
        temp = self.temp
        day = self.day
        return f"MyTemp({temp=}, {day=})"


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mytemps = [MyTemp(temp=t, day=i) for i, t in enumerate(temperatures)]
        stack = []
        res = [0] * len(temperatures)
        for mt in mytemps:
            # Base Case
            if len(stack) == 0:
                stack.append(mt)
                # print(f"bc {stack=}")
            # Is Hotter
            while len(stack) > 0 and mt.temp > stack[-1].temp:
                # Get the previous day, compute the diff, set it in result
                prev_mt = stack.pop()
                day_difference = mt.day - prev_mt.day
                res[prev_mt.day] = day_difference
                # print(f"wl {stack=}")
                # print(f"   comparing {mt=} and {prev_mt=}")
                # print(f"   {res=}")
            # Add next one
            stack.append(mt)
        return res                
                
        
        