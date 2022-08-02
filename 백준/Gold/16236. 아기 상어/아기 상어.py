import sys
from collections import deque
shark_x, shark_y = 0,0
shark_size = 2    #초기 상어 사이즈
eat_cnt = 0    #먹은 횟수
fish_cnt = 0    #반복문 반복 횟수 결정
fish_pos = []
time = 0
dx = (0,0,1,-1)    #좌우하상
dy = (1,-1,0,0)
n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if 0 < board[i][j] <=6:    #물고기가 있으면 물고기 갯수 증감
            fish_cnt +=1
            fish_pos.append((i,j))
        elif board[i][j] == 9:    #상어가있는 위치를 변수에 따로 저장
            shark_x, shark_y = i,j    #상어의 크기가 9라고 생각할 수 있으므로
board[shark_x][shark_y]=0

def bfs(shark_x,shark_y):
    q = deque()
    q .append((shark_x,shark_y,0))    #x위치, y위치, 거리
    dist_list = []    #탐색할때마다 초기화
    visited = [[False]*n for _ in range(n)]
    visited[shark_x][shark_y] = True    #시작점 방문처리
    min_dist = int(1e9)    #가장큰수로 min값 저장
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y
            if 0<=xx<n and 0<=yy<n and not visited[xx][yy]:    #범위에있고 방문하지 않았다면
                if board[xx][yy] <= shark_size:    #같은 크기거나 작으면(지나갈 수 있거나 먹을 수 있으면)
                    visited[xx][yy] = True
                    if 0<board[xx][yy]<shark_size:    #먹을 수 있으면
                        min_dist = dist    #먹을 물고기까지의 거리로 갱신
                        dist_list.append((dist+1,xx,yy))    #거리저장 리스트에 추가
                    if dist+1 <= min_dist:
                        q.append((xx,yy,dist+1))
    if dist_list:
        dist_list.sort()    #가장 앞에있는 최소값 return 하기위해
        return dist_list[0]
    else:
        return False

while fish_cnt :
    result = bfs(shark_x,shark_y)
    if not result:    #먹을 수 있는 물고기가 없다면
        break
    shark_x,shark_y = result[1],result[2]    #물고기를 먹고나서 상어 위치 저장
    time +=result[0]    #걸린 시간(거리 1 = 시간 1초)
    eat_cnt+=1    #먹은 횟수증가(상어 사이즈 키우기위해
    fish_cnt-=1    #반복문 횟수 감소시키기
    if shark_size == eat_cnt:    #넘어서면 상어 사이즈 증가
        shark_size +=1
        eat_cnt =0    #초기화
    board[shark_x][shark_y] = 0    #먹은 후 -> 0으로 바꿈

print(time)