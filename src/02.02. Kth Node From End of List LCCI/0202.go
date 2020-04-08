/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func kthToLast(head *ListNode, k int) int {
    m := make(map[int]int)
    len := 0
    p := head
    for p != nil {
        len++
        m[len] = p.Val
        p = p.Next
    }
    index := len - k + 1
    return m[index]
}
