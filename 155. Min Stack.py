class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(val, self.min[-1] if self.min else val))
		
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min[-1]
    
    
    
#     def __init__(self):
#         self.stack = []
#         self.min = None
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if self.min is None:
#             self.min = val 
#         self.min = val if val < self.min else self.min
		
#     def pop(self) -> None:
#         self.stack.pop()
#         if self.stack:
#             self.min = self.stack[-1]
#         else:
#             self.min = None
#         for i in self.stack:
#             self.min = i if i < self.min else self.min
    
#     def top(self) -> int:
#         return self.stack[-1]
        
#     def getMin(self) -> int:
#         # return min(self.stack) # too slow O(nlogn) not O(n)
#         return self.min