import heapq

class SeverityHeap:
    def __init__(self):
        self.heap = []

    def add_complaint(self, complaint):
        heapq.heappush(self.heap, (-complaint.severity, complaint))

    def get_highest_severity(self):
        if not self.heap:
            return None
        return self.heap[0][1]

    def pop_highest_severity(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[1]

    def display_heap(self):
        for sev, comp in self.heap:
            print(comp)
