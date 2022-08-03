import sys

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

def dfs(start, count):
    visited[start] = True
    if count == 4:
        print(1)
        exit(0)

    for i in graph[start]:
        if not visited[i]:
            dfs(i, count+1)
            visited[i] = False

for _ in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(N):
    dfs(i, 0)
    visited[i] = False
print(0)