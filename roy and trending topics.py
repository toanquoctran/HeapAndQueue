import queue
pq = queue.PriorityQueue()
n = int(input())

class Post:
    def __init__(self, topicID, z, zNew):
        self.topicID = topicID
        self.z = z
        self.zNew = zNew
        self.zChange = zNew - z

    def __lt__(self, other):
        if self.zChange == other.zChange:
            return self.topicID > other.topicID
        return self.zChange > other.zChange

for _ in range(n):
    topicID, z, p, l, c, s = list(map(int, input().split()))
    zNew = p*50 + l*5 + c*10 + s*20
    pq.put(Post(topicID, z, zNew))

for _ in range(5):
    cur = pq.get()
    print(cur.topicID, cur.zNew)