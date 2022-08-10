N, K = map(int,input().split())
list = ['B' for _ in range(N)]
flag = 0
for i in range(N):
    list[i] = 'A'
    count = 0

    for j in range(0,len(list)-1):
        if list[j] == 'A':
            for k in range(j+1, len(list)):
                if list[k] == 'B':
                    count+=1
    if K == count:
        flag = 1
        break
    elif K < count:
        list[i] = 'B'

if flag == 1: print("".join(list))
else: print(-1)