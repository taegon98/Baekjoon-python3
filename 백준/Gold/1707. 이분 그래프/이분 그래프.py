import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

def bfs(start, g):
    queue = deque()
    queue.append(start)
    visited[start] = g

    while queue:
        s = queue.popleft()
        for i in graph[s]:
            if not visited[i]:
                visited[i] = -1 * visited[s]
                queue.append(i)
            elif visited[i] == visited[s]:
                return False
    return True

for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)

    for _ in range(E):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, V+1):
        if not visited[i]:
            result = bfs(i,1)
            if not result:
                break
    print("YES" if result else "NO")
