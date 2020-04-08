func preorder(root *Node) []int {
    if root == nil {
        return []int{}
    }
    var ret []int
    ret = append(ret, root.Val)
    for _, v := range root.Children {
        ret = append(ret, preorder(v)...)
    }
    return ret
}