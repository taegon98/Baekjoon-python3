import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y):
    visited[x][y] = 0
    queue = deque()

    queue.append([x,y])
    while queue:
        X,Y = queue.popleft()
        if X == N-1 and Y == M-1:
            print(visited[X][Y])
            exit(0)
        for i in range(4):
            NX = X+dr[i]
            NY = Y+dc[i]

            if 0<=NX<N and 0<=NY<M and visited[NX][NY] == -1:
                if graph[NX][NY] == 0:
                    visited[NX][NY] = visited[X][Y]
                    queue.appendleft([NX,NY])
                elif graph[NX][NY] == 1:
                    visited[NX][NY] = visited[X][Y] + 1
                    queue.append([NX,NY])
bfs(0,0)