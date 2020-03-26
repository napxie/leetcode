# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre, end, pre.next, end.next = self, self, head, head
        while end:
            for i in range(k):
                if end is None:
                    break
                end = end.next
            if end is None:
                break
            start, _next, end.next = pre.next, end.next, None
            pre.next, start.next = self.reverse(start), _next
            end = pre = start
        return self.next
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

def createList():
    head = ListNode(0)
    cur = head
    for i in range(1, 5):
        cur.next = ListNode(i)
        cur = cur.next
    return head
            
def printList(head):
    cur = head
    while cur != None:
        print(cur.val, '-->', end='')
        cur = cur.next

    print('NULL')

if __name__ == "__main__":
    head = createList()
    printList(head)
    res = Solution().reverseKGroup(head, 2)
    printList(res)