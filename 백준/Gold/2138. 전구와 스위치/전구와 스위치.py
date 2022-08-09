import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int,input().rstrip()))
B = list(map(int,input().rstrip()))

def bulb(L,D):
    count = 0
    C = L[:]
    for k in range(1,len(C)):
        if C[k-1] != D[k-1]:
            count+=1
            if k == len(C)-1:
                for l in k-1,k:
                    if C[l] == 0: C[l] = 1
                    else: C[l] = 0
            else:
                for l in k-1,k,k+1:
                    if C[l] == 0: C[l] = 1
                    else: C[l] = 0
    if C == D:
        return count
    else: return 1e9

result = bulb(A,B)
for i in 0, 1:
    if A[i] == 0: A[i] = 1
    else: A[i] = 0
result = min(result, bulb(A,B)+1)
print(result if result != 1e9 else -1)