class StockSpanner:

    def __init__(self):
        self.mono = []
        self.prices = []
        self.day = 0
        

    def next(self, price: int) -> int:
        '''
        want the days previous for which the stock is less than or equal to 
        so this is a right to left monotonically increasing queue
        and if something is less or equal, pop it
        but we're building it as we go
        so each new price we get is something from the right
        so each next is like our loop body
        '''
        self.prices.append(price)
        # print(f"next called with {price=}")
        # print(f"{self.day=}\n{self.prices=}\n{self.mono=}")

        prev_day = 0
        while len(self.mono) > 0 and price >= self.prices[self.mono[-1]]:
            # print(f"while loop, peeked at {self.mono[-1]=} with price {self.prices[self.mono[-1]]}")
            self.mono.pop()
        
        if len(self.mono) == 0:
            res = self.day + 1
        else:
            res = self.day - self.mono[-1]

        self.mono.append(self.day)
        self.day += 1

        # print(f"returning {res=}\n")
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)