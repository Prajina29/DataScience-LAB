import heapq ### min-heap

heap = []
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)

print(heapq.heappop(heap))  # smallest element
print(heap)
