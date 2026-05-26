class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        UNVISITED = 0
        VISITING = 1
        VISTED = 2
        state = [UNVISITED] * numCourses

        def dfs(u):
            if state[u] == VISITING:
                return False
            
            state[u] = VISITING
            for v in adj[u]:
                if state[v] == UNVISITED:
                    if not dfs(v):
                        return False
                elif state[v] == VISITING: # <--- 必須明確捕捉正在訪問的節點！
                    return False
                    
            state[u] = VISTED # 註：你這裡拼錯字了，應該是 VISITED，但不影響邏輯
            return True

        for i in range(numCourses):
            if state[i] == UNVISITED:
                if not dfs(i):
                    return False
        return True
