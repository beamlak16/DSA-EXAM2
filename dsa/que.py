class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value

    def front(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def rear(self):
        if self.rear == -1:
            print("Queue is empty")
            return None
        return self.queue[self.rear]

    def is_empty(self):
        return self.front == -1

