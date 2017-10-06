class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        # stack push: append()
        # stack pop:  pop()


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)



    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        tmpStack = []
        while len(self.stack) > 0:
            tmpStack.append(self.stack.pop())
        ret = tmpStack.pop()
        while len(tmpStack) > 0:
            self.stack.append(tmpStack.pop())
        return ret


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        tmpStack = []
        while len(self.stack) > 0:
            tmpStack.append(self.stack.pop())
        ret = tmpStack[-1]
        while len(tmpStack) > 0:
            self.stack.append(tmpStack.pop())
        return ret



    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
