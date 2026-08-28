from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if len(position) != len(speed):
            print("Mismatched inputs")

        fleet_stack = [] # stack to track times to hit target
        car_data = [] # list to track all data

        for i in range(len(position)):
            p = position[i]
            s = speed[i]
            # target = p + s*time
            # target - p = s*time
            time = (target - p) / s
            car_data.append([p,s,time])

        # Get the car that's furthest ahead first
        car_data.sort(key=lambda data:-1*data[0])

        # print(car_data)

        for p, s, t in car_data:
            # only added to stack if its not a fleet
            # fleet if one car is slower than the next
            if len(fleet_stack) > 0:
                # the slowest car got there in t_prev seconds
                # the next slowest car got there in t seconds
                t_prev = fleet_stack[-1]
                if t_prev >= t:
                    # print("[Prev is slower] Compared (prev,curr)", (t_prev, t))
                    # print(fleet_stack)
                    continue # if its slower, don't add and take the slower one as a fleet
                else:
                    # print("[Curr is slower]  Compared (prev,curr)", (t_prev, t))
                    fleet_stack.append(t)
            else:
                # print("Nothing on stack adding")
                fleet_stack.append(t)

            # print(fleet_stack)

        return len(fleet_stack)

    def checkSolution(self, target, position, speed, expected):
        print("====TESTING====")
        print("Checking input:", target, position, speed)
        actual = self.carFleet(target, position, speed)
        print("Expected: ", expected)
        print("Actual:   ", actual)
        print("Matches:  ", expected == actual)
        print("")