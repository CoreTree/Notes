class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        if self.next is None:
            return f"<ListNode(val={self.val})>"
        return f"<ListNode(val={self.val},next={self.next})>"

class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

sol = Solution()
listnode_a = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3))))
print("Input:", listnode_a)
sol.reorderList(listnode_a)
print("Output:", listnode_a)