class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Dll:
    def __init__(self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print("Doubly linked list is empty.")
        else:
            a = self.head  # a = sll.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next

    def backward_traversal(self):
        print()
        if self.head is None:
            print("Doubly linked list is empty.")
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            while a is not None:
                print(a.data, end=" ")
                a = a.prev

    def insertion_at_beginning(self, data):
        print()
        ns = Node(data)
        a = self.head
        a.prev = ns
        ns.next = a
        self.head = ns

    def insertion_at_end(self, data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        ne.prev = a

    def insertion_at_specified_node(self, position, data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(1, position - 1):
            a = a.next
        nib.prev = a
        nib.next = a.next
        a.next.prev = nib
        a.next = nib

    def deletion_at_beginning(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None
        self.head.prev = None

    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
        a.prev = None

    def deletion_at_particular_node(self, position):
        print()
        a = self.head.next
        b = self.head
        for i in range(1, position - 1):
            a = a.next
            b = b.next
        b.next = a.next
        a.next.prev = b
        a.next = None
        a.prev = None


n1 = Node(5)
dll = Dll()
dll.head = n1
n2 = Node(10)
n2.prev = n1
n1.next = n2
n3 = Node(15)
n3.prev = n2
n2.next = n3
n4 = Node(20)
n4.prev = n3
n3.next = n4
dll.forward_traversal()
dll.backward_traversal()
dll.insertion_at_beginning(2)
dll.forward_traversal()
dll.backward_traversal()
dll.insertion_at_end(25)
dll.forward_traversal()
dll.insertion_at_specified_node(3, 7)
dll.forward_traversal()
dll.deletion_at_beginning()
dll.forward_traversal()
dll.backward_traversal()
dll.deletion_at_end()
dll.forward_traversal()
dll.backward_traversal()
dll.deletion_at_particular_node(3)
dll.forward_traversal()
dll.backward_traversal()
