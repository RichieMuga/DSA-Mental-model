class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = Node()

# add to the end of the list
    def append(self,data):
        newNode = Node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next

        # after we find the final node
        cur.next = newNode

# add to the beggining of the list
    def prepend(self,data):
        newNode = Node(data)
        
        # update the next node in the newNode to be the following predecessing nodes
        newNode.next = self.head.next
        # update the next node in the dummy head to the newNode
        self.head.next = newNode

# inser node at any point of the list
    def insert(self,index,value):
        newNode = Node(value)

        # set current node to equal dummy head node
        curr = self.head

        # while the index does not react zero
        while index != 0:
            if curr.next != None:
                curr = curr.next
                index-=1
            else:
                return

        # when reached desired index change the curr.next node to point to the new node
        newNode.next = curr.next

        # and then make sure the previous node points to the current node
        curr.next = newNode


# delete node at any point of the list
    def deletion(self, index):
        if index == 0:
            self.head = self.head.next if self.head else None
            return

        index = index -1
        before_curr = self.head

        # index of the curr value
        while index != 0:
            if before_curr.next != None:
                before_curr = before_curr.next
                index-=1

        before_curr.next = before_curr.next.next


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.prepend(4)
sll.append(3)
sll.insert(1,9)
sll.deletion(3)

cur = sll.head.next
while cur != None:
    print(cur.data)
    cur = cur.next

