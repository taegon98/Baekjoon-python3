import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
result = []
comp_count =0

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y):
    visited[x][y] = True
    queue = deque()
    queue.append([x,y])
    house_count = 1
    while queue:
        X,Y = queue.popleft()

        for i in range(4):
            NX = X+dr[i]
            NY = Y+dc[i]

            if 0<=NX<N and 0<=NY<N and not visited[NX][NY]:
                visited[NX][NY] = True
                if graph[NX][NY] == 1:
                    queue.append([NX,NY])
                    house_count+=1
    return house_count
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))
            comp_count+=1

result.sort()
print(comp_count)
for i in result:
    print(i)