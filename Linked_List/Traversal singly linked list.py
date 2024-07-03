# Traversal of linked list
class Node:
    def __init__(self, data):
        self.data = data  # n1.data = 5, n2.data = 10, n3.data = 15, n4.data = 20
        self.next = None  # n1.next = None, n2.next = None, n3.next = None, n4.next = None


class Sll:
    def __init__(self):
        self.head = None  # sll.head = None

    def traversal(self):
        if self.head is None:
            print("Singly linked list is empty.")
        else:
            a = self.head  # a = sll.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next

    def insert_at_beginning(self, data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_at_end(self, data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

    def insert_at_specified_node(self, position, data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(1, position - 1):
            a = a.next
        nib.next = a.next
        a.next = nib

    def deletion_at_beginning(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None

    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    def deletion_at_particular_node(self, position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1, position - 1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None


n1 = Node(5)
sll = Sll()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4
sll.traversal()
sll.insert_at_beginning(2)
sll.traversal()
sll.insert_at_end(25)
sll.traversal()
sll.insert_at_specified_node(3, 7)
sll.traversal()
sll.deletion_at_beginning()
sll.traversal()
sll.deletion_at_end()
sll.traversal()
sll.deletion_at_particular_node(3)
sll.traversal()


