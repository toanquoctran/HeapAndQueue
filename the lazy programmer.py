import queue

class Job:
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.d = d
    def __lt__(self, other):
        return self.d < other.d

class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value

t = int(input())
for _ in range(t):
    time = 0
    money = 0
    jobs = []
    maxHeap = queue.PriorityQueue()
    n = int(input())
    for _ in range(n):
        a, b, d = map(int, input().split())
        jobs.append(Job(a, b, d))
    jobs.sort()
    for i in range(len(jobs)):
        a = jobs[i].a
        b = jobs[i].b
        d = jobs[i].d
        time += b
        maxHeap.put((PQEntry(a), b, d))
        while time > d:
            ta, tb, td = maxHeap.get()
            if tb > time - d:
                money += (time - d) / ta.value
                tb -= time - d
                time = d
                maxHeap.put((ta, tb, td))
            else:
                time -= tb
                money += tb / ta.value
    print("%.2f" % money)