from collections import deque

N,K = map(int,input().split())
d = [0 for _ in range(100001)] #거리 저장
visited = [False for _ in range(100001)] #방문 여부 저장
queue = deque()

def bfs(start):
    queue.append(start)

    while queue:
        p = queue.popleft()
        if p == K:
            return d[p]
        if 0<=(p*2)<=100000 and not visited[p*2]:
            d[p * 2] = d[p]
            visited[p*2] = True
            queue.append(p*2)
        for i in (p-1, p+1):    #각 조건을 차례로 돌면서
            if 0<=i<=100000 and not visited[i]:   #범위 && 방문안했으면
                d[i] = d[p]+1    #이전방문횟수 + 1
                visited[i] = True
                queue.append(i)
n = bfs(N)
print(n)



