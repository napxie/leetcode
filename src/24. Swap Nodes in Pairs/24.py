class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head
        # Nodes to be swapped
        first_node = head
        second_node = head.next
        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        # Now the head is the second node
        return second_node

    def swapPairs1(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


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
    nums = [1, 2, 3, 4]
    printList(Solution().swapPairs(createList(nums)))
    printList(Solution().swapPairs1(createList(nums)))
