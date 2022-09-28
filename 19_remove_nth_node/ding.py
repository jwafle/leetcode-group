# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """naive solution:
        # pass one to get length
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next
        target = length - n
                
        # pass two to remove node
        if target == 0:
            head = head.next
            return head
        counter = 1
        curr = head
        while counter < target:
            counter += 1
            curr = curr.next
        temp = curr.next
        if temp:
            if temp.next:
                tail = temp.next
                curr.next = tail
                temp = None
            else:
                curr.next = None
        else:
            return None
        
        return head
        """

        # Two Pointer Solution
        fast = head
        slow = head
    
        # shift fast pointer forward n spaces
        # since n <= size this won't break
        for _ in range(n):
            fast = fast.next

        # if fast pointer is None then n == size
        # since shifted all the way to the end of linked list
        if not fast:
            return head.next

        # move both pointers until fast is on the last node
        # slow pointer will be right before node to remove
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head