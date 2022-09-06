# LIFO
#
# linkedlist
#
# last
# inserted is first
# deleted
#
# insert, pop, top -> head
# size, tail ->

class Node:
    def __init__(self, data):
        self.data = None
        self.next = None


class stack:
    def __init__(self, data):
        self.head = None
        self.size = 0

    def insert(self, data):
        temp = Node(data)
        temp.next = self.head
        head = temp
        self.size += 1

    def size(self):
        return self.size

    def top(self):
        if self.head == None:
            return None
        return self.head.data

    # top head 3->2->1
    def pop(self):
        if self.head == None:
            return None
        popdata = self.head.data
        temp = self.head.next
        self.head = temp
        self.size -= 1
        return popdata

st=stack()
st.insert(20)
st.insert(30)
st.top()
st.pop()

