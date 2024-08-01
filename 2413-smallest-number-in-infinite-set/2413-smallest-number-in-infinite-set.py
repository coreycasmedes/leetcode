import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.heap = []
        self.heap_set = set()
        

    def popSmallest(self) -> int:
        if len(self.heap) > 0:
            smallest = heapq.heappop(self.heap)
            self.heap_set.remove(smallest)
        else:
            smallest = self.smallest
            self.smallest += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.smallest:
            if num in self.heap_set:
                pass
            else:
                self.heap_set.add(num)
                heapq.heappush(self.heap, num)

        
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)