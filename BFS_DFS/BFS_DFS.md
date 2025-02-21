# Breadth First Search.
- This is an algorithim whereby, starting from the root as the first level; all the other child nodes are visited in level order from left to right until the intended child node is reached or all the nodes are visited.

## Prerquisites.
- One should have a basic understanding of the queue datastructure

## Advantages.
- Its easier to get the neighbouring nodes and output them.

## Disadvantages.
- More memory consumpion

## Importance of BFS/Real life use cases.
- Google maps naviagtion
- Friend suggestion in social media
- Zombie game, showing how an infection spreads level by level
- Finding the nearest free toilet

# Depth First Search(DFS).
- This is an algorithim whereby one searches the branch of a binary tree, upto the last node, and if the last node is reached the one checks the child's ansestor's unvisited child node and marks it as visited, this goes on until the intended node is reached or the all the nodes are visited.

## Prerequisites.
- Basic understanding of the stack datastructure

## Advantages.
- Deep level transversal is easier. ie. nodes at a deeper level are easier to reach

## Disadvantage.
- Not really suitable for finding neighbouring child nodes, would rather use BFS.

## Importance of DFS/Real world scenatios.
- Procatination. i.e getting into a rabbit hole.
- web crawling.
