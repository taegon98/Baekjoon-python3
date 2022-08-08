import math
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

if N == 1:    #세로 길이가 1이면
    print(1)    #처음 시작지점 1개
elif N == 2:    #세로 길이가 2이면
    print(min(4, (M+1)//2))    
else:    #세로 길이가 3이상인 경우
    if M < 4:    #가로길이가 4미만인 경우
        print(M)
    elif M < 7:    #가로길이가 7미만인 경우
        print(4)
    else:    #가로길이가 7이상인 경우
        print(M-2)
