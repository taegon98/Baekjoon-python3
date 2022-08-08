import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = [list(map(int,input().rstrip())) for _ in range(N)]
B = [list(map(int,input().rstrip())) for _ in range(N)]
count = 0

for i in range(0, N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:    #값이 다르면
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if A[k][l] == 0: A[k][l] = 1    #3x3행렬의 전체 값 reverse
                    else: A[k][l] = 0
            count += 1    #전체 값을 reverse할때마다 count값 증가

if A == B:    #A행렬과 B행렬이 같으면
    print(count)    
    exit(0)

print(-1)    #같지 않으면
