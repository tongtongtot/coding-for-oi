from queue import PriorityQueue
class LFUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.cnt = {}
        self.vis = {}
        self.capacity = capacity
        self.q = PriorityQueue()
        self.num = 0
        self.time = 0

    def get(self, key: int) -> int:

        self.time = self.time + 1

        if key not in self.dict or self.dict[key] == -1:
            return -1
        
        if key not in self.cnt:
            self.cnt.update({key: 1})
        else:
            self.cnt[key] = self.cnt[key] + 1
            print("add", key, self.cnt[key])

        head = self.q.get()
        while self.q.empty() is False and (self.cnt[head[1]] > head[0] or self.cnt[head[1]] == 0):
            head = self.q.get()
        
        self.q.put([self.cnt[head[1]], head[1]])
        print("put", self.cnt[head[1]], head[1])
        self.q.put([self.cnt[key], key])
        print("put", self.cnt[key], key)
        
        return self.dict[key]
        # return self.cnt[key]

    def put(self, key: int, value: int) -> None:
        
        self.time = self.time + 1

        if key not in self.dict or self.dict[key] == -1:
            
            self.num = self.num + 1
            if self.num > self.capacity:
                if self.q.empty() is False:
                    head = self.q.get()
                    while self.q.empty() is False and (self.cnt[head[1]] > head[0] or self.cnt[head[1]] == 0):
                        head = self.q.get()
                        print("while", head[1])
                    print("cnt", self.cnt[head[1]])
                    print("cnt2", self.cnt[2])
                    print("q", self.q.queue)
                    self.cnt[head[1]] = 0 
                    self.dict[head[1]] = -1
                    self.num = self.num - 1
                    print("here", head[1])
        
        if key not in self.cnt:
            self.cnt.update({key: 1})
        else:
            self.cnt[key] = self.cnt[key] + 1
            print("add", key, self.cnt[key])

        self.dict.update({key: value})
        
        self.q.put([self.cnt[key], key])
        print("put", self.cnt[key], key)

capacity = 2

obj = LFUCache(capacity)
obj.put(1,1)
obj.put(2,2)
param_1 = obj.get(1)
obj.put(3,3)
# param_2 = obj.get(2)
# print(param_2)