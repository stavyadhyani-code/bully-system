from collections import deque

class ComplaintQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, complaint):
        self.queue.append(complaint)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display_queue(self):
        for c in self.queue:
            print(c)
