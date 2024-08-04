from collections import OrderedDict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        hashmap = OrderedDict()
        prefix_sum = 0

        current = dummy

        while current:

            prefix_sum += current.val
            first = hashmap.get(prefix_sum, current)
            while prefix_sum in hashmap:
                hashmap.popitem()
            hashmap[prefix_sum] = first
            first.next = current = current.next
        return dummy.next
