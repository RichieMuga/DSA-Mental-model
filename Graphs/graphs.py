"""
Consider the following graph

0 --> 1 --> 2 <--
 \             / \ 
  \           /   \ 
   --> 3 --> 4 --> 5
      / \ 
     /   \ 
    7     6

   assume 4 is connected to 2
   assume 5 is connected to 2
   assume 3 is directly connected to 7
   assume 3 is directly connected to 6
"""

# array of edges [start, end]
A = [[0,1], [1,2], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]

# number of nodes / vertices
n = 8

## convert from edge list to adjacency matrix
m = []

for i in range(n):
    m.append([0]* n)

for u,v in A:
    m[u][v] = 1

print(m)
print("\n")
# Uncomment the following if the graph is undericted
# for u,v in A:
#     m[v][u] =1

# convert from edje list to adjacency list
from collections import defaultdict, deque

d = defaultdict(list)

for u,v in A:
    d[u].append(v)

print(d)
print("\n")



##################################################
# 
# Transversing an adjacency list
# 
##################################################

# DFS with recursion
def dfs_recursion(node):
    print(node)
    for neigbour_node in d[node]:
        if neigbour_node not in seen:
            seen.add(neigbour_node)
            dfs_recursion(neigbour_node)
# intialize where we start from
source = 0

# set of values we've seen
seen = set()

seen.add(source)

dfs_recursion(source)


# iterative dfs using stack
stack =[source]

while stack:
    node = stack.pop()
    print(node)
    for neighbour_node in d[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            stack.append(neighbour_node)

# bfs
from collections import deque

queue = deque()
seen = set()

queue.append(source)

while queue:
    node = queue.popleft()
    for neighbour in d[node]:
        if neighbour not in seen:
            seen.add(neighbour)
            queue.append(neighbour)

# class implementation
class Node:
    def __init__(self, value):
        self.value = value 
        self.neighbour = []
    
    def __str__(self):
        return f'Node({self.value})'

    def display(self):
        connections = [node.value for node in self.neighbour]
        return f'{self.value} is connected to {connections}'
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbour.append(B)
B.neighbour.append(A)
C.neighbour.append(A)
D.neighbour.append(A)

A.display()
