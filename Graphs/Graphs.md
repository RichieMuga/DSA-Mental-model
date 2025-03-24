# Graphs
- This is a datastructure that contains vertices and edges which are connected together to form a relationship.

## Types of graphs
    - ** Directed graph **: These contains one direction only
    - ** Undirected graph **: Contains bidirectional vertex and edge

## Different ways to represent graphs
- Consider the following graph image below:
    
    ![Graph example](../pictures/graph_example1.png)

1. #### Edge list
edge_list = [[0,1], [1,2], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]

2. #### Adjacency matrix
- The row represents to, while the column represents the from

- Consider the previosuly discussed graph at the beggining of the topic on ```Different ways to represent a graph```
    
    ![adjacency_matrix](../pictures/adjacency_matrix.png)

- As you can see we use 0's and 1's to represent whether a node was visited or not.

3. #### Adjacency list 
- This uses a hashmap in that the key represents the nodes value while the value is the list of all the connections it has

- The following below is the example of an adjacency list

                    ```
                    adjacency_list = {
                        0:[1,3],
                        1:[2],
                        2:[],
                        3:[7,6,4],
                        4:[2,5],
                        5:[2],
                        6:[],
                        7:[]
                    }
                    ```

- This is the most recommended way of usig graphs

4. #### Node class
- This is whereby one implements a node class with the values of self.value, as the value of the node and the self.neighbours as the adjacent nodes connected to it 

- Below is an example implementation of a node class in python:
```
                    class Node:
                        __init__(self, value Int, neighbours List):
                            self.value = value
                            self.neighbours = neighbours
```


## Graph transversal techniques
### Recursive DFS(Depth First Search)
- This algorithim prioritizes the deepest node within a graph

- Some of the requirements to implement a standard recursive dfs in graphs include
    1. Implementing a dfs
    2. Backtracking to the start of the dfs
    3. Having a seen set to keep track to which nodes have been visited

### Iteration DFS
- This is a dfs solution that uses a stack and for loop(s) to transverse the graph
- Some of the requirements to implement a standard iterative dfs in graphs include
    1. Implementing a dfs
    2. Adding and poping to the stack depending on which node we are on
    3. Having a seen set to keep track to which nodes have been visited

### Breadth First Search
- This is a dfs soltion whereby we transverse the nearest node first making sure we have exausted all shallow options then going deep ie. like a virus
    1. Implementing a bfs
    2. Adding and poping to the queue depending on which node we are on
    3. Having a seen set to keep track to which nodes have been visited


NB: The difference between trees and graphs is that trees contain a property known as a connected acyclick graph.

## General time and space complexity of graphs
- Time: o(v+e)
- Space: o(v+e)
