N,M,K = map(int,input().split())
count = 0

while True:
    N -= 2
    M -= 1
    if N>=0 and M>=0 and N+M >= K:
        count+=1
    else:
        print(count)
        exit(0)