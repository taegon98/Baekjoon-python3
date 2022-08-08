import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = [list(map(int,input().rstrip())) for _ in range(N)]
B = [list(map(int,input().rstrip())) for _ in range(N)]
count = 0

for i in range(0, N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if A[k][l] == 0: A[k][l] = 1
                    else: A[k][l] = 0
            count += 1

if A == B:
    print(count)
else:
    print(-1)
