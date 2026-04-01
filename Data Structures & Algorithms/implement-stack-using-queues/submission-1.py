class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class MyStack:

    def __init__(self):
        self.right = ListNode(0)
        self.left = ListNode(0)
        self.right.prev = self.left
        self.left.next = self.right
        

    def push(self, x: int) -> None:
        
        node, next, prev = ListNode(x), self.right, self.right.prev
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev
        

    def pop(self) -> int:
        
        node, next, prev = self.right.prev, self.right, self.right.prev.prev
        next.prev = prev
        prev.next = next
        return node.val
        

    def top(self) -> int:
        return self.right.prev.val
        

    def empty(self) -> bool:
        if self.left.next == self.right:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()