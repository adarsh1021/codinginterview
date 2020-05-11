class Heap:
    def __init__(self, arr):
        print
        self.heap = self.build_heap(arr.copy())
        self.size = len(self.heap)

    def build_heap(self, arr):
        heap_size = len(arr)
        for i in range(heap_size//2, -1, -1):
            self.heapify(arr, heap_size, i)
        return arr

    def heapify(self, arr, heap_size, i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i

        if left < heap_size and arr[left] > arr[largest]:
            largest = left
        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, heap_size, largest)
    
    def sort(self):
        for i in range(self.size-1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify(self.heap, i, 0)
        return self.heap

h = Heap([2, 5, 12, 44, 1, 56, 19, 21, 10, 7, 3])
print(h.sort())

            