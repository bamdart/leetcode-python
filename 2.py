# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_list_from_node(list_node):
    result = []

    while 1:
        result.append(list_node.val)

        if list_node.next is None:
            return result

        list_node = list_node.next

def list_to_node(result_list):
    result = ListNode()
    now_node = result
    for i, num in enumerate(result_list):
        now_node.val = num
        if i != len(result_list) - 1:
            now_node.next = ListNode()
            now_node = now_node.next
    
    return result

class Solution(object):
    def addTwoNumbers(self, l1_node, l2_node):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1 = get_list_from_node(l1_node)
        l2 = get_list_from_node(l2_node)

        l1_len = len(l1)
        l2_len = len(l2)

        if l1_len > l2_len:
            l2 += [0] * (l1_len - l2_len)
        else:
            l1 += [0] * (l2_len - l1_len)

        result = []
        next_value = 0

        for i, num in enumerate(l1):
            add_result = num + l2[i] + next_value
            if add_result >= 10:
                next_value = add_result // 10
                add_result -= next_value * 10
            else:
                next_value = 0

            result.append(add_result)

        if next_value != 0:
            result.append(next_value)

        return list_to_node(result)