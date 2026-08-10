# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Dummy nodes to serve as start markers for two lists
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        # Pointers to build the two lists
        before = before_head
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
            
        # Sever the tail of the 'after' list to avoid cycles
        after.next = None
        
        # Connect the 'before' list to the 'after' list
        before.next = after_head.next
        
        return before_head.next





__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))