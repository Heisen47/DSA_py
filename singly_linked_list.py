class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<node data %s>" % self.data


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.__count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None

    def __len__(self):

        return self.__count

    def add(self, data):
        """
        Adds new Node containing data to head of the list
        Also called prepend
        Takes O(1) time
        """
        new_head = Node (data, next_node=self.head)
        self.head = new_head
        self.__count += 1

