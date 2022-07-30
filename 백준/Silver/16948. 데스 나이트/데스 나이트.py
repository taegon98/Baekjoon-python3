import sys
from collections import deque

N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int,sys.stdin.readline().split())
chess = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

dr = [-2,-2,0,0,2,2]    #이동할 수 있는 방향 배열
dc = [-1,1,-2,2,-1,1]

def bfs(r,c):
    queue.append((r,c))

    while queue:
        x,y = queue.popleft()   #FIFO
        if x == r2 and y == c2:    #가장 먼저 도착하게 되면 출력 후 프로그램 종료
            print(chess[x][y])
            exit(0)
        for i in range(6):  #6방향에 대한 for문
            nx = x+dr[i]
            ny = y+dc[i]
            #범위를 벗어나지 않고 탐색을 하지 않았다면
            if 0<=nx<N and 0<=ny<N and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1    #이전 탐색횟수 + 1
                queue.append((nx, ny))

bfs(r1, c1)
print(-1)    #도착지에 도달하지 못하면 -1출력