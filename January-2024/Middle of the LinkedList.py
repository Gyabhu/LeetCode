"""
    Given the head of a singly linked list,
    return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.
"""

class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        print("Node Inserted Sucessfully")

    def SLinkedList(self, head):
        result = []
        fast = slow = head
        print(fast.dataval)
        while fast and fast.next:
            slow = slow.next
            result.append(slow)
            fast = fast.next.next

        return result

    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.dataval)
            current_node = current_node.next

llist = LinkedList()

node1 = llist.insert(1)
node2 = llist.insert(2)
node3 = llist.insert(3)
node4 = llist.insert(4)
node5 = llist.insert(5)

print("Sorted LinkedList")
print(llist.SLinkedList(llist))
llist.printLL()