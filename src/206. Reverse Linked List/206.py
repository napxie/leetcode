class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def reverseList1(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur


def createList(nums):
    head = ListNode(0)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head


def printList(head):
    cur = head
    while cur != None:
        print(cur.val, '->', end='')
        cur = cur.next
    print('NULL')


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    printList(Solution().reverseList(createList(nums)))
    printList(Solution().reverseList1(createList(nums)))
