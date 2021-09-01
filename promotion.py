import queue
pqMin = queue.PriorityQueue()

class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

receipts = [0]*1000002
pqMax = queue.PriorityQueue()

n = int(input())
totalPrize = 0

for _ in range(n):
    sums = list(map(int, input().split()))
    
    for i in range(1, len(sums)):
        receipts[sums[i]] += 1
        pqMin.put(sums[i])
        pqMax.put(PQEntry(sums[i]))
        
    while receipts[pqMax.queue[0].value] == 0:
        pqMax.get()
    receipts[pqMax.queue[0].value] -= 1

    while receipts[pqMin.queue[0]] == 0:
        pqMin.get()
    receipts[pqMin.queue[0]] -= 1

    largestSum = pqMax.queue[0]
    smallestSum = pqMin.queue[0]
    prize = largestSum.value - smallestSum
    pqMax.get()
    pqMin.get()
    totalPrize += prize
print(totalPrize)