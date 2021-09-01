import queue
topReviews = queue.PriorityQueue()
class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
allReviews = queue.PriorityQueue()

n = int(input())
nReviews = 0
for _ in range(n):
    line = list(map(int, input().split()))

    if line[0] == 1:
        nReviews += 1
        x = line[1]

        if not topReviews.empty() and x > topReviews.queue[0]:
            temp = topReviews.get()
            allReviews.put(PQEntry(temp))
            topReviews.put(x)

        else:
            allReviews.put(PQEntry(x))

        if nReviews % 3 == 0:
            topReviews.put(allReviews.get().value)

    elif line[0] == 2:
        if topReviews.empty():
            print("No reviews yet")
        else:
            print(topReviews.queue[0])