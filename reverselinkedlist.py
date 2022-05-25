from linkedlist import LinkedList
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__== "__main__":
    node = Solution()
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_values([5,6,7,8])
    ll.insert_at(0,7)
    ll.insert_at(1,66)
    ll.insert_at(3,9)
    print(node.reverseList(ll))
