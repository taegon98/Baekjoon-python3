import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

def check(t):
    if S == t:
        print(1)
        exit(0)
    if not t:
        return
    if t[-1] == 'A':
        temp = t.pop()
        check(t)
        t.append(temp)
    if t[0] == 'B':
        check(t[::-1][:-1])

check(T)
print(0)