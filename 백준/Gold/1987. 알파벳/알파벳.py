import sys

R, C = map(int, sys.stdin.readline().split())
chess = []
alpha = [False for _ in range(26)]
max_value = 1    #시작점을 포함하므로 1
dr = [-1, 1, 0, 0]    #상하좌우
dc = [0, 0, -1, 1]

for i in range(R):
    chess.append(list(sys.stdin.readline().rstrip()))

def dfs(r, c, count):
    global max_value
    max_value = max(max_value, count)

    for i in range(4):    #4방향 모두검사
        nr = r + dr[i]
        nc = c + dc[i]
        #범위를 벗어나지않고 방문할 지점의 알파벳을 가진적이 없다면
        if 0 <= nr < R and 0 <= nc < C and not alpha[ord(chess[nr][nc]) -65]:
            alpha[ord(chess[nr][nc])-65] = True
            dfs(nr, nc, count+1)    #방문할 행, 열, 카운트증가 -> 탐색
            alpha[ord(chess[nr][nc])-65] = False    #백트랙킹 ->

alpha[ord(chess[0][0])-65] = True    #시작점에있는 알파벳 add
dfs(0,0,1)    #시작점부터 탐색
print(max_value)