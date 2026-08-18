import sys
sys.setrecursionlimit(10**7)

class LCA:
    def __init__(self, n):
        self.n = n
        self.LOG = (n).bit_length()  # ~ log2(n)
        self.adj = [[] for _ in range(n + 1)]
        self.depth = [0] * (n + 1)
        self.up = [[0] * self.LOG for _ in range(n + 1)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, v, p):
        self.up[v][0] = p
        for i in range(1, self.LOG):
            self.up[v][i] = self.up[self.up[v][i - 1]][i - 1]

        for to in self.adj[v]:
            if to != p:
                self.depth[to] = self.depth[v] + 1
                self.dfs(to, v)

    def build(self, root=1):
        self.depth[root] = 0
        self.dfs(root, root)

    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a

       
        diff = self.depth[a] - self.depth[b]
        for i in range(self.LOG):
            if diff & (1 << i):
                a = self.up[a][i]

        if a == b:
            return a

        
        for i in reversed(range(self.LOG)):
            if self.up[a][i] != self.up[b][i]:
                a = self.up[a][i]
                b = self.up[b][i]

        return self.up[a][0]
