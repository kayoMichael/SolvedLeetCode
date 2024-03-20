"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104

"""


# Time Complexity: O(N + M)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_in_between(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    current = list1
    last = list1
    index = a - 1
    for i in range(0, a - 1):
        current = current.next

    for i in range(0, b + 1):
        last = last.next

    current.next = list2

    while current.next is not None:
        current = current.next

    current.next = last

    return list1
