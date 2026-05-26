from collections import defaultdict
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        UNSEEN = 0
        VISITING = 1
        SEEN = 2
        visit = [UNSEEN] * n
        ans = []
        def dfs(u):
            if visit[u] == VISITING:
                return False
            if visit[u] == SEEN:
                return True
            visit[u] = VISITING
            for v in adj[u]:
                if not dfs(v):
                    return False
            visit[u] = SEEN
            ans.append(u)
            return True
        
        for i in range(n):
            dfs(i)

        return list(reversed(ans))