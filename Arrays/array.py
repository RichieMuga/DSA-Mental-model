# Objectives: create append, pop and sort in array class

class Array2:
    def __init__(self):
        self.data = []
        self.length = 0

    def append(self, val):
        self.data.append(val)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None  # or raise an error
        value = self.data.pop()
        self.length -= 1
        return value

    def sort(self):
        self.data.sort()  # uses Python’s built-in Timsort
        # length stays the same



# Prerequisites:
# 1. Prexisting array
#    - create appendings of 3 elements first then perform the other operations

arrayOperations = Array2()

print(arrayOperations.data)
arrayOperations.append(3)
arrayOperations.append(2)
arrayOperations.append(1)
print(arrayOperations.data)

arrayOperations.pop()
arrayOperations.sort()

print(arrayOperations.data)