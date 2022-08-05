import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dr = [-2, -2, 2, 2, -1, -1, 1, 1]    #나이트가 이동할 수 있는 8방향
dc = [-1, 1, -1, 1, -2, 2, -2, 2]

for i in range(N):    #테스트 케이스만큼 반복
    M = int(input())    #행렬 크기 입력받음
    start_x, start_y = map(int, input().split())    #시작지점
    arr_x, arr_y = map(int, input().split())    #도착지점
    graph = [[0 for _ in range(M)] for _ in range(M)]    #거리 저장 리스트

    def bfs(x,y):
        queue = deque()
        queue.append([x,y])

        while queue:
            X,Y = queue.popleft()
            if X==arr_x and Y==arr_y:    #도착하면 return
                return graph[X][Y]
            for i in range(8):
                NX = X+dr[i]
                NY = Y+dc[i]
                #범위안에있고 방문한적이없다면(0이라면)
                if 0<=NX<M and 0<=NY<M and graph[NX][NY] == 0:
                    graph[NX][NY] = graph[X][Y] + 1    #방문횟수 1증가
                    queue.append([NX,NY])

    print(bfs(start_x,start_y))
