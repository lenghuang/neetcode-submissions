from collections import deque

class Queue:
    
    def __init__(self):
        self.q = deque()
    
    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]
    
    def empty(self) -> bool:
        return len(self.q) == 0

    def size(self) -> int:
        return len(self.q)

    def to_str(self):
        return str(self.q)

class MyStack:

    q: Queue

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        '''
        q1 = [1,2,3]
        q2 = []
        
        add 4 to the end

        q1 = [4]
        q2 = [3,2,1]
        
        then

        q1 = [1,2,3,4]
        q2 = [1,2,3]

        since 4 was the "first" one in on empty, its the first one out
        and we can rotate to q2 and maintain the same order, since it would go 3, 

        can just do with one q?

        q = [1,2,3] add 4 to left
        q = [4,1,2,3] then bring it to front (pop 3)
        q = [3,4,1,2] pop 2
        q = [2,3,4,1] pop 1
        q = [1,2,3,4] do it three times (len - 1)
        '''
        print('before', self.q.to_str())
        self.q.push(x)
        for _ in range(self.q.size() - 1):
            temp = self.q.pop()
            self.q.push(temp)
        print('after', self.q.to_str())
    
    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q.top()

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()