import sys
N,S = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
count = 0

def sum(index, tot):
    global count
    if index >= N:
        return
    tot += l[index]

    if tot == S:
        count+=1
    sum(index+1, tot)
    sum(index+1, tot-l[index])

sum(0,0)
print(count)