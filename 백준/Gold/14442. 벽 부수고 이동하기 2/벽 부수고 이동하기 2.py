from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

N,M,K = map(int, input().split())
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]    #각 레이어마다 방문여부 저장리스트
graph = [list(map(int,input().strip())) for _ in range(N)]
dr = [-1,1,0,0]    #상하좌우
dc = [0,0,-1,1]

def bfs() :
    queue.append([0,0,K])
    visited[0][0][K] = 1    #시작점 방문처리
    while queue :
        x,y,z = queue.popleft()
        if x == N-1 and y == M-1 :    #도착시에 return
            return visited[x][y][z]
        for i in range(4):
            nx = dr[i] + x
            ny = dc[i] + y
            if 0<=nx<N and 0<=ny<M :    #범위안에있고
                # 벽이고 and 벽을 부술 수 있고 and 부순 벽에있는 레이어를 방문한적 없으면
                if graph[nx][ny]==1 and z>0 and visited[nx][ny][z-1]==0:
                    visited[nx][ny][z-1] = visited[x][y][z]+1    #한 번 벽을 부순 레이어에 방문횟수 추가
                    queue.append([nx,ny,z-1])    #z-1 -> 한 번 벽을 부순 레이어로 이동
                elif graph[nx][ny]==0 and visited[nx][ny][z]==0:    #통과가능하고 방문한적이 없다면
                    visited[nx][ny][z] = visited[x][y][z]+1
                    queue.append([nx,ny,z])
    return -1    #도착못할시에 return -1

print(bfs())
