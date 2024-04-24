
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        prev_node = root
        temp_node_list = []

        first = True
        while 1:
            if head is None:
                break

            if head.next is None:
                break

            temp_node_list = []
            temp_node_list.append(head)
            temp_node_list.append(head.next)

            temp_node_list[0].next = temp_node_list[1].next
            temp_node_list[1].next = temp_node_list[0]

            if first:
                root = temp_node_list[1]
                first = False
            else:
                prev_node.next = temp_node_list[1]

            prev_node = temp_node_list[0]

            head = temp_node_list[0].next

        return root