
def kahn(adj, deg):
    topo = []
    que = deque(c for c, d in deg.items() if d == 0)
    while que:
        u = que.popleft()
        for v in adj[u]:
            deg[v] -= 1
            if not deg[v]:
                que.append(v)
        topo.append(u)
    if len(topo) != len(deg):
        return ""
    return "".join(topo)


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        deg = {c: 0 for word in words for c in word}

        for w1, w2 in pairwise(words):
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
            for i in range(min_len):
                if w1[i] != w2[i]:
                    u, v = w1[i], w2[i]
                    if v not in adj[u]:
                        adj[u].add(v)
                        deg[v] += 1
                    break
        return kahn(adj, deg)
