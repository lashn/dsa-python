class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

class LinkedList:
    head=Node(10)
    head.next=Node(20)

    print(head.key)
    print(head.next.key)


