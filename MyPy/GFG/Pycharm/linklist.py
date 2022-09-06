class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def printList(head):
    curr = head
    while curr!= None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)
# printList(head)

import copy

import copy


def insertlist(head, x):
    curr = copy.deepcopy(head)
    head.key = x
    head.next = curr
    return head


x = 50
print(insertlist(head, x))
printList(head)

def insertend(head, x):
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(x)
    # head = curr
    return head


key = 60
head = insertend(head, key)
printList(head)
