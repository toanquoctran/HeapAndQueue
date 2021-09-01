import queue

while True:
    n = int(input())
    pq = queue.PriorityQueue()
    sum = 0
    tempSum = 0
    if n == 0:
        break
    a = list(map(int, input().split()))
    for i in a:
        pq.put(i)
    while len(pq.queue) > 1:
        first = pq.get()
        second = pq.get()
        tempSum = first + second
        sum += tempSum
        pq.put(tempSum)
    print(sum)