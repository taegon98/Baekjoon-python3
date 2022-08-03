import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int,input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i,j])

def bfs():

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dr[i]
            ny = y+dc[i]

            if 0<=nx<N and 0<=ny<M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx,ny])
bfs()
max = int(1e-9)
for i in range(N):
    for j in range(M):
        if tomato[i][j] > max:
            max = tomato[i][j]
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
print(max-1)