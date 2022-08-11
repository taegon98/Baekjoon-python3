import sys

n = int(input())
tat = []
num_list = list(map(int,input().split()))
num_list.sort()

for i in range(n):
     tot = num_list[i]
     for j in range(i-1,-1,-1):
          tot += num_list[j]
     tat.append(tot)

print(sum(tat))