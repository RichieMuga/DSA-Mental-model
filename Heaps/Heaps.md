# Heaps/Priority queue
- Heaps or priority queues are a datastructure that are complete or nearly complete binary trees


## Importance of heaps
- Useful in garbage collector of languages such as java

## Types of heaps
     - min heap
     - max heap

**Min heap**: is a type of heap in that the lowest value has the highest priority hence is at the top of the tree for example
```
                                -10
                                /  \
                               /    \
                              /      \
                             /        \
                             3         4
                            / \       / \
                           /   \     /   \
                          /     \   /     \
                        10       6 9      14
```
**Max heap**: is a type of heap in that the hightst value has the highest priority hence is at the top of the tree
```
                                 23
                                /  \
                               /    \
                              /      \
                             /        \
                            15        13
                           / \        / \
                          /   \      /   \
                         /     \    /     \
                        10      6  9      14
```
- The action in which one sorts the elements that is not at its desired place is called heapify
- There are two types of heapify, namely:
    - min heapfiy: sorting elements in a heap in which one achieves a min heap
    - max heapify: sorting elements in a heap in which one achieves a max heap

NB: Tuples are use for way for "truly sorting a heap into a min heap or max heap"
