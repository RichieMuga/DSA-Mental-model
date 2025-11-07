class Stack:
    def __init__(self):
        self.stack = []
    
    def append(self, element):
        self.stack.append(element)
        return self.stack
    
    def pop(self):
        if self.stack:
            self.stack.pop()
            return None

# example code
s = Stack()
print(s.append(1))
print(s.append(2))
print(s.pop())

print(s.stack)