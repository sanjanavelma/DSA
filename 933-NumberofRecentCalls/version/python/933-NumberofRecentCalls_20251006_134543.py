# Last updated: 06/10/2025, 13:45:43
class RecentCounter:

    def __init__(self):
        self.queue = deque([])
        

    def ping(self, t: int) -> int:
        previous = t - 3000
        while self.queue and self.queue[0]<previous:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)