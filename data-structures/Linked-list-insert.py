#!/usr/bin/python
"""
https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list
"""

"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def insert_to_existing(head, data):
    original_head = head
    while head.next is not None:
        head = head.next
    head.next = Node(data)
    return original_head


def Insert(head, data):
    if head is None:
        return Node(data)
    return insert_to_existing(head, data)
