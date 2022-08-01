import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, g):
    queue = deque()
    queue.append(start)
    visited[start] = g

    while queue:
        index = queue.popleft()
        for i in graph[index]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[index]
            elif visited[i] == visited[index]:
                return False
    return True

K = int(input())

for _ in range(K):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1):
        if not visited[i]:
            res = bfs(i,1)
            if not res: break
    print('YES' if res else 'NO')
