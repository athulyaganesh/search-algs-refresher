class DisjointSet: 
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, i): 
        if i == self.parent[i]: 
            return i 
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i] 

    def union(self, i, j): 
        i = self.find(i)
        j = self.find(j)
        
        if i == j: 
            return False 
        
        if self.rank[i] < self.rank[j]: 
            self.parent[i] = j 
        elif self.rank[i] > self.rank[j]: 
            self.parent[j] = i 
        else: 
            self.parent[i] = j 
            self.rank[i] += 1
        return True 
    
    def intersect(self, i, j): 
        return self.find(i) == self.find(j)

s = DisjointSet(5) 