class Node: 
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self,val):
        self.root = Node(val)
        self.stack = []
        self.stack.append(self.root.val)

    # insert a new node
    def insert(self,val):
        if val is None:
            return
        newNode = Node(val)
        curr = self.root
        ancestors = []

        while True:
            ancestors.append(curr.val)
            if val < curr.val:
                if curr.left is None:
                    curr.left = newNode
                    break
                else: 
                    curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    curr.right = newNode
                    break
                else:
                    curr = curr.right
            else:
                print("node already exists in bst")

        self.stack.append(val)
        print(f"Inserted {val}, Queue: {self.stack}")

    def remove(self, key, root):
        # remove node in bst
        # 3 cases, i have to handle
        # 1. if node has no children, ie. no left or right nodes = return None
        # 2. if node has one child = point the prev level to the next level after
        # 3. if node has two children = find the most min val and the recursively change the right node value
        if root == None:
            return None

        if key > root.val:
            root.right = self.remove(key, root.right)
        elif key < root.val:
            root.left = self.remove(key, root.left)
        else:
            if not root.left:
                return root.left
            elif not root.right:
                return root.right
            # find the min from the right subtree
            curr = root.right

            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.remove(root.right, curr.val)

        return root
        
    #BFS
    def bfs(self):
        curr = self.root
        queue = []
        list = []

        queue.append(curr)

        while len(queue) > 0:
            curr = queue[0]
            list.append(curr.val)
            queue.pop(0)


            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return list



    # DFS recursive
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=" ")
            self.inorder_traversal(node.right)

    # DFS iterative
    def dfsI(self):
        if not self.root:
            return
        stack = [self.root]

        while stack:
            node = stack.pop()

            print(node.val, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


# instanciate the binary search tree
binarySearch = BinarySearchTree(24)

# insert into the left or right node of the bst in the root or in the ancestor
binarySearch.insert(9)

binarySearch.insert(8)

binarySearch.insert(22)

binarySearch.insert(31)

binarySearch.insert(33)

binarySearch.insert(30)

print("BST Inorder Traversal:")
binarySearch.inorder_traversal(binarySearch.root)


print("\nBFS Traversal:")
print(binarySearch.bfs())

print("\n REMOVE NODE IN BST")
binarySearch.remove(8,binarySearch.root)
binarySearch.inorder_traversal(binarySearch.root)
print("\nMUSTARD")
binarySearch.dfsI()

# BinarySearch tree, has two nodes, namely left and right
# we add a node either to the left or the right
# after we instanciate the BST, we add a node that has an empty right and left node
# when we insert, we inster first on the left and then on the right if the left is present
# edge cases is if the value provided is None, then we return an empty Node

# remove, just pass the position of the Node in the stack
