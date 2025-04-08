class DisjointedSets:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])  # Path compression
        return self.par[node]

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)

        if p1 == p2:
            return False  # already in same set
        if self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

# Example usage:
def find_invalid_edge(n, edges):
    ds = DisjointedSets(n)
    for node1, node2 in edges:
        if not ds.union(node1, node2):
            return [node1, node2]
    return None

