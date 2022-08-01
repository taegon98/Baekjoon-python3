import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
queue = deque()

dr = [-1,1,0,0]    #4방향
dc = [0,0,-1,1]

def bfs(r,c,s):
    global result
    queue.append([r,c])

    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            #범위를 벗어나지 않고 방문한적이 없다면
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if graph[nx][ny] == s:    #해당 index 색 = 탐색하고자 하는 색
                    visited[nx][ny] = True
                    queue.append([nx,ny])
    result+=1    #한 구간 탐색 후 증감

for i in range(2):
    result = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i,j,graph[i][j])
    print(result)
    for i in range(N):    #적록색약 R==G -> G->R로 바꾸기
        for j in range(N):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'
