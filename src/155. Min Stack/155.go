type Node struct {
    data int
    next *Node
}

type Stack struct {
    head *Node
}

func NewStack() *Stack {
    return &Stack{
        head:&Node{},
    }
}

func (s *Stack) push(v int) {
    n := &Node{
        data: v,
        next: nil,
    }
    n.next = s.head.next
    s.head.next = n
}

func (s *Stack) pop() {
    s.head.next = s.head.next.next
}

func (s *Stack) isEmpty() bool {
    return s.head.next == nil
}

func (s *Stack) top() int {
    return s.head.next.data
}

type MinStack struct {
    dataStack *Stack
    minStack *Stack
}

/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{
        dataStack: NewStack(),
        minStack: NewStack(),
    }
}


func (m *MinStack) Push(x int)  {
    m.dataStack.push(x)
    if m.minStack.isEmpty() {
        m.minStack.push(x)
    } else {
        v := m.minStack.top()
        if x <= v {
            m.minStack.push(x)
        }
    }
}


func (m *MinStack) Pop()  {
    data := m.dataStack.top()
    m.dataStack.pop()
    min := m.minStack.top()
    if data == min {
        m.minStack.pop()
    }
}

func (m *MinStack) Top() int {
    return m.dataStack.top()
}


func (m *MinStack) GetMin() int {
    return m.minStack.top()
}