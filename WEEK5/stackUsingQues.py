#stack using queues
import collections
class MyStack:

    def __init__(self):
        self.queue = collections.deque()
        self.count=0

    def push(self, x):
        q = self.queue
        q.append(x)
        self.count+=1
        for i in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return not len(self.queue)
    def printstack(self):
        print(self.queue)


s1=MyStack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.printstack()
print("top",s1.top())
print("popped item",s1.pop())
s1.printstack()
