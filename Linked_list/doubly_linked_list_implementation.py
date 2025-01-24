class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        

    # add to the end of the list
    def append(self, data):
        newNode = Node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next

        # after we find the final node
        cur.next = newNode

        # point the prev pointer to the last node
        newNode.prev = cur

    # add to the beggining of the list
    def prepend(self, data):
        newNode = Node(data)

        # update the next node in the newNode to be the following predecessing nodes
        newNode.next = self.head.next
        # update the next node in the dummy head to the newNode
        self.head.next = newNode

        # If the list is not empty, update the prev pointer of the current first node
        if self.head.next is not None:
            self.head.next.prev = newNode

        # point the prev pointer to the dummy head node
        newNode.prev = self.head

    # inser node at any point of the list
    def insert(self, index, value):
        newNode = Node(value)

        # set current node to equal dummy head node
        curr = self.head

        # while the index does not react zero
        while index != 0:
            if curr.next != None:
                curr = curr.next
                index -= 1
            else:
                return

        # when reached desired index change the curr.next node to point to the new node
        newNode.next = curr.next

        # make sure the newNode.next.prev points to the newNode
        newNode.next.prev = newNode

        # and then make sure the previous node points to the current node
        curr.next = newNode

        # and make sure the newNode.prev points to the curr
        newNode.prev = curr

    # delete node at any point of the list
    def deletion(self, index):
        if index == 0:
            self.head = self.head.next if self.head else None
            return

        index = index - 1
        before_curr = self.head

        # index of the node we want to delete
        while index != 0:
            if before_curr.next != None:
                before_curr = before_curr.next
                index -= 1

        # make the next pointer skip the curr node and point to the next
        before_curr.next = before_curr.next.next

        # maje the prev pointer point to the before cur
        before_curr.next.prev = before_curr


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.prepend(4)
dll.append(3)
dll.insert(1, 9)
dll.deletion(3)

cur = sll.head.next
while cur != None:
    print(cur.data)
    cur = cur.next
