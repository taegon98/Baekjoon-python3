import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int,input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

dr = [-1,1,0,0]    #상하좌우
dc = [0,0,-1,1]

for i in range(N):    #토마토가 익은 곳의 위치만 append
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:    #접근 가능한 곳의 토마토가 모두 익을때까지 반복(0이 없을때까지)
        x,y = queue.popleft()

        for i in range(4):    #4방향으로 0이 없을때까지 반복
            nx = x+dr[i]
            ny = y+dc[i]
            #범위안에있고 토마토가 익지 않았으면(0이 있으면)
            if 0<=nx<N and 0<=ny<M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1    #토마토 익기까지의 거리(날짜) + 1
                queue.append([nx,ny])
bfs()
max = int(1e-9)    #최대 값 갱신위해 가장 작은 수 저장
for i in range(N):
    for j in range(M):
        if tomato[i][j] > max:    #가장 긴 거리 = 다 익을때까지 걸리 날짜 수
            max = tomato[i][j]
        if tomato[i][j] == 0:    #익지 않은 토마토가 있으면 -1 -> 종료
            print(-1)
            exit(0)
print(max-1)    #1에서 시작했으므로 거리-1