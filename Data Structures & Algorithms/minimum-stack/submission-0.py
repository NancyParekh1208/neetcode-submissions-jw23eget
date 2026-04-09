class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:

        
        self.stack.append(val)
        # calculate new min val
        val = min(val, self.minstack[-1] if self.minstack else val)
        
        self.minstack.append(val) # whichever is min gets added to stack
        

    def pop(self) -> None:

        self.stack.pop()
        self.minstack.pop() #since for every number added to main stack we have added prefix min to the extra stack, it will remove only that.
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
