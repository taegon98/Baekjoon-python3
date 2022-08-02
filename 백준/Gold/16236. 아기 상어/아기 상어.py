import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
fish_eat = 0    #몇 마리 먹었는지
fish_count = 0    #몇 마리 있는지
time = 0    #먹는데 걸린시간
shark_size = 2    #상어 사이즈
shark_x, shark_y = 0,0

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:    #상어면
            shark_x, shark_y = i,j    #위치 저장
            graph[i][j] = 0    #9인상태로 있으면 탐색때마다 9가 물고기로 간주되므로
        elif graph[i][j] != 0:    #물고기면 카운트 증감
            fish_count+=1

def bfs(x,y):
    visited = [[False for _ in range(N)] for _ in range(N)]
    dist = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append([x,y])
    temp = []    #가장 가까운 물고기 위치정보 저장 리스트
    visited[x][y] = True

    while queue:
        X,Y = queue.popleft()

        for i in range(4):
            NX = X+dr[i]
            NY = Y+dc[i]

            if 0<=NX<N and 0<=NY<N and not visited[NX][NY]:    #범위안에있고 방문한적이 없다면
                if graph[NX][NY] <= shark_size:    #지날 수 있으면
                    visited[NX][NY] = True    #방문처리
                    dist[NX][NY] = dist[X][Y] + 1    #현재 = 이전 + 1
                    queue.append([NX,NY])
                    if 0 < graph[NX][NY] < shark_size:    #먹을 수 있으면
                        temp.append([dist[NX][NY],NX,NY])    #먹은 물고기의 위치 정보 저장

    if temp:
        temp.sort()    #거리순 -> 행(위쪽) -> 열(왼쪽) 정렬
        return temp[0]
    else:
        return False    #비어있으면 물고기 없다

while fish_count:    #물고기 다 먹을때까지
    result = bfs(shark_x, shark_y)
    if not result:    #물고기 없으면 종료
        break
    shark_x, shark_y = result[1], result[2]    #먹은 물고기 좌표정보 저장 -> 먹은 물고기부터 탐색
    time += result[0]    #걸린 시간(거리1 = 시간1초)
    fish_eat += 1    #먹은횟수 1 증가
    fish_count -=1    #물고기 1마리 먹힘

    if fish_eat == shark_size:    #사이즈만큼 먹으면
        shark_size+=1    #아기상어 사이즈 1증가
        fish_eat = 0    #초기화
    graph[shark_x][shark_y] = 0
print(time)
