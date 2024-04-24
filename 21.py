from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = {}

        while list1:
            if list1.val not in result:
                result[list1.val] = 1
            else:
                result[list1.val] += 1
            list1 = list1.next

        while list2:
            if list2.val not in result:
                result[list2.val] = 1
            else:
                result[list2.val] += 1
            list2 = list2.next

        if len(result) == 0:
            return None

        keys = sorted(list(result.keys()))

        root = None
        now_node = root
        for key in keys:
            for count in range(result[key]):
                new_node = ListNode(key)
                if root is None:
                    root = new_node
                    now_node = root
                    continue

                now_node.next = new_node
                now_node = now_node.next

        return root