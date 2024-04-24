
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        temp_node = head

        while 1:
            node_list.append(temp_node)
            if temp_node.next is None:
                break

            temp_node = temp_node.next

        if len(node_list) == 1:
            return None

        if len(node_list) == n:
            return head.next

        node_list[-(n + 1)].next = node_list[-n].next

        return head