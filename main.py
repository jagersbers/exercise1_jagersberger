# singly linked list
# node class of the singly linked list


class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        node = SLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = node
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    """
    Exercise part 1,2,3,4

    Implement the given methods below according to the requirements in the exercise sheet.
    Make sure to return the correct values.
    """

    def insert_node(self, prev_data, data):
        node = SLLNode(data)
        current = self.head
        while current is not None:
            if current.data == prev_data:
                node.next = current.next
                current.next = node
                self.size += 1
                return
            current = current.next
        return False

    def clear(self):
        self.head = None
        self.size = 0

    def get_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.data
            current = current.next
        return False

    def delete_node(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next


"""
Exercise part 5
Implement a doubly linked list according to the exercise sheet.
You can copy the code from the singly linked list and modify it.
"""


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the DLLNode class
        node = DLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head and tail
            self.head = node
            self.tail = node
        else:  # if it is not empty, we add the new node to the tail of the list
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        # Increase the size of the list
        self.size += 1

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def insert_node(self, prev_data, data):
        node = DLLNode(data)
        current = self.head
        while current is not None:
            if current.data == prev_data:
                node.next = current.next
                node.prev = current
                current.next = node
                if node.next is not None:
                    node.next.prev = node
                else:
                    self.tail = node
                self.size += 1
                return
            current = current.next
        return False

    def delete_node(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return

        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return


"""
Exercise Part 5 and 7:
Complete the classes below to implement a stack and queue data structure. You are free to use built-in
methods but you have to complete all methods below. Always return the correct data type according
to the exercise sheet
"""


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        return

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)
        return

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def show_left(self):
        if len(self.queue) > 0:
            return self.queue[-1]

    def show_right(self):
        if len(self.queue) > 0:
            return self.queue[0]

    def size(self):
        return len(self.queue)
