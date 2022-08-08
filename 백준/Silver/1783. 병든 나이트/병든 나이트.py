import math
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

if N == 1:
    print(1)
elif N == 2:
    if M > 6:
        print(4)
    elif M >= 5:
        print(3)
    elif M >= 3:
        print(2)
    else:
        print(1)
else:
    if M < 4:
        print(M)
    elif M < 7:
        print(4)
    else:
        print(M-2)
