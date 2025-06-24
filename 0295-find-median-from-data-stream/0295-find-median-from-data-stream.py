import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []  # max heap (left half, as negative numbers)
        self.minHeap = []  # min heap (right half)

    def addNum(self, num: int) -> None:
        # Always add to maxHeap first (as negative)
        heapq.heappush(self.maxHeap, -num)
        # Move largest of maxHeap to minHeap
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        # Balance: if minHeap has more elements, move smallest back to maxHeap
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()