# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: 
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        temp=slow.next
        prev=None
        while temp:
            curr=temp.next
            temp.next=prev
            prev=temp
            temp=curr
        right=prev
        left=head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        
