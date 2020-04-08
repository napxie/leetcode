/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reverseKGroup(head *ListNode, k int) *ListNode {

	h := ListNode{}
	l := &h
	s := 0
	for head != nil {
		l.Next = head
		s++
		l = l.Next
		head = head.Next
	}
	head = h.Next
	retHead := ListNode{}
	retList := &retHead
	for count := int(s / k); count != 0; count-- {
		h = ListNode{}
		l = &h
		for i := 0 ; i < k ; i++ {
			l.Next = head
			l = l.Next
			head = head.Next
		}
		l.Next = nil
		retList.Next = reserveLink(h.Next)
		for retList.Next != nil  {
			retList = retList.Next
		}
	}
	retList.Next = head
	return retHead.Next
}
func reserveLink(head *ListNode) *ListNode {
    var prev *ListNode
    for head  != nil {
        head.Next, prev, head = prev, head, head.Next
    }
    return prev
}

