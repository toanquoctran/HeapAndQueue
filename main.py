def maxHeapify(i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(a) and a[left] > a[largest]:
        largest = left
    if right < len(a) and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(largest)

def buildMaxHeap(n):
    for i in range(n//2 -1, -1, -1):
        maxHeapify(i)

def top():
    return a[0]

def push(value):
    a.append(value)
    i = len(a) - 1
    while i != 0 and a[(i - 1) // 2] > a[i]:
        a[i], a[(i - 1) // 2] = a[(i - 1) // 2], a[i]
        i = (i - 1) // 2

def pop():
    length = len(a)
    if length == 0:
        return
    a[0] = a[length - 1]
    a.pop()
    maxHeapify(0)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i])
        if len(b) < 3:
            print(-1)
        else:
            b.sort()
            res = b[i] * b[i-1] * b[i-2]
            print(res)