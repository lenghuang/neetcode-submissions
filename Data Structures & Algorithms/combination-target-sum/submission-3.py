'''
nums = [2,5,6,9]
target = 9

every number can either be included, or not

checkSum([], 0) = True
checkSum([], t) = False
checkSum([x], t) = checkSum([], t - x)

example

checkSum([2,5,6,9], 9) 
-> do we include 2 or not? try both
-> checkSum([5,6,9], 7) or checkSum([5,6,9], 9)

but you can choose something any numver of times?

looks like numbers are small

and for a number k and a number t i can try it at most t / k times

so just try all versions

checkSum(head::tail, t) = 
    don't include           checkSum(tail, t)
    try to include once     checkSum(tail, t - head)
    try to include twice    checkSum(tail, t - 2 * head)
    ...
    try to include t // head times
'''

class Solution:
    
    def recurse(self, nums: List[int], acc: List[int], t: int) -> List[List[int]]:
        # print("recurse -- nums=", nums, "t=", t, "acc=", acc)
        if t == 0 and len(acc) > 0:
            # print("NUMS IS 0 -- appending :)")
            return [acc]
        elif len(nums) == 0:
            # print("NUMS IS 0 -- returning :(")
            return []

        head, tail = nums[0], nums[1::]
        # print("recurse -- head", head, "tail", tail)
        total_res = []
        for k in range((t // head) + 1):
            new_num = head * k
            new_acc = acc + [head for _ in range(k)]
            # print("recurse -- loop -- k", k, "new_num", new_num, "new_acc", new_acc)
            res = self.recurse(tail, new_acc, t - new_num)
            if len(res) > 0:
                total_res += res
        
        return total_res
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.recurse(nums, [], target)
    