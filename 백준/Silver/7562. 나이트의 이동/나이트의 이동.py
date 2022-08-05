from collections import deque

n = int(input())

dx = [-2,-2,2,2,-1,-1,1,1]
dy = [-1,1,-1,1,-2,2,-2,2]

for _ in range(n):
    c = int(input())
    graph = [[0 for _ in range(c)] for _ in range(c)]

    d_x, d_y = map(int,input().split())
    a_x, a_y = map(int,input().split())
    queue = deque()
    queue.append((d_x, d_y))
    while queue:
        x, y = queue.popleft()
        if x==a_x and y==a_y:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= c or ny >= c: continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    print(graph[a_x][a_y])
