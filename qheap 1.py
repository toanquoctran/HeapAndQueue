import queue
pq1 = queue.PriorityQueue()
pq2 = queue.PriorityQueue()

q = int(input())
for _ in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        v = a[1]
        pq1.put(v)
    elif a[0] == 2:
        v = a[1]
        pq2.put(v)
    elif a[0] == 3:
        while not pq1.empty() and not pq2.empty() and pq2.queue[0] == pq1.queue[0]:
            pq1.get()
            pq2.get()
        print(pq1.queue[0])