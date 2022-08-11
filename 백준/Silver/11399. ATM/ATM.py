import sys
input = sys.stdin.readline

N = int(input().rstrip())
line = list(map(int,input().split()))
line.sort()    #인출시간이 가장 빠른 사람들부터 정렬

time = 0

for i in range(0,len(line)):    #첫번째~마지막 사람까지 기다린 시간 누적
    for j in range(0, i+1):
        time += line[j]
print(time)
