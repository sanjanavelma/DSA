# Last updated: 07/07/2025, 21:48:42
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_day = min(event[0] for event in events)
        max_day = max(event[1] for event in events)

        heap = []
        res = 0
        i = 0
        n = len(events)

        for day in range(min_day, max_day + 1):
            while i < n and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                res += 1

        return res

            