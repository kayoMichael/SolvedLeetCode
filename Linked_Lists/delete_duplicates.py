from linked_list import Node
"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the 
linked list sorted as well.

"""


def delete_duplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


def liked_list_has_loop(head, head_2):
    pointer_1 = head
    pointer_2 = head_2
    while pointer_1 is not pointer_2:
        pointer_1 = head_2 if not pointer_1 else pointer_1.next
        pointer_2 = head if not pointer_2 else pointer_2.next

    return pointer_1
