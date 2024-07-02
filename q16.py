class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, node):
        if node is None:
            return None
        if node.next is None:
            self.head = node
            return node
        node1 = self.reverse(node.next)
        node1.next = node
        node.next = None
        return node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp


ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(85)

print("Given linked list:")
ll.print()

ll.reverse(ll.head)

print("\nReversed Linked list:")
ll.print()