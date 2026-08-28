class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prev_colder_days = []
        res = [0 for _ in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            # if today is most recent warmer day, check how many days its been for the previous colder days
            # while the top of the stack is colder, keep popping it off and setting it
            while prev_colder_days and prev_colder_days[-1][1] < t:
                # print("[algo] last day is warmer", prev_colder_days[-1][1], "<", t)
                # print("[algo] stack1", prev_colder_days)
                [i_prev, t_prev] = prev_colder_days.pop()
                # populate that
                res[i_prev] = i - i_prev

            # else, just added iti
            prev_colder_days.append([i, t])
            # print("[algo] stack2", prev_colder_days)

        return res