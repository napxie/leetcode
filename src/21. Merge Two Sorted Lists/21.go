func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    prehead := &ListNode{}
    prev := prehead

    for {
        if l1 == nil {
            prev.Next = l2
            break
        }
        
         if l2 == nil {
            prev.Next = l1
             break
        }
        
        if l1.Val > l2.Val {
            prev.Next = l2
            l2 = l2.Next
        } else {
            prev.Next = l1
            l1 = l1.Next
        }
        
        prev = prev.Next
    }
    
    return prehead.Next
}