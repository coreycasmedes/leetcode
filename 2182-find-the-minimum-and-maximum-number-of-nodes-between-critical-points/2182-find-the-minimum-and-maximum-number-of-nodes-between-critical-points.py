# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        maximas = []
        length = 1
        prev = head.val
        current = head.next

        while current:
            if current.next:
                if current.val < prev and current.val < current.next.val:
                    # local min
                    maximas.append(length)
                if current.val > prev and current.val > current.next.val:
                    maximas.append(length)
                length += 1
                prev = current.val
                current = current.next
                
            else:
                break

        # FIND MIN
        if len(maximas) <= 1:
            return [-1,-1]

        minim = 2 ** 31
        for i in range(len(maximas)-1):
            if maximas[i+1] - maximas[i] < minim:
                minim = maximas[i+1] - maximas[i]
        return [minim, maximas[-1] - maximas[0]]




        