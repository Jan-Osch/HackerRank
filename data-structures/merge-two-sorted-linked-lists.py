#!/usr/bin/python
"""
https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists
"""

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def is_first_head_smaller(headA, headB):
    if headA.data < headB.data:
        return True
    return False


def choose_new_head_when_one_is_empty(headA, headB):
    if headA is None:
        return headB
    return headA


def either_head_is_empty(headA, headB):
    if headA is None or headB is None:
        return True
    return False


def MergeLists(headA, headB):
    if either_head_is_empty(headA, headB):
        return choose_new_head_when_one_is_empty(headA, headB)
    if is_first_head_smaller(headA, headB):
        new_head = headA
        new_head.next = MergeLists(headA.next, headB)
    else:
        new_head = headB
        new_head.next = MergeLists(headA, headB.next)
    return new_head


def stringify_list(head):
    if head is None:
        return ''
    if head.next is None:
        return str(head.data)
    return str(head.data) + ' -> ' + stringify_list(head.next)


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


def construct_list(array_of_values):
    current = None
    for value in array_of_values:
        current = Insert(current, value)
    return current
