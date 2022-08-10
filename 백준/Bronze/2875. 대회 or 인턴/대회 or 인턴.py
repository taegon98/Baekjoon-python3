N,M,K = map(int,input().split())
count = 0

while True:
    N -= 2    #대회에 참여하는 인원 감소
    M -= 1
    if N>=0 and M>=0 and N+M >= K:    #인원수를 벗어나지 않고 참여해야하는 인원이 남아있으면
        count+=1
    else:    #감소 후 인원을 벗어나거나 참여해야하는 인원이 남아있지 않으면
        print(count)
        exit(0)
