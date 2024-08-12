class MinStack:

    def __init__(self):
        self.s=[]
        self.mini=[]

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.mini)==0:
            self.mini.append(val)
        elif(self.mini[-1]<val):
            self.mini.append(self.mini[-1])
        else:
            self.mini.append(val)
    def pop(self) -> None:
        self.mini.pop()
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()