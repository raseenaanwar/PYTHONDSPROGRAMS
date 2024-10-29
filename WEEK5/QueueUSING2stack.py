class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            # Transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()

    def front(self):
        if not self.stack2:
            # Transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]

    def isEmpty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.front())  # Output: 10

queue.dequeue()
print(queue.front())  # Output: 20

print(queue.isEmpty())  # Output: False

queue.dequeue()
queue.dequeue()

print(queue.isEmpty())  # Output: True
