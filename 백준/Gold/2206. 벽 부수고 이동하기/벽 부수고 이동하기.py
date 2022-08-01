import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
queue = deque()

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y,z):
    queue.append([x,y,z])
    visited[x][y][z] = 1
    while queue:
        X,Y,Z = queue.popleft()

        if X == N-1 and Y == M-1:
            print(visited[X][Y][Z])
            exit(0)
        for i in range(4):
            NX = X+dr[i]
            NY = Y+dc[i]

            if 0<=NX<N and 0<=NY<M:
                if graph[NX][NY] == 0 and visited[NX][NY][Z] == 0:
                    visited[NX][NY][Z] = visited[X][Y][Z] + 1
                    queue.append([NX,NY,Z])
                elif Z > 0 and visited[NX][NY][Z-1] == 0:
                    visited[NX][NY][Z-1] = visited[X][Y][Z] + 1
                    queue.append([NX,NY,Z-1])
bfs(0,0,1)
print(-1)