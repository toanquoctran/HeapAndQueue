import queue

s = []
q = queue.Queue()
class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
pq = queue.PriorityQueue()

numStack = 0
numQueue = 0
numPriorityQueue = 0

n = int(input())
count = 0

for _ in range(n):
    x = list(map(int, input().split()))
    if x[0] == 1:
        s.append(x[1])
        q.put(x[1])
        pq.put(PQEntry(x[1]))
    elif x[0] == 2:
        count += 1
        if len(s) != 0 and s[-1] == x[1]:
            s.pop()
            numStack += 1
        if not q.empty() and q.queue[0] == x[1]:
            q.get()
            numQueue += 1
        if not pq.empty() and pq.queue[0].value == x[1]:
            pq.get()
            numPriorityQueue += 1

if (numStack == count and numQueue == count) or (numQueue == count and numPriorityQueue == count) or (numPriorityQueue == count and numStack == count):
    print("not sure")
elif numStack != count and numQueue != count and numPriorityQueue != count:
    print("impossible")
elif numStack == count:
    print("stack")
elif numQueue == count:
    print("queue")
elif numPriorityQueue == count:
    print("priority queue")