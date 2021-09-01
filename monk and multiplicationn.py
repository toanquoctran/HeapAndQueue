def maxHeapify(a, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    n = len(a)
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a, largest, n)

def buildMaxHeap(a, n):
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(a, i, n)

def heapSort(a, n):
    heapSize = n
    buildMaxHeap(a, n)
    for i in range(n - 1, 1, -1):
        a[1], a[i] = a[i], a[1]
        heapSize -= 1
        maxHeapify(a, 1, heapSize)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n+1):
        heapSort(a, i)
        if i < 3:
            print(-1)
        else:
            res = a[i-1] * a[i-2] * a[i-3]
            print(res)