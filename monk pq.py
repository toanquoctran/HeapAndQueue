import queue
pq = queue.PriorityQueue()
class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    y = 0
    z = 0
    for i in a:
        pq.put(PQEntry(i))
        if len(pq.queue) < 3:
            print(-1)
        else:
            x = pq.queue[0]
            pq.get()
            y = pq.queue[0]
            pq.get()
            z = pq.queue[0]
            pq.get()
            pq.put(x)
            pq.put(y)
            pq.put(z)
            print(x.value * y.value * z.value)