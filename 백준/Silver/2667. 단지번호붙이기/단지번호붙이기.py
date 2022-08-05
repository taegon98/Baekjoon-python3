import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]    #방문여부
result = []    #단지마다 집 갯수 저장 리스트
comp_count =0    #단지 수 카운트

dr = [-1,1,0,0]    #상하좌우
dc = [0,0,-1,1]

def bfs(x,y):
    visited[x][y] = True
    queue = deque()
    queue.append([x,y])
    house_count = 1    #집 갯수 카운트(시작지점의 집 포함하므로 -> 1)
    while queue:
        X,Y = queue.popleft()

        for i in range(4):
            NX = X+dr[i]
            NY = Y+dc[i]
            #범위안에있고 방문한적이없다면
            if 0<=NX<N and 0<=NY<N and not visited[NX][NY]:
                visited[NX][NY] = True    #방문처리
                if graph[NX][NY] == 1:    #연결된 집이있으면 덱에 append -> 탐색
                    queue.append([NX,NY])
                    house_count+=1    #집의 갯수 증감
    return house_count    #집 갯수 return

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:    #집이있고 방문한적이 없다면
            result.append(bfs(i,j))    #return된 집의 갯수 저장
            comp_count+=1    #위 탐색을 통해 연결되어있는 모든 집 방문처리 -> 단지수 증감

result.sort()    #오름차순 정렬
print(comp_count)
for i in result:
    print(i)
