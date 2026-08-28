
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def myPrint(*args):
            if False:
                print(*args)

        lo = 0
        hi = max(piles)
        max_time = hi

        def getEatingTime(k):

            if k == 0:
                myPrint("eating time", h + 1)
                return h + 1

            k_num = max(k - 1, 0)
            k_den = max(k, 1)
            time = sum([(p+k_num)//k_den for p in piles])
            myPrint("eating time", time)
            return time

        lo = 0
        hi = max(piles)

        k = hi

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            myPrint("considering k=", mid)
            time = getEatingTime(mid)
            if time <= h:
                k = min(k, mid)
                myPrint("storing lowest valid k as", k)
                myPrint("i can take more time, i want to eat slower")
                hi = mid - 1
            else:
                myPrint("ate too slow got caught, speed up")
                lo = mid + 1

        if getEatingTime(mid) <= h:
            return min(mid, k)

        return k