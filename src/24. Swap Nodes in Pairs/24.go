/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	result := head.Next
	head.Next = swapPairs(head.Next.Next)
	result.Next = head
	return result
}

 func swapPairs(head *ListNode) *ListNode {
    prev := new(ListNode)
    prev.Next = head
    t := prev
    for prev.Next != nil && prev.Next.Next != nil {
        cur := prev.Next
        ne  := cur.Next
        prev.Next,ne.Next,cur.Next = ne,cur,ne.Next
        prev = cur
    }
    return t.Next
}