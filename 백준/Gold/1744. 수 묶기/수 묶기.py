import sys

input = sys.stdin.readline

N = int(input().rstrip())
pos_l = []
neg_l = []
for _ in range(N):
    pos_l.append(int(input().rstrip()))
pos_l.sort(reverse=True)

for i in range(N):
    if pos_l[i] <= 0:
        neg_l = pos_l[i:]
        pos_l = pos_l[:i]
        break
neg_l.sort()
sum = 0

for i in range(0, len(pos_l),2):
    if i >= len(pos_l)-1:
        sum += pos_l[i]
        break
    if pos_l[i] > 0 and pos_l[i+1] > 1:
        sum += (pos_l[i] * pos_l[i+1])
    else:
        sum += pos_l[i] + 1

for i in range(0, len(neg_l), 2):
    if i >= len(neg_l) - 1:
        sum += neg_l[i]
        break
    if neg_l[i] < 0 and neg_l[i + 1] <= 0:
        sum += (neg_l[i] * neg_l[i + 1])

print(sum)
